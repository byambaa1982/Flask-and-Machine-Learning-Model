from flask import Flask, jsonify, request
from sklearn.linear_model import LogisticRegression
import pandas as pd

app = Flask(__name__)

from sklearn.datasets import load_iris
import pandas as pd

data = load_iris()
df = pd.DataFrame(data['data'], columns=['sepal_len', 'sepal_width', 'petal_lengh', 'petal_width'])

X=df[['sepal_width', 'sepal_len']]
y=data['target']
model.score(X_train, y_train)

@app.route('/predict-iris')
def predict_iris():

    predicted=model.predict(X_test)
    robabilities = model.predict_proba(X_test).tolist()

    return str(request.args.getlist('param'))
