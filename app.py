from flask import Flask, render_template, url_for, request
from client import Client


app = Flask(__name__)


client = Client()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/room_entry',  methods=['GET', 'POST'])
def room_entry():
    if request.method == "POST":
        room_id = request.form.get("room_id")
        user_name = request.form.get("my_name")
        user_login = request.form.get("my_log")
        user_password = request.form.get("my_pass")
        user_surname = request.form.get("my_surname")

        if not (room_id.isalpha() and len(room_id) == 5):
            print("bad room id")
            msg = "Неверный ввод идентификатора"
            return render_template('index.html', error_msg=msg, user_name=user_name,
                                   user_surname=user_surname, login_ans="Welcome back",
                                   user_login=user_login, user_password=user_password)
        got_name, got_surname, got_role = client.SetRoomId(room_id, user_name, user_surname, user_login, user_password)
        if got_name != "" and got_surname != "":
            user_name = got_name
            user_surname = got_surname
        return render_template('code_mirror.html', room_id=room_id, user_name=user_name,
                               user_surname=user_surname, user_role=got_role)


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        room_id = request.form.get("room_number")
        text = request.form["editor"]
        name = request.form.get("my_name")
        surname = request.form.get("my_surname")
        role = request.form.get("my_role")
        new_role = client.Update_Role(name, surname, room_id, role)
        res = client.GetListOfUsers(room_id, text, name, surname)
        if new_role == "reader but can be writer":
            res.text = text
        return render_template('code_mirror.html', room_id=room_id, new_list_of_users=res.list_of_users,
                               text=res.text, user_name=name, user_surname=surname, user_role=new_role)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        login = request.form.get("login")
        password = request.form.get("password")
        name = request.form.get("name")
        surname = request.form.get("surname")
        code, info = client.Registration(login, password, name, surname)
        if code:
            return render_template('index.html', registration_ans=info, user_name=name, user_surname=surname,
                                   user_login=login, user_password=password)
        return render_template('index.html', registration_ans=info, user_name=name, user_surname=surname,
                               user_login=login, user_password=password)


@app.route('/login', methods=['GET', 'POST'])
def LogIn():
    if request.method == 'POST':
        login = request.form.get("login")
        password = request.form.get("password")
        code, info, name, surname = client.Login(login, password)
        if code:
            return render_template('index.html', login_ans=info, user_name=name, user_surname=surname,
                                   user_login=login, user_password=password)
        return render_template('index.html', login_ans=info, user_name=name, user_surname=surname,
                               user_login=login, user_password=password)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
