from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///do.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<Todo %r>' % self.id


@app.route("/")
def home():
    todos = Todo.query.all()

    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    description = request.form.get('description')
    new_todo = Todo(description=description)

    db.session.add(new_todo)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
