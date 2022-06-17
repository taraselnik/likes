from flask import Flask
import check
import module_likes

d = ["Bob", "Ivan", "Kate", "Andy", "megan", 'KLFKGJFKGfjgfngjn']
user_likes = {
    "error": None,
    "data": None,
    "error_message": None
}

if check.global_check(d) is None:
    user_likes["error"] = False
    user_likes["data"] = module_likes.out_func(d)
else:
    user_likes["error"] = True
    user_likes["error_message"] = check.global_check(d)[1]

app = Flask(__name__)


@app.route("/likes")
def likes():
    return user_likes


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run(debug=True, port=8000)
