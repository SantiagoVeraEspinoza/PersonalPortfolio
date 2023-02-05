from dotenv import load_dotenv
from flask import Flask, render_template, request
import os


load_dotenv()
app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)


@app.route('/')
def index():
    return render_template('index.html', title="Vitrina", project_1="Team Portfolio Site", github_link="https://github.com/MLH-Fellowship/project-vitrina", languages="Flask, JS, AWS",
                           date_1="Jan 26/2023 - Feb 06/2023", url=os.getenv("URL"))


""" Route names post-fix """
# -aboutme
# -work
# -education
# -hobbies
# -places

""" Section fillouts """
xavier_about = {
    "contact": "xavierjmoreno401@gmail.com",
    "aboutme": "I'm a Computer Engineering student who's very passionate about Robotics and AI both in a personal and professional avenue. As a result I'm starting to look deeper into topics like Machine Learning, Autonomous Vehicles and Humanoid Robotics. Currently I'm starting to focus on growing my skills in C++, Python, Operating Systems and Data Structures and Algorithms. I have a background in IT, which led to me gaining interest in Cloud Computing as well. On my personal interests, I absolutely love hackathons, they are great way to meet others and to explore new topics and push boundaries. As a result of them, I've started to become interested in joining both Kaggle Competitions and Robotics Tournaments."
}

xavier_career = {
    "jobcount": 4,
    "companies": ["MLH Fellowship", "Southwest Airlines", "Fujitsu",  "Self-Employed"],
    "jobtitle": ["Site Reliability Engineer Fellow",  "Noc Analyst", "Service Desk Analyst",  "Private Tutor"],
    "dates": ["Jan 2023 - April 2023", "Nov 2022 - Present", "March 2021 - Nov 2021", "Nov 2019 - Present"],
    "descriptions": {
        0: ["Worked in a cohort of 20 other members"],
        1: ["Performed continuous monitoring & incident response of various systems through Grafana, escalating tickets when required using ServiceNow. Coordinated with various teams from departments on incidents",
            "Continuously updated & monitored 250 RHEL 7 machines and 500 Windows 10 machines",
            "Performed hardware and software upgrades for machines running AVTEC software"],
        2: ["Citrix-Systems used to virtualize workstation PC with tools such as Wireshark, Teamviewer & AWS voice",
            "Collaborated in a team addressing 10-20 tickets daily & advising up to 20 clients daily",
            "SOTI mobicontrol & TeamViewer - Remoted into Windows PCs dealing with malware cleanup, software installation, password-resets, network-connectivity. Used ServiceNow for ticketing",
            "Handled Zebra device issues, involving incorrect network configurations with IP or staging",
            "Working with networking hardware ( Cisco Switches & Routers ) to address issues with DHCP / DNS / IP"],
        3: ["Tutored Undergraduate students in 1-on-1 sessions, using personally tailored study plans for Math and CS",
            "For Math taught Calculus I-II, for CS taught various languages, with a focus on Java & JavaScript",
            "Studied and debugged thousands of lines of code and gave students feedback on their work"],
    }
}

santiago_about = {
    "contact": "santiveraespinoza@gmail.com",
    "aboutme": "I am a future engineer in computer technologies currently studying at Tecnológico de Monterrey (ITESM, 2021 - 2025). I have been programming since 16, self-taught. My main language is C++, I can also program in Python, Matlab, R and HTML. Made some videogames on my own, as well as some physics simulators. I also have good knowledge in Office and Adobe apps."
}

santiago_career = {
    "jobcount": 1,
    "companies": ["MLH Fellowship"],
    "jobtitle": ["Site Reliability Engineer Fellow"],
    "dates": ["Jan 2023 - April 2023"],
    "descriptions": {
        0: ["Worked in a cohort of 20 other members"],
    }
}

""" Cindy Routes """

