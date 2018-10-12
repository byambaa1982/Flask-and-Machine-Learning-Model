# Predict price for a particular used car in Flask
### 1. What is this project?

Shopping for a used vehicle is quite tricky, because there are following questions: Is the price reasonable? Or, why does this car seem cheaper [or more expensive]? This question is often difficult to answer due to the fact that it's hard to keep track of all the vehicles of interest currently available on the market.

### 2. Project Objective

This project's objective was to build a model and deploy it using Flask python framework that determines if the asking price for a particular car is reasonable given the information provided in the listing. 

### 3. Steps

+ Creating your flask dev environment
+ Flask App Organization
+ Train a model in flask
+ Using a Bootstrap templates to add some style
+ Passing data and predicting with our model
+ Jinja templating with flask

### Data  limitations:

+ Only looked at used cars. According to Ward’s Automotive Yearbook 2013, about 42 million used cars ($380 billion in total revenues) were sold in the U.S. in 2012. By comparison, about 15 million new cars ($300 billion in total revenue) were sold in the U.S. in the same year.
+ Vehicles located within 75 miles of Chicago, IL, because of local consumers’ preferences.
Minimum aksing price of $5,000.
After obtaining and filtering the data, the final dataset contained:
+ 4,235 unique listings
+ 54 makes
+ 485 models
+ 34 unique years


### Conclusion
+ My scraped data was very messy and missing many entries, especially exterior color, interior color and plant country. I had to drop these, even though those are very important features.  While the details provided in the downloaded listings are quite comprehensive, I was only able to include a small number of the features. And some features, especially text feature, were very unreliable. Many of the them had multiple variations of the same name, or different names with the same meaning, such as 'radio!, fm/am radio, radio!!!'. I was not able to develop a code capable of cleaning up the discrepancies between the various names, and I suspect this had a negative impact on the regression. 
+ My model shows different regression (Fig 3.5) on expensive cars (i.e. more than $150000), because exotic cars have very different features, various interests and are very different from one another. 
