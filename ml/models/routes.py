from flask import Blueprint, redirect, render_template, url_for, flash, abort

from ml.models.forms import FormPrediction
from ml.models.utils import exported_models

import numpy as np

models = Blueprint("model", "__name__")

@models.route('/', methods=['GET', 'POST'])
def calculus():
    # creer les models
    
    form = FormPrediction()
    print(form.models)
    #list(exported_models.keys())

    if form.validate_on_submit():
        to_predict = np.array([[form.pregnent.data, form.glucose.data, form.pression_art.data,
                                form.epaisseur_peau.data, form.insulin.data, form.IMC.data,
                                form.fonction_diabete.data, form.age.data]])
        res = exported_models[form.models.data].predict(to_predict)
        print("\n\n\n")
        print(res)
        res = "Diabethique" if res[0] > 0.3 else "Non diabetique"
        print(res)
        return render_template("/default.html", form=form, diabetique=res, pred=to_predict, model_used=form.models.data)
    return render_template("/default.html", form=form)
