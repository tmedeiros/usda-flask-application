import os
from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from predictors import UserEntryForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    form = UserEntryForm()
    return render_template('index.html', title='USDA Cattle Price Prediction', form=form)


if __name__ == '__main__':
    app.run()
