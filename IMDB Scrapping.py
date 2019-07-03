import pymongo as pm
#from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
import json


pages= 25                                                   #count pages
url = 'http://www.imdb.com/search/title?genres=action' #initial page url

counter=1                # for changing url according to number of movies

index=1                  #for giving serial number

scraped_list=[]          #it will contain my dictonary for every movie

while(pages>0):
    
    response = requests.get(url).text                      #gets url
    soup = BeautifulSoup(response, 'lxml')                 #scrap html syntax
    
    #print(soup.prettify)

    for all_detail in soup.find_all('div',class_='lister-item-content'):       #going through all the each movie section
        name=all_detail.a.text                                                 #scraping name of movie
        
        year = all_detail.find('span', class_='lister-item-year').text         #scraping year of movie
        
        try:
            rating = all_detail.find('div', class_='inline-block ratings-imdb-rating').get('data-value')   #scraping ratings of movie
        except AttributeError:                                                                          
            rating = "NA"
            
        each_para_text=[]                                                      #contains text for each paragraph
        
        for all_paragraph in all_detail.find_all('p'):
            each_para_text.append(all_paragraph.text)

        find_stars=str(each_para_text[2]).find("Stars:")                       #getting the starting index of stars
        
        star_for_each_movie=[each_cast.strip() for each_cast in  each_para_text[2][find_stars+6:].split(",")]   #storing star cast of movie
        
               
        data={"Index":index,                
              "Movie_name":name,
              "Year":year.strip('-'),
              "Ratings":rating,
              "Star_Cast":star_for_each_movie}                                 #storing index,name,year,rating,star cast of movie
        
        index=index+1
        
        scraped_list.append(data)
        
    counter=counter+50
    url='http://www.imdb.com/search/title?genres=action&start='+str(counter)   #changing url for going to next page
        
    pages=pages-1
        

for ind in scraped_list:
    print(ind['Index'],'-',ind['Movie_name'],'-',ind['Year'],'-',ind['Star_Cast'],'-',ind['Ratings'])
    print()

#create json
with open('scraped_list_of_movies', 'w') as fout:
    json.dump(scraped_list , fout)
  
print("All the Scrapping is completed")

#connecting to Mongodb
try: 
    conn = pm.MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
  
# database 
db = conn.database 
  
# Created or Switched to collection names: IMDB_Collection 
collection = db.IMDB_Collection

for each_movie_record in scraped_list:
    collection.insert_one(each_movie_record)
    
cursor = collection.find() 
for record in cursor: 
    print(record) 
