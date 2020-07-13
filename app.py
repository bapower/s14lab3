from flask import Flask, render_template, request, redirect, url_for
from models.user import Db, User
from modules.userform import UserForm
from mimesis import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "s14a-key"
Db.init_app(app)


@app.route('/')
def index():
    users = User.query.all()
    for user in users:
        User.toString(user)
    return render_template("index.html", users = users)

# @route /adduser - GET, POST
@app.route('/adduser', methods=['GET', 'POST'])
def addUser():
    form = UserForm()
    # If GET
    if request.method == 'GET':
        return render_template('adduser.html', form=form)
    # If POST
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            age = request.form['age']
            new_user = User(first_name=first_name, age=age)
            Db.session.add(new_user)
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('adduser.html', form=form)

# @route /adduser/<first_name>/<age>
@app.route('/adduser/<first_name>/<age>')
def addUserFromUrl(first_name, age):
    Db.session.add(User(first_name=first_name, age=age))
    Db.session.commit()
    return redirect(url_for('index'))

@app.route('/user/<id>')
def getUser(id):
    user = User.query.get(id)
    User.toString(user)

    return render_template("user.html", user = user)

@app.route('/user/delete/<id>')
def deleteUser(id):
    user = User.query.get(id)
    Db.session.delete(user)
    Db.session.commit()

    return redirect(url_for('index'))

@app.route('/user/edit/<id>', methods=['GET', 'POST'])
def editUser(id):
    user = User.query.get(id)
    if user:
        form = UserForm(formdata=request.form, obj=user)
        if request.method == 'POST':
            user.first_name = request.form['first_name']
            user.age = request.form['age']
            Db.session.commit()
            return redirect('/')
        return render_template('edituser.html', form=form, id=id)
    else:
        return 'Error loading #{id}'.format(id=id)

@app.route('/seed/<rows>')
def seedDatabase(rows):
    person = Person('en')
    for _ in range(0, int(rows)):
        first_name = person.first_name()
        age = person.age()
        new_user = User(first_name=first_name, age=age)
        Db.session.add(new_user)
        Db.session.commit()
    return redirect(url_for('index'))
