from flask import Flask, render_template

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Кирилл</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>
"""


@app.route('/')
@app.route('/<name>/')
def hello(name="незнакомец"):
    return f"Привет, {name.capitalize()}!"


@app.route('/index/')
def html_index():
    return render_template('index.html')


@app.route('/index/1')
def html_index1():
    context = {
        'title': 'Личный блог',
        'name': 'Смирнов',
    }
    return render_template('index2.html', **context)


@app.route('/if/')
def show_if():
    context = {
        'title': 'Ветвление',
        'user': 'Крутой хакер!',
        'number': 1,
    }
    return render_template('show_if.html', **context)


@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f"Путь до файла '{file}'"


@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


@app.route('/text/')
def text():
    return html


@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал,',
            'Программистом взял и стал.',
            'Хитрый знает он язык,',
            'Он к другому не привык.'
            ]
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    return txt


@app.route('/for/')
def show_for():
    comtext = {'title': 'Цикл',
               'poem': ['Вот не думал, не гадал,',
                        'Программистом взял и стал.',
                        'Хитрый знает он язык,',
                        'Он к другому не привык.'
                        ]}
    return render_template('show_for.html', **comtext)


@app.route('/users/')
def users():
    _users = [{'name': 'Никанор',
               'mail': 'nik@mail.ru',
               'phone': '+7-987-654-32-10',
               },
              {'name': 'Феофан',
               'mail': 'feo@mail.ru',
               'phone': '+7-987-444-33-22',
               },
              {'name': 'Оверран',
               'mail': 'forest@mail.ru',
               'phone': '+7-903-333-33-33',
               }, ]
    context = {'users': _users,
               'title': 'Точечная нотация'}
    return render_template('user.html', **context)


if __name__ == "__main__":
    app.run(debug=True)
