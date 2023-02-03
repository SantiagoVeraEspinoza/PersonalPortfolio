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
