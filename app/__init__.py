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

app = Flask(__name__)

mydb.connect()
mydb.create_tables([TimelinePost])
if not os.getenv("TESTING") == "true": mydb.close()

if os.getenv("DEPLOYED", False) == "true":
    @app.before_request
    def _db_connect():
        mydb.connect()

    @app.teardown_request
    def _db_close(exc):
        if not mydb.is_closed():
            mydb.close()

if __name__ == "__main__":
    app.run(debug=False)

@app.route('/')
def index():
    return render_template('index.html', title="Main Page", projects= projects, url=os.getenv("URL"))

""" Flask Routes """
 
@app.route('/aboutme')
def aboutme(): 
    return render_template('about.html', title="Santiago's Profile", name="Santiago Vera Espinoza", contact_phone=santiago_about["phone"], contact_mail=santiago_about["mail"], contact_linkedin=santiago_about["linkedin"], contact_github=santiago_about["github"], about_me=santiago_about["aboutme"],
                           pic_url="./static/img/SantiagoPP.png",
                           about_route='aboutme',
                           work_route='work',
                           hobby_route='hobby',
                           education_route='education',
                           places_route='places',
                           url=os.getenv("URL"))


@app.route('/work')
def work():
    return render_template('work.html', title="Santiago's Profile", name="Santiago Vera Espinoza",
                           pic_url="./static/img/SantiagoPP.png",
                           about_route='aboutme',
                           work_route='work',
                           hobby_route='hobby',
                           education_route='education',
                           places_route='places',
                           career=santiago_career,  # Uses xavier_career dict to fill out details
                           user_education=santiago_education,
                           url=os.getenv("URL"))


@app.route('/hobbies')
def hobby():
    return render_template('hobbies.html', title="Santiago's Profile", name="Santiago Vera Espinoza",
                           pic_url="./static/img/SantiagoPP.png",
                           about_route='aboutme',
                           work_route='work',
                           hobby_route='hobby',
                           education_route='education',
                           places_route='places',
                           user_hobbies=santiago_hobby,
                           url=os.getenv("URL"))


@app.route('/places')
def places():
    return render_template('places.html', title="Santiago's Profile", name="Santiago Vera Espinoza",
                           pic_url="./static/img/SantiagoPP.png",
                           about_route='aboutme',
                           work_route='work',
                           hobby_route='hobby',
                           education_route='education',
                           places_route='places',
                           mapper=santiago_mapper,
                           #    mapperjson=json.dumps(xavier_mapper),
                           url=os.getenv("URL"))

@app.route('/project/<int:id>')
def project(id):
    return render_template('project.html',
                           title=projects["project_name"][id],
                           client=projects["project_client"][id],
                           date=projects["project_date"][id],
                           introduction=projects["project_intro"][id],
                           description=projects["project_desc"][id],
                           technical_skills=projects["technical_skills"][id],
                           soft_skills=projects["soft_skills"][id],
                           videos=projects["project_videos"][id],
                           photos=projects["project_gallery"][id],
                           url=os.getenv("URL"))

@app.route('/blog')
def blog():
    return render_template(f'blog.html',
                           title="Blog",
                           titles=blogs["blog_titles"],
                           dates=blogs["blog_dates"],
                           authors=blogs["blog_authors"],
                           read_times=blogs["blog_read_times"],
                           images=blogs["image_names"],
                           links=blogs["links"],
                           url=os.getenv("URL"))

@app.route('/blog/<name>')
def blog_post(name):
    return render_template(f'./blogs/{name}.html',
                           image_folder=f"./../../static/img/blogs/{name}/",
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

    print(f"{name} | {email} | {content}")

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