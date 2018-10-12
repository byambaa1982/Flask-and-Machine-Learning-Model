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
import pickle

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

# ------------Pickle my model to use later------------#
pickle.dump(gbr, open("model.pkl", "wb"))

app.run(debug=True)
@app.route('/cars', methods=['GET', 'POST'])
def cars():
    output = None
    if request.method=='POST':
        mileage = float(request.form['mileage'])
        output=y_pred[4]

    return render_template('base.html', output=output)

# -------- Print score of my model --------- #

app.run(debug=True)
@app.route('/scores')
def scores():
    load_model=pickle.load(open("model.pkl", "rb"))
    result=load_model.score(X_train, np.log(y_train))
    test_score=load_model.score(X_test, np.log(y_test))
    return render_template('score.html', output=result, test_score=test_score)
@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username=g.user.username,
                   email=g.user.email,
                   id=g.user.id)
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

