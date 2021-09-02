
#from templates.app import Article
from typing import Text
from flask import Flask, render_template, url_for, request, redirect, jsonify
from datetime import datetime
from flask_mongoengine import MongoEngine
import json
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)

client = MongoClient("mongodb://internal-138043858.us-east-1.elb.amazonaws.com:27017")    
db = client.posts      
post_list = db.post_list

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/create-article', methods=['POST', 'GET'])
def save():
    if request.method == "POST":
        title=request.values.get("title")    
        intro=request.values.get("intro")    
        text=request.values.get("text")
        dt_n=datetime.now()
        try:
            post_list.insert({ "title":title, "intro":intro, "text":text, "last_mod":dt_n})    
            return redirect ('/posts')
        except:
            return "error"
    else:
        return render_template("create-article.html")

@app.route('/posts')
def posts():
    post_l=post_list.find()
    return render_template("posts.html", post_l=post_l)


@app.route('/posts/<id>')
def post_detail(id):
    post_d = post_list.find_one({"_id" : ObjectId(id)})
    return render_template("post_detail.html", post_d=post_d)

@app.route('/posts/<id>/delete')
def post_delete(id):
    try:
        post_list.remove({"_id":ObjectId(id)})
        return redirect ('/posts')
    except:
        return "Error"

#    article = Article.query.get_or_404(id)
#    try:
#        db.session.delete(article)
#        db.session.commit()
#        return redirect ('/posts')



@app.route('/posts/<id>/update', methods=['POST', 'GET'])
def post_update(id):
#        post_u = post_list.find_one({"_id" : ObjectId(id)})
    if request.method == "POST":
        title=request.values.get("title")    
        intro=request.values.get("intro")    
        text=request.values.get("text")
        try:
            post_list.update({"_id":ObjectId(id)}, {'$set':{ "title":title, "intro":intro, "text":text }})
            return redirect ('/posts')
        except:
            return "error"
    else:    
        post_l=post_list.find_one({"_id" : ObjectId(id)}) 
        return render_template("post_update.html", post_l=post_l)   
##        article = Article(title=title, intro=intro, text=text)

#       try:
#            db.session.commit()
#           
#            
#    else:
#        article = Article.query.get(id)
#        return render_template("post_update.html", article=article)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
