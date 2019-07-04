# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import pymongo as pm

app = Flask(__name__)
@app.route('/api1')                                       #api for getting movie name
def api1():
    try: 
        conn = pm.MongoClient()                          #connecting to mongodb
        print("Connected successfully!!!") 
    except:   
        print("Could not connect to MongoDB") 
      
    # database 
    db = conn.database
    collection = db.IMDB_Collection
    cursor = collection.find()
    d=[]
    for record in cursor: 
        d.append(record["Movie_name"]) 
    #print(d)
    return render_template("index.html",data=d)                   #render data

@app.route('/api2')                                                #api for getting movie detail through index
def api2():
    try: 
        conn = pm.MongoClient() 
        print("Connected successfully!!!") 
    except:   
        print("Could not connect to MongoDB") 
      
    # database 
    db = conn.database
    collection = db.IMDB_Collection
    cursor = collection.find()
    d=[]
    for record in cursor: 
        d.append(record["Index"]) 
    return render_template("index2.html",data=d)                               #another page for api2

@app.route("/movies",methods=["POST","GET"])                                       #this is action for api2
def movies():
    if request.method=="POST":
        name_id=request.form['idx']
    try: 
        conn = pm.MongoClient() 
        print("Connected successfully!!!") 
    except:   
        print("Could not connect to MongoDB") 
      
    # database 
    db = conn.database
    collection = db.IMDB_Collection
    #print(name_id,"check")
    cursor = collection.find({"Index":int(name_id)})
    movie_string=""
    for i in cursor:
        movie_string=movie_string+str(i["Index"])+"."+"NAME:-"+" "+i["Movie_name"]+" "+str(i["Year"])+" || "+"Cast :"+",".join(i["Star_Cast"])+" || "+"RATINGS:-"+" "+str(i["Ratings"])
    return movie_string                                                    #returnng string that contains desirable information

@app.route("/movie",methods=["POST","GET"])                                   #action for api1
def movie():
    if request.method=="POST":
        moviename=request.form['movie_name']
    try: 
        conn = pm.MongoClient() 
        print("Connected successfully!!!") 
    except:   
        print("Could not connect to MongoDB") 
      
    # database 
    db = conn.database
    collection = db.IMDB_Collection
    #print(moviename,"check")
    cursor = collection.find({"Movie_name":moviename})
    movies_str=""
    for j in cursor:
        movies_str=movies_str+str(j["Index"])+"."+"NAME:-"+" "+j["Movie_name"]+" "+str(j["Year"])+" || "+"Cast :"+",".join(j["Star_Cast"])+" || "+"RATINGS:-"+" "+str(j["Ratings"])
    return movies_str                                                     #returning string that contains desirable information
    
                
if __name__=='__main__':
    app.run()
    
