from flask import Flask,render_template
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


@app.route("/post-single")
def postSingle():
    return render_template('post-single.html',
                           title='single posts',
                           posts=posts)

@app.route("/reqres-data")
def reqresData():
    return render_template('reqres-data.html')

@app.route("/post-all")
def home():
    return render_template('post-all.html',
                           title='all posts',
                           posts=posts)

# Trying to get favicon working on layout instead of html page
#import os
#from flask import send_from_directory
#@app.route("/static/favicon.ico") 
#def fav():
#    print(os.path.join(app.root_path, 'static'))
#    return send_from_directory(app.static_folder, 'favicon.ico')

if __name__ == '__main__':
	app.run( debug=True )


from json import dumps,loads

# @app.route("/post/<int:post_id")
# def post(post_id):
#     post = posts[post_id]   
#     return render_template('post-single.html',title=post['title'],p=post)

@app.route("/json_posts")
def json_posts():
    data = {
        'data': posts,
        'total': len(posts)
    }
    return dumps(data)



