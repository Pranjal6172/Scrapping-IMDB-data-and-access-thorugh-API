# Scrapping-IMDB-data-and-access-through-API

In this repository scrapping on IMDb website is done to get 1250 movies data.<br>
After scrapping,data is stored in both json file as well MongoDB database.<br>
Data is accessed from MongoDB database using flask with API.

## IMDB Scrapping.py

These file contains Scrapping code that is done on IMDb website as well MongoDB code for connecting to MongoClient and insertion into database.<br><br>
<b>BeautifulSoup is used for scrapping on IMDb and Pymongo is used for MongoDb.</b><br><br>
Dictionary is created for storing all the information for individual movie.<br>
List of all the dictionary is created to store data into json and database.<br>
For storing into MongoDb database, first connect to MongoClient then insert each dictionary that is persent in list into database one by one.

## FlaskAPI.py

These file conatins api code that is used for both access data from MongoDB as well for creating backend for website.<br><br>
<b>flask for backend and Pymongo is used for MongoDb.</b><br><br>
 In these two api is created :-<br>
 - api1 for getting request through movie name.
 - api2 for getting request through index number.
 - movies redirect to api1.
 - movies redirect to api2.
 
 ## index.html
 
 This contains the code for api1.<br>
 whenever user will enter any text it will show all the movie names that will contain the prefix as entered text.<br>
 if user will enter will click on submit button then it show all the related information regards to that Movie name.
 
 ## index2.html
 
 This contains the code for api2.<br>
 whenever user will enter any number it will show all the index that will contain the prefix as entered number.<br>
 if user will enter will click on submit button then it show all the related information regards to that Index number.
 
 ## Scraped_list_of_movies
 
 It is the json file that contains scrapped data in the form of list of dictionary.
 
