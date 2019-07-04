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
