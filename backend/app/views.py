from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        pass
    return render_template("index.html")