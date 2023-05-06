#tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from peewee import *
from playhouse.shortcuts import model_to_dict
from app import TimelinePost

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        #assert "<title>MLH Fellow</title>" in html
        assert "<h1>Team Projects</h1>" in html        
        assert "<h1>Santiago Vera Espinoza</h1>" in html

        # TODO Add more tests relating to the home page

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

    #TODO Add more tests relating to the /api/timeline_post
        TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')

        timeline_post1 = [
                model_to_dict(p)
                for p in TimelinePost.select()
            ]

        assert timeline_post1[0]['id'] == 1
        assert timeline_post1[0]['name'] == 'John Doe'
        assert timeline_post1[0]['email'] == 'john@example.com'
        assert timeline_post1[0]['content'] == 'Hello world, I\'m John!'

        
    #TODO Add more tests relating to the the timeline page
    def test_timeline_page(self):
        response = self.client.get("/timeline")
        #assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert "</form>" in html
        assert "</script>" in html
        assert "<div class=\"top_post_box\">" in html 


    #error or edge cases
    def test_malformed_timeline_post(self):
        # POST request missing name

        response = self.client.post("/api/timeline_post", data= {"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data= {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data= {"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Email" in html

