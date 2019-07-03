from flask import Flask, render_template, url_for, request, session, redirect, jsonify
import pymongo as pm

app = Flask(__name__)
@app.route('/')
def api1():
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
        d.append(record["Movie_name"]) 
    return render_template("index.html",data=d)
    
if __name__=='__main__':
    app.run()
