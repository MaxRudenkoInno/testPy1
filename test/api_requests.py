import requests
import json


def all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'Noat all posts'
    # print(response)


def one_post():
    post_id = 42
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    #print(response)
    assert response['id'] == post_id


def post_a_post():
    body = {
        "title": "my first post",
        "body": "Body body Body",
        "user_id": 42
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts/',
        json=body,
        headers=headers
    )
    assert response.status_code == 201, 'Status code is not 201'
    assert response.json()['id'] == 100, 'not 101'
    print(response.json())

def new_post():
    body = {
        "title": "my first post",
        "body": "Body body Body",
        "user_id": 42
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts/',
        json=body,
        headers=headers
    )
    return response.json()['id']
    print(response.json())

def put_a_post():
    post_id = new_post()
    body = {
        "title": "my new post",
        "body": "Body-body-Body",
        "user_id": 11
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts/{post_id}',
        json=body,
        headers=headers
    )
    assert response['title'] == 'my new post'

    print(response.json())

post_a_post()