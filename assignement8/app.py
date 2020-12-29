from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('my final CV.html')


@app.route('/contact')
def contact_me():
    return render_template('Form-Contact me.html')


@app.route('/contactList')
def contact_list():
    return render_template('contact list.html.html')


@app.route('/assignement8')
def assignement8_fun():
    user_ab= {'firstName': 'Shiraz', 'lastName': 'Koretz', 'Salutation': 'Ms.', 'gender': 'girl'}
    return render_template('assignment8.html', user=user_ab, hobbies=['reading books', 'dancing', 'painting', 'running'],
                      degree=('B.A', )
                           )

@app.route('/user')
def user_fun():
    User_from_my_DB= {'firstName': 'Shiraz', 'lastName': 'Koretz', 'Salutation': 'Ms.', 'gender': 'girl'}
    return render_template('user.html',  user=User_from_my_DB)


if __name__ == '__main__':
    app.run(debug=True)
