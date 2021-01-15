
from flask import Flask, redirect, url_for, render_template, request, session
from flask import jsonify
from utilities.db.db_manager import DBManager


app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def home_page():
    return render_template('my final CV.html')


@app.route('/contact')
def contact_me():

    return render_template('Form-Contact me.html')


@app.route('/contactList')
def contact_list():
    return render_template('contact list.html')


@app.route('/assignment8')
def assignement8_fun():
    user_ab= {'firstName': 'Shiraz', 'lastName': 'Koretz', 'Salutation': 'Ms.', 'gender': 'girl'}
    return render_template('assignment8.html', user=user_ab, hobbies=['reading books', 'dancing', 'painting', 'running'],
                      degree=('B.A', )
                           )

#this is for assigment 8- include and extends
@app.route('/user')
def user_fun():
    User_from_my_DB= {'firstName': 'Shiraz', 'lastName': 'Koretz', 'Salutation': 'Ms.', 'gender': 'girl'}
    return render_template('user.html',  user=User_from_my_DB)

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_fun():

    userslist = [{"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
             "avatar": "https://reqres.in/img/faces/7-image.jpg"},
            {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
             "avatar": "https://reqres.in/img/faces/8-image.jpg"},
            {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
             "avatar": "https://reqres.in/img/faces/9-image.jpg"},
            {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
             "avatar": "https://reqres.in/img/faces/10-image.jpg"},
            {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
             "avatar": "https://reqres.in/img/faces/11-image.jpg"},
            {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
             "avatar": "https://reqres.in/img/faces/12-image.jpg"}]
    username =''
    searchname=''
    if request.method == 'GET':
        if 'name' in request.args:
         searchname = request.args['name']
        if searchname == '':
            return render_template('assignment9.html', userslist=userslist)
        else:
            return render_template('assignment9.html', username=searchname,  userslist=userslist, request_method=request.method)

    if request.method == 'POST':
        user = request.form['username']
        session['logged_in'] = True
        session['username'] = user
        return render_template('assignment9.html')

    return render_template('assignment9.html')

from Pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


@app.route('/logout', methods=['GET' , 'POST'])
def logout_fun():
    session['logged_in'] = False
    session['username'] = ' '
    return render_template('assignment9.html')



@app.route('/assignment11/users')
def get_users():
    if request.method == "GET":
        query = "select * from users"
        db_manager = DBManager()
        query_result = db_manager.fetch(query=query)
        if len(query_result) == 0:
            return jsonify ({
                'success': 'False',
                'data': []
            })
        else:
            data=[]
            for user in query_result:
                data.append({
                  'id:': user.id,
                  'first name:': user.first_name,
                  'last name:': user.last_name,
                  'email:': user.email,
                  'success': 'True'
                })
            return jsonify(data)
@app.route('/assignment11/users/selected/' ,defaults={'SOME_USER_ID':14})
@app.route('/assignment11/users/selected/<int:SOME_USER_ID>')
def get_my_users(SOME_USER_ID):
    if request.method == "GET":
        query = "select * from users WHERE id='%s'" % (SOME_USER_ID)
        db_manager = DBManager()
        query_result = db_manager.fetch(query=query)
        if len(query_result) == 0:
            return jsonify ({
                'success': 'False',
                'data': []
            })
        else:
            user= query_result[0]
            return jsonify({
                'id:': user.id,
                'first name:': user.first_name,
                'last name:': user.last_name,
                'email:': user.email,
                'success': 'True'
            })





if __name__ == '__main__':
    app.run(debug=True)
