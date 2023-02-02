import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/')
def index():
    return render_template('index.html', title="Vitrina", project_1="Team Portfolio Site", languages="Flask, JS, AWS",
                           date_1="Jan 26/2023 - Feb 06/2023", url=os.getenv("URL"))
