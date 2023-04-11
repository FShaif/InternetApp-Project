from flask import Flask,render_template
from json import dumps
from postdata import posts

app = Flask(__name__)

@app.route("/")
def homePagex():
   return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')
        
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/mobiles")
def mobiles():
    return render_template('mobiles.html')

@app.route("/post-all")
def postAll():
    return render_template('post-all.html')

@app.route("/post-single")
def postSingle():
    return render_template('post-single.html')

@app.route("/reqres-data")
def reqresData():
    return render_template('reqres-data.html')

if __name__ == '__main__':
	app.run( debug=True )





""" Temporarily Commented to test code 
@app.route("/post/<int:post_id")
def post(post_id):
    post = posts[post_id]   
    return render_template('post-single.html',title=post['title'],p=post) # Changed this line and forgot what the old line was
"""


@app.route("/json_posts")
def json_posts():
    return dumps(posts)

