# Predict price for a particular used car in Flask
### 1. What is this project?

Shopping for a used vehicle is quite tricky, because there are following questions: Is the price reasonable? Or, why does this car seem cheaper [or more expensive]? This question is often difficult to answer due to the fact that it's hard to keep track of all the vehicles of interest currently available on the market.

### 2. Project Objective

This project's objective was to build a model that determines if the asking price for a particular car is reasonable given the information provided in the listing and deploy ML model using Flask for public as a ML production. 

### 3. Steps

+ Creating my flask dev environment
+ Organize Flask App
+ Train a model in flask
+ Using a Bootstrap templates to add some style
+ Passing data and predicting with my model
+ Jinja templating with flask

### Getting prediction inputs into flask

My model uses the following variables to predict a used car price:
 
+ Model Year: 
+ Brakes: 
+ Airbag: 
+ Camera: 
+ Controls: 
+ Speakers: 
+ Video: 
+ Bluetooth: 
+ Alarm: 
+ Navigations: 
+ Digital: 
+ Keyless: 
+ Heated: 
+ Leather: 
+ Armrest: 
+ Drivetrain: 
+ Fuel Type: 
+ Transmission:
+ Make: 
+ Model: 
+ Total: 


In order to hook up the web interface with the model I had to allow the user to input all of the required model parameters. The easiest way to do this is with a simple web form.

![alt text](/image/input "Logo Title Text 1")


### Conclusion
+ My scraped data was very messy and missing many entries, especially exterior color, interior color and plant country. I had to drop these, even though those are very important features.  While the details provided in the downloaded listings are quite comprehensive, I was only able to include a small number of the features. And some features, especially text feature, were very unreliable. Many of the them had multiple variations of the same name, or different names with the same meaning, such as 'radio!, fm/am radio, radio!!!'. I was not able to develop a code capable of cleaning up the discrepancies between the various names, and I suspect this had a negative impact on the regression. 
+ My model shows different regression (Fig 3.5) on expensive cars (i.e. more than $150000), because exotic cars have very different features, various interests and are very different from one another. 
