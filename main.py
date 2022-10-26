from flask import Flask, render_template
from post import Post, AllPosts

all_posts = AllPosts()
post = Post()

app = Flask(__name__)


@app.route('/')
def home():
    print(all_posts.result)
    return render_template("index.html", blog_posts=all_posts.result)


@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    for p in all_posts.result:
        if p['id'] == blog_id:
            post.id_ = p['id']
            post.title_ = p['title']
            post.subtitle_ = p['subtitle']
            post.body_ = p['body']
            post.author_ = p['author']
            post.date_ = p['dateCreation']

    return render_template("post.html", blog=post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
