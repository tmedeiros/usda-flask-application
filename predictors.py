from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class UserEntryForm(FlaskForm):
    # username = StringField('Username', validators=[DataRequired()])
    dropdown_list_grade = [('0', '------ Please select a grade ------'), ('1', '0 - 35% Choice'),
                           ('2', '35 - 65% Choice'), ('3', '65 - 80% Choice'), ('4', 'Over 80% Choice'),
                           ('5', 'Total all grades')]
    dropdown_list_purchase_type = [('0', '- Please select a Purchase Type -'), ('1', 'Formula Net'),
                            ('2', 'Negotiated Grid Net')]
    dropdown_list_selling_basis = [('0', '--- Please select a Selling Basis ---'), ('1', 'Dressed'), ('2', 'Live')]
    dropdown_list_class = [('0', '------ Please select a class------'), ('1', 'All Steers & Heifers'),
                           ('2', 'Dairybred Steer/Heifer'), ('3', 'Heifer'), ('4', 'Mixed Steer/Heifer'),
                           ('5', 'Mixed Steer/Heifer/Cow'), ('6', 'Steer')]
    headcount = StringField('Head Count')
    weight_range_low = StringField('Weight Range Low')
    weight_range_high = StringField('Weight Range High')
    average_weight = StringField('Average Weight')
    dressed_percentage = StringField('Dressed Percentage')
    report_year = StringField('Report Year')
    report_month = StringField('Report Month')
    price_range_low = StringField('Price Range Low')
    price_range_high = StringField('Price Range High')
    purchase_type = SelectField('Purchase Type', choices=dropdown_list_purchase_type)
    selling_basis = SelectField('Selling Basis', choices=dropdown_list_selling_basis)
    class_type = SelectField('Class Type', choices=dropdown_list_class)
    grade = SelectField('Grade', choices=dropdown_list_grade)
    submit = SubmitField('Submit')
