from application import app, db
from flask import render_template, request, json, Response, redirect, flash
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm

courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3",
"term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming",
"credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming",
"credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular",
"credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2",
"description":"Advanced Java Programming","credits":"4","term":"Fall"}]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', index=True)

@app.route('/courses/')
@app.route('/courses/<string:term>')
def courses(term='Spring 2020'):
    return render_template('courses.html', courseData= courseData, courses=True, term=term)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form, register=True)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    title = "Login"
    if form.validate_on_submit():
        if request.form.get("email") == "test@test.com":
            flash("You are Successfully logged in !", "success")
            return redirect ("/index")
        else:
            flash("Sorry! Something went wrong", "danger")
    return render_template('login.html', form=form, title=title, login=True)

@app.route('/enrollment', methods=["GET","POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template('enrollment.html', data={"id":id, "title":title, "term":term })

@app.route('/api')
@app.route('/api/<idx>')
def api(idx = None):
    if idx == None:
        jdata = courseData
    else:
        jdata = courseData[int(idx)]

    return Response( json.dumps(jdata), mimetype='application/json')


@app.route('/user')
def user():
    #User(user_id=1, first_name="hash", last_name='ash', email='hashash@uta.com', password='hash123').save()
    #User(user_id=2, first_name="lava", last_name='lav', email='lavalav@uta.com', password='lava321').save()

    users = User.objects.all()
    return render_template("user.html", users=users)
