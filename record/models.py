# import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username


class Alerts(db.Model):
    """check for"""

    asin = db.Column(db.String(20), unique=True, primary_key=True)
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return "<User %r>" % self.email


class Price_History(db.Model):
    """Track historical data"""

    asin = db.Column(db.String(20), unique=True, primary_key=True)
    title = db.Column(db.String(120))
    date = db.Column(db.Date)
    amount = db.Column(db.Numeric)
    currency = db.Column(db.String(5))


class User(db.Model):
    """For logging in"""

    email = db.Column(db.String(120), unique=True, primary_key=True)
    password = db.Column(db.String(30))
    # add list of asins user wants to track

    def __repr__(self):
        return "<User %r>" % self.email


def list_of_asins(sql_db):
    """with db open, extract list of asins from Alerts, return list"""
    Alerts.query.asins()


# conn = psycopg2.connect(host="localhost", database="mydb", user="zaki", password="password123")

# def test(conn):
#     cur = conn.cursor()
#     cur.execute("""
#     SELECT *
#     FROM webscrape.users
#     """)
#     rows = cur.fetchall()
#     print(rows)
#   B07SVVP426
#   B00OLZXQTM
#


if __name__ == "__main__":
    db.create_all()
    # william = User(email="sqlalchemy_test2", password="password123")
    # db.session.add(william)
    # db.session.commit()
    # users = User.query.all()
    # print(User.query.all())
    # for user in users:
    #     print(user.email, user.password)
    # item1 = Alerts(asin="B07SVVP426", email="sqlalchemy_test")
    # item2 = Alerts(asin="B00OLZXQTM", email="sqlalchemy_test2")

    # db.session.add(item2)
    # db.session.commit()
    lw = Alerts.query.all()
    x = Alerts.asin.all()
    print(x)
    for i in lw:
        print(i.asin)
    pass
