#Let's break down what this code is doing.

#1. The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL.
#2. The second line says we'll use PyMongo to interact with our Mongo database.
#3 The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.


from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#Under these lines, let's add the following to set up Flask:
app = Flask(__name__)

#We also need to tell Python how to connect to Mongo using PyMongo. 
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
#"mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app".


#Set Up App Routes
#The code we create next will set up our Flask routes: one for the main HTML page everyone will view when visiting the web app, and one to actually scrape new data using the code we've written.


#First, let's define the route for the HTML page. In our script, type the following:

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#the @app.route , tells Flask what to display when we're lookign at the hotemage, index. html
#index.html is the default HTML file that we will use to display the content we've scraped. 
#accomplished through the function (def index
#mars = mongo.db.mars.find_one() uses PyMongo to find the "mars" collection in our database, which we will create when we convert our Jupyter scraping code to Python Script. We will also assign that path to themars variable for use later.

#return render_template("index.html" tells Flask to return an HTML template using an index.html file. We'll create this file after we build the Flask routes.

#, mars=mars) tells Python to use the "mars" collection in MongoDB. This function is what links our visual representation of our work, our web app, to the code that powers


#NEXT FUNCTION SETS UP THE SCRAPING ROUTE
 #  1: defines Flask route. "/scrape", run the function created below
 # 2: access the database, scrape new data using our scraping. py
# 3: def scrape: defines the scraping function
# 4: asign new variable that points to our Mongo database Mars =
#5 : create variable that holds the scraped data. (scraping_all)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)
   if __name__ == "__main__":
      app.run()
