import flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return f"Привет Мир!"

@app.route('/about/')
def about():
    return f"about"

@app.route('/contact/')
def contact():
    return f"contact"

@app.route('/<int:num_a>/<int:num_b>')
def sum_int(num_a,num_b):
    return f'{num_a} + {num_b} = {num_b+num_a}'


@app.route('/len_name/<name>/')
def len_name(name):
    return f'{len(name)}'

html = """
<h1>Привет, меня зовут Кирилл</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""

@app.route('/hello/')
def hello_html():
    return html

students = [
    {"firstname": "Иван","lastname": "Иванов",'age': 20, 'rate': 4.5},
    {"firstname": "Иван","lastname": "Иванов",'age': 20, 'rate': 4.5},
    {"firstname": "Иван","lastname": "Иванов",'age': 20, 'rate': 4.5},
    {"firstname": "Иван","lastname": "Иванов",'age': 20, 'rate': 4.5}
]

@app.route('/student/')
def get_studets():
    return render_template("students.html", students= students)

class News:
    def __init__(self,title, description, date):
        self.title = title
        self.description = description
        self.date = date

@app.route('/news/')
def news():
    news = [News('Какая-то новость', 'Описание', '2023-09-21'),News('Какая-то новость', 'Описание', '2023-09-21'),News('Какая-то новость', 'Описание', '2023-09-21')]
    return render_template("news.html", news= news)

@app.route('/main/')
def main_m():
    return render_template("main1.html")

@app.route('/main/about')
def about_m():
    return render_template("about.html")

@app.route('/main/contact')
def contact_m():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
