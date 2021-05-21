# les modeles ici
import pickle
import sklearn

with open("./ml/models/load/knn.pkl", "rb") as f:
    knn = pickle.load(f)

with open("./ml/models/load/Logistic_Regression.pkl", "rb") as f:
    Logistic_Regression = pickle.load(f)

with open("./ml/models/load/model_lr.pkl", "rb") as f:
    model_lr = pickle.load(f)

with open("./ml/models/load/random_forest.pkl", "rb") as f:
    random_forest = pickle.load(f)

exported_models = {"knn": knn,
                   "Logistic_Regression": Logistic_Regression,
                   "model_lr": model_lr,
                   "random_forest": random_forest}

# exported_models['reg_line'] = qsdfqsdfq