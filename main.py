from flask import Flask, render_template, request

# from flask import url_for
# from track_item import begin_tracking


def main(user_url: str):
    """Program starts here"""
    # valid url?
    #     if so, parse
    #     else, throw error
    # amazon or ebay url?
    #     if not amazon/ebay, throw Error
    #     else begin amazon or ebay function
    pass


app = Flask(__name__)


@app.route("/hello")
def hello():
    return "<h1> Hello world!1</h1>"


@app.route("/", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        print(name, email)
        return (name, email)


if __name__ == "__main__":
    # args = parse_args()
    # main(args)
    print("/// MAIN ///")
    # main()
    app.run(host="127.0.0.1", port=8080, debug=True)
    # pass
