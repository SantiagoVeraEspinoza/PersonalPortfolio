import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/')
def index():
    return render_template('index.html', title="Vitrina", project_1="Team Portfolio Site", github_link= "https://github.com/MLH-Fellowship/project-vitrina",languages="Flask, JS, AWS",
                           date_1="Jan 26/2023 - Feb 06/2023", url=os.getenv("URL"))


""" Xavier Flask Routes """

@app.route('/xavier-work')
def workexp():
    return render_template('work.html', title="Xavier's Profile",name="Xavier",company_name="MLH Fellowship", role="Site Reliability Engineer Fellow",
                           work_length="Jan 30/2023 - April 30/2023", url=os.getenv("URL"))


"Cindy About Me"
@app.route('/cindy-aboutme')
def aboutme():
    return render_template('about.html', title="Cindy's Profile",name ="Cindy",contact_info="cindyliang0127@gmail.com", about_me="Hello! My name is Cindy Liang and I am currently a junior studying at NYU [insert more information] If you're looking for random paragraphs, you've come to the right place. When a random word or a random sentence isn't quite enough, the next logical step is to find a random paragraph. We created the Random Paragraph Generator with you in mind. The process is quite simple. Choose the number of random paragraphs you'd like to see and click the button. Your chosen number of paragraphs will instantly appear.",pic_url="./static/img/CindyPP.png",url=os.getenv("URL"))


