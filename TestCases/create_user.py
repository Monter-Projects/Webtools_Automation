import requests
import jsonpath
import json

def url():
    return "https://reqres.in/"

post_create_api = url() + '/api/users'
put_api = url() + '/api/users/2'

def test_Create_User():
    post_response = requests.post(post_create_api)
    print(post_response)
    request_post_json = read_data()
    post_data = requests.post(post_create_api, request_post_json)
    print("Posted data:", post_data)
    header_data = post_data.content
    convert_json = json.loads(header_data)
    get_data = convert_json.get('name')
    if get_data == 'kiran':
        print("got data is matching with posted data:", get_data)
        assert True
    else:
        print("got data: ", get_data)
        assert False

def test_put_response():
    request_put_json = read_data()
    put_data = requests.put(put_api,request_put_json)
    print(put_data)
    print("Content of put_user: ", put_data.content)
    print(put_data.content)
    convert_json = json.loads(put_data.text)
    get_data = convert_json.get('job')
    print("Put_get_Data: ", get_data)
    if get_data == "senior-QA":
        print("Your are doing perfect job")
        assert True
    else:
        print("you need to try for new job")
        assert False

def read_data():
    file = open(r'C:\Users\kirkumar\OneDrive - Electronics for Imaging, Inc\Desktop\pythonProject1\venv\create_user.json', 'r')
    json_input = file.read()
    request_post_json = json.loads(json_input)
    print(request_post_json)
    return request_post_json

