from flask import Blueprint, render_template, request, redirect
import json, random
from . import globalconstants
from urllib.request import urlopen

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        pass
    return render_template("index.html")

@views.route('/game', methods=['GET', 'POST'])
def game():
    already_asked = list()
    score = 0

    if request.method == 'POST':
        print(request.form)
        already_asked = json.loads(request.form.getlist("already_asked")[0])
        score = int(request.form["score"])
        if score == -1:
            return redirect("/game")
        print(already_asked)

    q_f = urlopen("https://storage.cloud.google.com/nikalodean.appspot.com/qa.json")
    m_f = urlopen("https://storage.cloud.google.com/nikalodean.appspot.com/mm.json")
    q_data = json.loads(q_f.read())
    m_data = json.loads(m_f.read())

    all_answered = False
    for i in range(10):
        if len(q_data) == 0:
            all_answered = True
            break
        data = random.choice(q_data)
        data["score"] = score
        if data["id"] in already_asked:
            q_data = list(filter(lambda i: i['id'] != data["id"], q_data))
        else:
            already_asked.append(data["id"])
            break
    
    if all_answered == True:
        data = {
            "ques": "Congratulations! You have answered all the questions correctly. Waittttt that means you are stupid as fuck... :p",
            "options": False,
            "score": score
        }
    else:
        data["already_asked"] = already_asked
        for option in data["options"]:
            if isinstance(data["options"][option], str):
                data["msgs"] = (m_data[data["options"][option]])
    print(data)

    return render_template("game.html", data=data)
