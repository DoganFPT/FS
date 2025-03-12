from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Users/49179/Desktop/mypyprojects/fullstack/Steph.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Steph(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, unique=True, nullable=False)
    threes = db.Column(db.Integer, unique=True, nullable=False)
    twos = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"<Stats {self.points}>"


with app.app_context():
    db.create_all()

@app.route("/")
def index():
    stats= Steph.query.all()
    return render_template("index.html",stats=stats)

@app.route("/stats", methods=["GET", "POST"])
def add_stats():
    if request.method=="POST":
        points=request.form["points"]
        threes=request.form["threes"]
        twos= request.form["twos"]

        new_stat=Steph(points=points,threes=threes,twos=twos)
        db.session.add(new_stat)
        db.session.commit()

        return redirect(url_for("index"))
    
    stats=Steph.query.all()
    return render_template("stats.html",stats=stats)

@app.route("/delete/<int:id>")
def delete_stat(id):
    stat_to_delete = Steph.query.get(id)
    try:
        db.session.delete(stat_to_delete)
        db.session.commit
        return redirect("/")
    except:
        return "NOT ABLE TO DELETE"


if __name__ == "__main__":
    app.run(debug=True)
