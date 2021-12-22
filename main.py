from flask import Flask, request

# from flask_cors import CORS
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
# CORS(app)


@app.route("/hello")
def hello():
    return "<h1> Hello world!1</h1>"


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        print("get request to /test")
        return "/test response from flask"


@app.route("/", methods=["GET", "POST"])
def a():
    if request.method == "GET":
        # return render_template("form.html")
        return "get request to root/"
    if request.method == "POST":
        print("post method received")

        # JSON stored in data variable
        data = request.json
        # print(data["name"])
        print(data)
        return {"response": "/ response from flask"}


app.run(host="127.0.0.1", port=5000, debug=False)

# if __name__ == "__main__":
#     # args = parse_args()
#     # main(args)
#     print("/// MAIN ///")
#     # main()
#     app.run(host="127.0.0.1", port=5000, debug=False)
#     # pass
