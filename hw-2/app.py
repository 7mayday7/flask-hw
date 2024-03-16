from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome', methods=['POST'])
def welcome():
    # Получаем данные из формы
    name = request.form['name']
    email = request.form['email']

    # Создаем куки с данными пользователя
    response = make_response(render_template('welcome.html', name=name))
    response.set_cookie('username', name)
    response.set_cookie('email', email)
    return response


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('username', expires=0)
    response.set_cookie('email', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
