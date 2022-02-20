from dataclasses import asdict

from flask import Flask, request, session
from werkzeug.security import check_password_hash, generate_password_hash

from database.create import init_connection
from database.data_classes import User
from database.methods import add_user, return_user
from main import item_confirmation

# from flask_cors import CORS
# from flask import url_for
# from track_item import begin_tracking


app = Flask(__name__)
app.secret_key = "rj5sztFrGIG4DTVm_lnx0w"
# CORS(app)

conn = init_connection()


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        data = request.json
        url = data
        response = item_confirmation(url)
        print(response)
    return asdict(response)


@app.route("/", methods=["GET", "POST"])
def a():
    """Main entry point

    For post requests, select path with json"""

    if request.method == "GET":
        # return render_template("form.html")
        return "get request to root/"

    if request.method == "POST":
        print("post method received")

        # JSON stored in data variable
        data = request.json
        print(data)
        print(data["name"])
        if data["form"] == "one":
            print("form one")

        if data["form"] == "two":
            print("form two")
        if request.method == "POST" and "pid" in request.form:
            pass
        # # exit early
        # if data is invalid:
        #     return "response: incorrect url, send a valid amazon url"

        # # continue on
        # scrape_item():
        #     return image, title, price
        # # sending response, for confirmation
        # if no:
        #     exit early
        # else:
        #   begin_tracking()

        # dump post data to text file
        with open("output/frontend_inputs.txt", "a") as fp:
            fp.write(f"\n{data}")
        return {"response": "/ response from flask"}


@app.route("/register", methods=["GET", "POST"])
def register():
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    print(request.json)
    data = request.json
    email = data["email"]
    password = data["password"]

    if request.method == "POST" and email and password:
        # Create variables for easy access
        _hashed_password = generate_password_hash(password)
        print(email)
        # check if email exists
        account = return_user(conn, email)
        if account:
            print("user exists: ", email)
            return {"response": "Account with this email already exists!"}
        else:
            print("no user: ", email)
            add_user(conn, User(email=email, password=_hashed_password))
            return {"response": "Valid registration! Account created"}
    elif request.method == "POST":
        # empty email/password
        print("No Email and password! Compelete the Form")
        return {"response": "Empty email and/or password field"}
    return {"response": "/register response from flask"}


@app.route("/login", methods=["GET", "POST"])
def login():
    print(request.json)
    data = request.json
    email = data["email"]
    password = data["password"]

    if request.method == "POST" and email and password:
        account = return_user(conn, email)
        if account:
            (u_id, u_email, u_password) = account
            print("user exists")
            print(u_password)
            hashed_password = u_password
            print("hashed_password", hashed_password)
            if check_password_hash(hashed_password, password):
                session["loggedin"] = True
                session["id"] = u_id
                session["email"] = u_email
                return {"response": "Correct User and password, logged in!"}
            else:
                return {"response": "Incorrect password!"}
        else:
            return {"response": "user does not exist"}

        # check if email exists
        # if yes, check hashed password
        # if no, return error - incorrect email
        # check if password matches
        # if no, return error - incorrect password
        # if yes, create session


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "loggedin" in session:
        print(session["id"])
        cur = conn.cursor()
        cur.execute("SELECT * FROM webscrape.users WHERE id = %s", [session["id"]])
        account = cur.fetchone()
        (u_id, u_email, u_password) = account
        print(u_id, u_email)
        return {"response": "session"}
    else:
        return {"response": "no session"}


app.run(host="127.0.0.1", port=5000, debug=False)

# if __name__ == "__main__":
#     # args = parse_args()
#     # main(args)
#     print("/// MAIN ///")
#     # main()
#     app.run(host="127.0.0.1", port=5000, debug=False)
#     # pass
