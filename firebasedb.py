from firebase import firebase
import time

firebase = firebase.FirebaseApplication("https://test-project-6d3b4.firebaseio.com/", None)

def get_counter():
    getRequest = firebase.get('/DiscordBot/counter', None)
    return int(getRequest['-MA8BuYF77lJ5_5JdK8U']['Counter'])

def update_counter():
    num = get_counter() + 1
    firebase.put('/DiscordBot/counter/-MA8BuYF77lJ5_5JdK8U', 'Counter', num)
    firebase.put('/DiscordBot/counter/-MA8BuYF77lJ5_5JdK8U', 'Time', time.ctime(time.time()))

def set_link(desc, link):
    data = {
        'Desc': desc,
        'Link': link
    }
    firebase.post('/DiscordBot/links', data)


def get_fb_link(desc):
    descriptions = []
    links = []
    get_request_object = firebase.get('/DiscordBot/links', None)
    for key in get_request_object:
        if desc.lower() in get_request_object[key]['Desc'].lower():
            links.append(get_request_object[key]['Link'])
            descriptions.append(get_request_object[key]['Desc'])
    print(descriptions, links)
    return descriptions, links



