from flask_wtf import FlaskForm
import flask_wtf
from wtforms import SelectField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired

from ml.models.utils import exported_models

class FormPrediction(FlaskForm):
    pregnent         = IntegerField("Pregnancies", validators=[DataRequired()])
    glucose          = IntegerField("Glucose", validators=[DataRequired()])
    pression_art     = IntegerField("Pression arterielle", validators=[DataRequired()])
    epaisseur_peau   = IntegerField("Epaisseur de peau", validators=[DataRequired()])
    insulin          = IntegerField("Insuline", validators=[DataRequired()])
    IMC              = FloatField("IMC", validators=[DataRequired()])
    fonction_diabete = FloatField("Fonction diabete", validators=[DataRequired()])
    age              = IntegerField("Age", validators=[DataRequired()])
    models           = SelectField("Modèle de prediction", choices=[(key, key) for key in list(exported_models.keys())])
    submit           = SubmitField("envoyer")
