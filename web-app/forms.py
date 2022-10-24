from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError
from wtforms.validators import NumberRange

class PredictForm(FlaskForm):
   age = IntegerField('Age', [NumberRange(0, 99, "Choose a value between 0 and 99")])
   gender = SelectField('Gender', choices=[("female", "female"), ("male", "male")])
   work_type = SelectField('Tipo de Trabajo', choices = ["wt1", "wt2", "wt3", "wt4"])
   residence_type = SelectField('Tipo de Residencia', choices = ["r1", "r2", "r3", "r4"])

   hypertension = SelectField('hypertension', choices = ["si", "no"])
   enfermedad_coronaria = SelectField('Enfermedad Coronaria', choices = ["si", "no"])
   
   height = DecimalField('BMI')
   weight = DecimalField('BMI')
   glucose = DecimalField('Nivel de glucosa')
   smokevalues = ["formerly smoked", "smoker", "never", "Unknown"]
   smoker = SelectField('Fumar', choices = smokevalues)
  
  
   submit = SubmitField('Predict')
   
   abc = "" # this variable is used to send information back to the front page
