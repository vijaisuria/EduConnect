from flask import Flask, request, render_template
from linkedin_api import Linkedin

app = Flask(__name__)

def get_linkedin_profile(username):
    api = Linkedin('sriradha81@gmail.com', '***')
    profile = api.get_profile(username)
    return profile

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        career_goal = request.form['careerGoal']
        manual_skills = request.form.getlist('skill[]')
        linkedin_username = request.form.get('linkedinUsername')
        profile_data = None

        if linkedin_username:
            profile_data = get_linkedin_profile(linkedin_username)
        elif manual_skills:
            profile_data = manual_skills

        return render_template('index.html', profile_data=profile_data, manual_skills=manual_skills)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
