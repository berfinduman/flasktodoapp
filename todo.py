from flask import Flask, render_template, redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/berfi/OneDrive/Masaüstü/TodoApp/todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(80))
    todo=db.Column(db.Boolean)

@app.route("/complete/<string:id>")
def update(id):
    todo_1=Todo.query.filter_by(id=id).first()
    todo_1.todo= not todo_1.todo
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def delete(id):
    tod=Todo.query.filter_by(id=id).first()
    db.session.delete(tod)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/")
def index():
    todos=Todo.query.all()
    return render_template("index.html",todos=todos)
@app.route("/add",methods=["POST"])
def addtodo():
    title=request.form.get("title")
    newtodo = Todo(title= title, todo=False)
    db.session.add(newtodo)
    db.session.commit()
    
    return redirect(url_for("index"))

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)