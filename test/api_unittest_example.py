import unittest
import requests
import sys

class TestPostApi(unittest.TestCase):
    # Precondition
    # def setUp(self) -> None:

    # Postcondition
    # def tearDown(self) -> None:

    def setUp(self):
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
        self.post_id = response.json()['id']
        print(f'Post created: {self.post_id}')

    # Postcondition
    def tearDown(self) -> None:
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        print(f'Post deleted: {self.post_id}')

    @unittest.skip("Error happened")
    def test_get_one_post(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id)

class TestIndependent(unittest.TestCase):

    @unittest.skipIf(sys.platform == 'linux', "no Windows only test")
    def test_get_all_posts (self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)

    def test_add_post(self):
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
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], 101)
