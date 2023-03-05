from app.users import *
from peewee import *
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from playhouse.shortcuts import model_to_dict

import os
import datetime
import requests
import json
from flask import render_template_string

load_dotenv()

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route('/')
def index():
    return render_template('index.html', team_projects= team_projects, url=os.getenv("URL"))


""" Xavier Flask Routes """
@app.route('/xavier-aboutme')
def xav_aboutme():
    return render_template('about.html', title="Xavier's Profile", name="Xavier", contact_info=xavier_about["contact"], about_me=xavier_about["aboutme"],
                           pic_url="./static/img/XavierPP.png",
                           about_route="xav_aboutme",
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           education_route='xav_education',
                           places_route='xav_places',
                           user_hobbies=xavier_hobby,
                           url=os.getenv("URL"))


@app.route('/xavier-work')
def xav_work():
    return render_template('work.html', title="Xavier's Profile", name="Xavier",
                           work_length="Jan 30/2023 - April 30/2023",
                           pic_url="./static/img/XavierPP.png",
                           about_route="xav_aboutme",
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           education_route='xav_education',
                           places_route='xav_places',
                           career=xavier_career,  # Uses xavier_career dict to fill out details
                           user_education=xavier_education,
                           url=os.getenv("URL"))


@app.route('/xavier-education')
def xav_education():
    return render_template('education.html', title="Xavier's Profile", name="Xavier",
                           pic_url="./static/img/XavierPP.png",
                           about_route="xav_aboutme",
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           education_route='xav_education',
                           places_route='xav_places',
                           url=os.getenv("URL"))


@app.route('/xavier-hobbies')
def xav_hobby():
    return render_template('hobbies.html', title="Xavier's Profile", name="Xavier",
                           pic_url="./static/img/XavierPP.png",
                           about_route="xav_aboutme",
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           user_hobbies=xavier_hobby,
                           education_route='xav_education',
                           places_route='xav_places',
                           url=os.getenv("URL"))


@app.route('/xavier-places')
def xav_places():
    return render_template('places.html', title="Xavier's Profile", name="Xavier",
                           pic_url="./static/img/XavierPP.png",
                           about_route='xav_aboutme',
                           work_route='xav_work',
                           hobby_route='xav_hobby',
                           education_route='xav_education',
                           places_route='xav_places',
                           mapper=xavier_mapper,
                           #    mapperjson=json.dumps(xavier_mapper),
                           url=os.getenv("URL"))


""" Santiago Flask Routes """
"Santiago About Me"


@app.route('/santiago-aboutme')
def san_aboutme():
    return render_template('about.html', title="Santiago's Profile", name="Santiago", contact_info=santiago_about["contact"], about_me=santiago_about["aboutme"],
                           pic_url="./static/img/SantiagoPP.png",
                           about_route='san_aboutme',
                           work_route='san_work',
                           hobby_route='san_hobby',
                           education_route='san_education',
                           places_route='san_places',
                           url=os.getenv("URL"))


@app.route('/santiago-work')
def san_work():
    return render_template('work.html', title="Santiago's Profile", name="Santiago",
                           pic_url="./static/img/SantiagoPP.png",
                           about_route='san_aboutme',
                           work_route='san_work',
                           hobby_route='san_hobby',
                           education_route='san_education',
                           places_route='san_places',
                           career=santiago_career,  # Uses xavier_career dict to fill out details
                           user_education=santiago_education,
                           url=os.getenv("URL"))


@app.route('/santiago-hobbies')
def san_hobby():
    return render_template('hobbies.html', title="Santiago's Profile", name="Santiago",
                           pic_url="./static/img/SantiagoPP.png",
                           about_route='san_aboutme',
                           work_route='san_work',
                           hobby_route='san_hobby',
                           education_route='san_education',
                           places_route='san_places',
                           user_hobbies=santiago_hobby,
                           url=os.getenv("URL"))


@app.route('/santiago-places')
def san_places():
    return render_template('places.html', title="Santiago's Profile", name="Santiago",
                           pic_url="./static/img/SantiagoPP.png",
                           about_route='san_aboutme',
                           work_route='san_work',
                           hobby_route='san_hobby',
                           education_route='san_education',
                           places_route='san_places',
                           mapper=santiago_mapper,
                           #    mapperjson=json.dumps(xavier_mapper),
                           url=os.getenv("URL"))


""" Cindy Flask Routes """
"Cindy About Me"


@app.route('/cindy-places')
def cin_places():
    return render_template('places.html', title="Cindy's Profile", name="Cindy",
                           pic_url="./static/img/CindyPP.png",
                           about_route="cin_aboutme",
                           work_route="cin_work",
                           hobby_route="cin_hobby",
                           education_route="cin_education",
                           places_route="cin_places",
                           mapper=cindy_mapper,
                           url=os.getenv("URL"))


