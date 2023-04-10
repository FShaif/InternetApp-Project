from flask import Flask,render_template
app = Flask(__name__)

from json import dumps
from postdata import posts

@app.route("/post/<int:post_id")
def post(post_id):
    post = posts[post_id]   
    return render_template('post.html',title=post['title'],p=post)


@app.route("/json_posts")
def json_posts():
    return dumps(posts)
