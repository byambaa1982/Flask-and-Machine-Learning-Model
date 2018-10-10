from flask import Flask, jsonify, request
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
import numpy as np
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)


@app.route('/')
def hello_world():
	print("..")
	return 'Hello, World! or else kkk. it is Byamba. Starting Flask'

# L1_logistic = LogisticRegression(C=1.0, penalty='l1')
# model = logreg.fit(df[['Speed']].values, df["student"].values)

@app.route('/jazzhands')
def jazzhands():
    return "<h1>Here's some <i>Pizzazz!</i></h1>"

@app.route('/twice/<int:x>') # int says the expected data type
def twice(x):
    output = 2 * x
    return 'Two times {} is {}'.format(x, output)
@app.route('/login/<string:x>') # int says the expected data type
def login(x):
    return 'Hey {} how is your day. {} is great pythonist'.format(x,x)

# ------------------------------------ #
# -------- DATA SCIENCE TIME --------- #
# ------------------------------------ #

# if __name__ == '__main__':
# build a basic model for titanic survival
titanic_df = pd.read_csv('data/titanic_data.csv')
titanic_df['sex_binary'] = titanic_df['sex'].map({'female': 1, 'male': 0})
train_df, test_df = train_test_split(titanic_df)

titanic_df = pd.read_csv('data/titanic_data.csv')
titanic_df['sex_binary'] = titanic_df['sex'].map({'female': 1, 'male': 0})

# choose our features and create test and train sets
features = [u'pclass', u'age', u'sibsp', u'parch', u'fare', u'sex_binary', 'survived']
train_df, test_df = train_test_split(titanic_df)
train_df = train_df[features].dropna()
test_df = test_df[features].dropna()

features.remove('survived')
X_train = train_df[features]
y_train = train_df['survived']
X_test = test_df[features]
y_test = test_df['survived']

# fit the model
L1_logistic = LogisticRegression(C=1.0, penalty='l1')
L1_logistic.fit(X_train, y_train)

# check the performance
target_names = ['Died', 'Survived']
y_pred = L1_logistic.predict(X_test)
print(classification_report(y_test, y_pred, target_names=target_names))

# start the app
app.run(debug=True)
@app.route('/titanic', methods=['GET', 'POST'])
def titanic():
    data = {} 
    if request.form:
        # get the form data
        form_data = request.form
        data['form'] = form_data
        predict_class = float(form_data['predict_class'])
        predict_age = float(form_data['predict_age'])
        predict_sibsp = float(form_data['predict_sibsp'])
        predict_parch = float(form_data['predict_parch'])
        predict_fare = float(form_data['predict_fare'])
        predict_sex = form_data['predict_sex']
        
        # convert the sex from text to binary
        if predict_sex == 'M':
            sex = 0
        else:
            sex = 1
        input_data = np.array([predict_class, predict_age, predict_sibsp, predict_parch, predict_fare, sex])
        
        # get prediction
        prediction = L1_logistic.predict_proba(input_data.reshape(1, -1))
        prediction = prediction[0][1] # probability of survival
        data['prediction'] = 'Approximate price is {:.1f}%'.format(prediction * 100)
    return render_template('titanic.html', data=data)

# ------------------------------------ #
# -------- Machine Learning on a Used Car market --------- #
# ------------------------------------ #

large = pd.read_csv('data/used_cars.csv')
large=large.dropna()
large=large.drop('index', axis=1)

X=large.drop('price', axis=1)
y=large[['price']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

gbr = GradientBoostingRegressor(n_estimators=90, learning_rate=0.1,
     max_depth=5, random_state=0, loss='ls')

gbr.fit(X_train, np.log(y_train))
gbr.score(X_train, np.log(y_train))
gbr.score(X_test, np.log(y_test))
y_pred=gbr.predict(X_test)
y_pred=np.exp(y_pred)

app.run(debug=True)
@app.route('/cars', methods=['GET', 'POST'])
def cars():
    output = None
    if request.method=='POST':
        mileage = float(request.form['mileage'])
        output=y_pred[4]

    return render_template('base.html', output=output)
app.run(debug=True)
@app.route('/predcars', methods=['GET', 'POST'])
def predcars():
    data = {} 
    if request.form:
        # get the form data
        form_data = request.form
        data['form'] = form_data
        predict_mile = float(form_data['predict_mile'])
        predict_modelyear=float(form_data['predict_year'])
        predict_brake=float(form_data['predict_brake'])
        predict_airbag=float(form_data['predict_airbag'])
        predict_camera=float(form_data['predict_camera'])
        predict_control=float(form_data['predict_control'])
        predict_speaker=float(form_data['predict_speaker'])
        predict_video=float(form_data['predict_video'])
        predict_bluetooth=float(form_data['predict_bluetooth'])
        predict_alarm=float(form_data['predict_alarm'])
        predict_navigation=float(form_data['predict_navigation'])
        predict_digital=float(form_data['predict_digital'])
        predict_keyless=float(form_data['predict_keyless'])
        predict_heated=float(form_data['predict_heated'])
        predict_leater=float(form_data['predict_leather'])
        predict_armrest=float(form_data['predict_armrest'])
        predict_total=float(form_data['predict_total'])
        predict_drivetrain=float(form_data['predict_drivetrain'])
        predict_fueltype=float(form_data['predict_fueltype'])
        predict_transmission=float(form_data['predict_transmission'])
        predict_make=float(form_data['predict_make'])
        predict_model=float(form_data['predict_model'])

        input_data = np.array([predict_mile,
                                predict_modelyear,
                                predict_brake,
                                predict_airbag,
                                predict_camera,
                                predict_control,
                                predict_speaker,
                                predict_video,
                                predict_bluetooth,
                                predict_alarm,
                                predict_navigation,
                                predict_digital,
                                predict_keyless,
                                predict_heated,
                                predict_leater,
                                predict_armrest,
                                predict_total,
                                predict_drivetrain,
                                predict_fueltype,
                                predict_transmission,
                                predict_make, 
                                predict_model])
        
        # get prediction
        prediction = gbr.predict(input_data.reshape(1, -1))
        prediction = np.exp(prediction[0]) # probability of survival
        data['prediction'] = 'Approximate price is {:.1f}'.format(prediction)
    return render_template('cars.html', data=data)