@app.route('/cindy-work')
def cin_work():
    return render_template('work.html', title="Cindy's Profile", name="Cindy",
                           work_length="date",
                           pic_url="./static/img/CindyPP.png",
                           about_route="cin_aboutme",
                           work_route="cin_work",
                           hobby_route="cin_hobby",
                           education_route="cin_education",
                           places_route="cin_places",
                           career=cindy_career,
                           user_education=cindy_education,
                           url=os.getenv("URL"))





@app.route('/cindy-hobbies')
def cin_hobby():
    return render_template('hobbies.html', title="Cindy's Profile", name="Cindy",
                           pic_url="./static/img/CindyPP.png",
                           about_route="cin_aboutme",
                           work_route="cin_work",
                           hobby_route="cin_hobby",
                           education_route="cin_education",
                           places_route="cin_places",
                           user_hobbies=cindy_hobby,
                           url=os.getenv("URL"))


@ app.route('/cindy-aboutme')
def cin_aboutme():
    return render_template('about.html', title="Cindy's Profile", name="Cindy", contact_info=cindy_about["contact"], about_me=cindy_about["aboutme"],
                           pic_url="./static/img/CindyPP.png",
                           about_route="cin_aboutme",
                           work_route="cin_work",
                           hobby_route="cin_hobby",
                           education_route="cin_education",
                           places_route="cin_places",
                           url=os.getenv("URL"))


""" Raven Routes """
@ app.route('/raven-aboutme')
def rav_aboutme():
    return render_template('about.html', title="Raven's Profile", name="Raven", contact_info=raven_about["contact"], about_me=raven_about["aboutme"],
                           pic_url="./static/img/RavenPP.png",
                           about_route="rav_aboutme",
                           work_route='rav_work',
                           hobby_route='rav_hobby',
                           education_route='rav_education',
                           places_route='rav_places',
                           url=os.getenv("URL"))


@ app.route('/raven-work')
def rav_work():
    return render_template('work.html', title="Raven's Profile", name="Raven",
                           work_length="Jan 30/2023 - April 30/2023",
                           pic_url="./static/img/RavenPP.png",
                           about_route="rav_aboutme",
                           work_route='rav_work',
                           hobby_route='rav_hobby',
                           education_route='rav_education',
                           places_route='rav_places',
                           user_education=raven_education,
                           career=raven_career,  # Uses raven_career dict to fill out details,
                           url=os.getenv("URL"))

@ app.route('/raven-hobbies')
def rav_hobby():
    return render_template('hobbies.html', title="Raven's Profile", name="Raven",
                           pic_url="./static/img/RavenPP.png",
                           about_route="rav_aboutme",
                           work_route='rav_work',
                           hobby_route='rav_hobby',
                           education_route='rav_education',
                           places_route='rav_places',
                           user_hobbies=raven_hobby,
                           url=os.getenv("URL"))


@ app.route('/raven-places')
def rav_places():
    return render_template('places.html', title="Raven's Profile", name="Raven",
                           pic_url="./static/img/RavenPP.png",
                           about_route='rav_aboutme',
                           work_route='rav_work',
                           hobby_route='rav_hobby',
                           education_route='rav_education',
                           places_route='rav_places',
                           mapper=raven_mapper,
                           #    mapperjson=json.dumps(raven_mapper),
                           url=os.getenv("URL"))

@ app.route('/timeline')
def timeline():
    response = requests.get('http://127.0.0.1:5000/api/timeline_post')
    data = response.json()
    print(response)

    return render_template("timeline.html", title="Timeline",
    data = data,
    data_lenght = len(data['timeline_posts'])
    )


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    if not {'name'}.issubset(request.form.keys()):
        return render_template_string("<html><body><h1>Invalid name</h1></body></html>"), 400
    
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']

    if not content:
        return render_template_string("<html><body><h1>Invalid content</h1></body></html>"), 400
    
    if not '@' in email:
        return render_template_string("<html><body><h1>Invalid Email</h1></body></html>"), 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)







@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
        return {
            'timeline_posts': [
                model_to_dict(p)
                for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
            ]
        }

@app.route('/api/timeline_post', methods=['DELETE'])
def delete_last_time_line_post():
    last_post = TimelinePost.select().order_by(TimelinePost.created_at.desc()).first()
    if last_post:
        last_post.delete_instance()
        return {'message': 'Post deleted successfully'}
    else:
        return {'error': 'No posts found'}