cindy_about = {
    "contact": "cindyliang0127@gmail.com",
    "aboutme": "I am currently a junior studying Computer Science at NYU. I am passionate about full stack software development and in my free time, I like to immerse myself with Natural Langauge Processing and UX/UI design. I am currently honing my coding skills for C and would like to pick up more languages in the future so I can keeping learning and improving."
}

cindy_career = {
    "jobcount": 4,
    "companies": ["MLH Fellowship", "Self-Employed", "ReachNBeyond", "Naomedical"],
    "jobtitle": ["Site Reliability Engineer Fellow", "Private Math Tutor", "Computer Science Teacher", "UX/UI Intern"],
    "dates": ["Jan 2023 - April 2023", "January 2023 - Present", "June 2022 - Present", "June 2021 - August 2021"],
    "descriptions": {
        0: ["Worked in a cohort of 20 other members"],
        1: ["Tutored K-12 students in 1-on-1 sessions with custom made study designs"],
        2: ["Taught over 50 students Computer Science (Javascript) and Math"],
        3: ["Designed app features to improve urgent health care user’s experience by making it more efficient and accessible. Experience working with tech stacks and startup operation"],
    }
}





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
                           url=os.getenv("URL"))

@app.route('/santiago-education')
def san_education():
    return render_template('education.html', title="Santiago's Profile", name="Santiago",
                           pic_url="./static/img/SantiagoPP.png",
                           about_route='san_aboutme',
                           work_route='san_work',
                           hobby_route='san_hobby',
                           education_route='san_education',
                           places_route='san_places',
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
                           url=os.getenv("URL"))


""" Cindy Flask Routes """
"Cindy About Me"


@app.route('/cindy-places')
def cindy_places():
    return render_template('places.html', title="Cindy's Profile", name="Cindy",
                           pic_url="./static/img/CindyPP.png",
                           about_route="cindy_aboutme",
                           work_route="cindy_work",
                           hobby_route="cindy_hobby",
                           education_route="cindy_education",
                           places_route="cindy_places",
                           url=os.getenv("URL"))

@app.route('/cindy-work')
def cindy_work():
    return render_template('work.html',title="Cindy's Profile", name="Cindy",
                            work_length = "date",
                           pic_url="./static/img/CindyPP.png",
                           about_route="cindy_aboutme",
                           work_route="cindy_work",
                           hobby_route="cindy_hobby",
                           education_route="cindy_education",
                           places_route="cindy_places",
                           career= cindy_career,
                           url=os.getenv("URL"))


@app.route('/cindy-education')
def cindy_education():
    return render_template('education.html', title="Cindy's Profile", name="Cindy",
                           pic_url="./static/img/CindyPP.png",
                           about_route="cindy_aboutme",
                           work_route="cindy_work",
                           hobby_route="cindy_hobby",
                           education_route="cindy_education",
                           places_route="cindy_places",
                           url=os.getenv("URL"))

@app.route('/cindy-hobbies')
def cindy_hobby():
    return render_template('hobbies.html', title="Cindy's Profile", name="Cindy",
                           pic_url="./static/img/CindyPP.png",
                           about_route="cindy_aboutme",
                           work_route="cindy_work",
                           hobby_route="cindy_hobby",
                           education_route="cindy_education",
                           places_route="cindy_places",
                           url=os.getenv("URL"))


@ app.route('/cindy-aboutme')
def cindy_aboutme():
    return render_template('about.html', title="Cindy's Profile", name="Cindy", contact_info=cindy_about["contact"], about_me=cindy_about["aboutme"],
                           pic_url="./static/img/CindyPP.png",
                           about_route="cindy_aboutme",
                           work_route="cindy_work",
                           hobby_route="cindy_hobby",
                           education_route="cindy_education",
                           places_route="cindy_places",
                           url=os.getenv("URL"))




""" Route Template """

""" 
@app.route('/YourName-education')
def xav_education():
    return render_template('type.html', title="Name's Profile", name="",
                           pic_url=".png",
                           about_route="",
                           work_route='',
                           hobby_route='',
                           education_route='',
                           places_route='',
                           url=os.getenv("URL"))


 """
