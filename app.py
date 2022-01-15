from dataclasses import asdict

from flask import Flask, request

from main import item_confirmation

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


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        data = request.json
        url = data
        response = item_confirmation(url)
        print(response)
    return asdict(response)


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        print("get request to /test")
        return "/test response from flask"


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


app.run(host="127.0.0.1", port=5000, debug=False)

# if __name__ == "__main__":
#     # args = parse_args()
#     # main(args)
#     print("/// MAIN ///")
#     # main()
#     app.run(host="127.0.0.1", port=5000, debug=False)
#     # pass
