import gzip
import os
import pickle
import sklearn

import numpy as np
from flask import Flask, request, render_template, flash

from predictors import UserEntryForm

# from flask_bootstrap import Bootstrap

app = Flask(__name__)
# bootstrap = Bootstrap(app)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserEntryForm()
    if request.method == 'POST':
        form.result = ' '
        try:
            user_data = [form.headcount.data, form.weight_range_low.data, form.weight_range_high.data,
                         form.average_weight.data, form.dressed_percentage.data, form.price_range_low.data,
                         form.price_range_high.data, form.report_year.data, form.report_month.data, 0.0, 0.0,
                         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            user_data[9] = 1.0 if form.purchase_type.data == '1' else 0.0
            user_data[10] = 1.0 if form.purchase_type.data == '2' else 0.0
            user_data[11] = 1.0 if form.selling_basis.data == '1' else 0.0
            user_data[12] = 1.0 if form.selling_basis.data == '2' else 0.0
            user_data[13] = 1.0 if form.class_type.data == '1' else 0.0
            user_data[14] = 1.0 if form.class_type.data == '2' else 0.0
            user_data[15] = 1.0 if form.class_type.data == '3' else 0.0
            user_data[16] = 1.0 if form.class_type.data == '4' else 0.0
            user_data[17] = 1.0 if form.class_type.data == '5' else 0.0
            user_data[18] = 1.0 if form.class_type.data == '6' else 0.0
            user_data[19] = 1.0 if form.grade.data == '1' else 0.0
            user_data[20] = 1.0 if form.grade.data == '2' else 0.0
            user_data[21] = 1.0 if form.grade.data == '3' else 0.0
            user_data[22] = 1.0 if form.grade.data == '4' else 0.0
            user_data[23] = 1.0 if form.grade.data == '5' else 0.0

            array = np.asarray(user_data, dtype=np.float)
            user_data_norm = (array - array.mean()) / array.std()
            transformed_prediction_data = np.asarray(user_data_norm).reshape(-1, 24)

            model_path = "usda_model.pkl"
            with gzip.open(model_path, 'rb') as f:
                p = pickle.Unpickler(f)
                usda_model = p.load()
            usda_model.predict(transformed_prediction_data)

            result = usda_model.predict(transformed_prediction_data)
            result = "${:.2f}".format(result[0])
            form.result = result
        except:
            form.result = 'Please, enter predictor values to continue'

        return render_template('index.html', form=form)
    return render_template('index.html', title='USDA Cattle Price Prediction', form=form)


if __name__ == '__main__':
    app.run()
