import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier

def lr_stemm(y_train_stemmed, y_test_stemmed, X_train_stemmed, X_test_stemmed):
    '''
    This function takes stemm data and creates dataframes for y_test and y_train.
    It takes the data frames and fits logistic regression and makes a prediction
    '''
    # create dataframe for stemm train / test
    y_train_stemmed = pd.DataFrame(dict(actual=y_train_stemmed))
    y_test_stemmed = pd.DataFrame(dict(actual=y_test_stemmed))

    # create logistics regesson object by fitting to X_trian and y_train
    lm_stemm = LogisticRegression().fit(X_train_stemmed, y_train_stemmed)

    # make prediction on train and test for stemm data
    y_train_stemmed['predicted'] = lm_stemm.predict(X_train_stemmed)
    y_test_stemmed['predicted'] = lm_stemm.predict(X_test_stemmed)

    return y_train_stemmed, y_test_stemmed


def lr_lemm(y_train_lemmed, y_test_lemmed, X_train_lemmed, X_test_lemmed):
    '''
    This function takes lemm data and creates dataframes for y_test and y_train.
    It takes the data frames and fits logistic regression and makes a prediction
    '''
    # create dataframe for lemm train / test
    y_train_lemmed = pd.DataFrame(dict(actual=y_train_lemmed))
    y_test_lemmed = pd.DataFrame(dict(actual=y_test_lemmed))

    # create logistics regesson object by fitting to X_trian and y_train
    lm_lemm = LogisticRegression().fit(X_train_lemmed, y_train_lemmed)

    # make prediction on train and test for Lemmatize data
    y_train_lemmed['predicted'] = lm_lemm.predict(X_train_lemmed)
    y_test_lemmed['predicted'] = lm_lemm.predict(X_test_lemmed)

    return y_train_lemmed, y_test_lemmed


def lr_print(y_train_lemmed, y_test_lemmed, y_train_stemmed, y_test_stemmed):
    '''
    This function prints the accuracy score for for stemm and lemm data using logistics regression
    '''
    print(f"TRAIN\nLogistics Regression Stemmed Accuracy: {round(accuracy_score(y_train_stemmed.actual, y_train_stemmed.predicted), 2)}")
    print(f"Logistics Regression Lemmed Accuracy: {round(accuracy_score(y_train_lemmed.actual, y_train_lemmed.predicted), 2)}")


    print(f"\nTEST\nLogistics Regression Stemmed Accuracy Test: {round(accuracy_score(y_test_stemmed.actual, y_test_stemmed.predicted), 2)}")
    print(f"Logistics Regression Lemmed Accuracy Test: {round(accuracy_score(y_test_lemmed.actual, y_test_lemmed.predicted), 2)}")


def rfc_stem(X_train_stemmed, X_test_stemmed, y_train_stemmed):

    # fit and predict with stemmed data
    rfc_stem =  RandomForestClassifier(max_depth=5, min_samples_leaf=5, min_samples_split=6, n_estimators=10, random_state=123, warm_start=True, bootstrap=False)
    rfc_stem.fit(X_train_stemmed, y_train_stemmed)
    y_pred_train_stem = rfc_stem.predict(X_train_stemmed)
    y_pred_test_stem = rfc_stem.predict(X_test_stemmed)

    return y_pred_train_stem, y_pred_test_stem

def rfc_lem(X_train_lemmed, X_test_lemmed, y_train_lemmed):

    # fit and predict with lemmatized data
    rfc_lem =  RandomForestClassifier(min_samples_split=4, n_estimators=10, min_samples_leaf=1, random_state=123, warm_start=True, max_depth=None, bootstrap=True)
    rfc_lem.fit(X_train_lemmed, y_train_lemmed)
    y_pred_train_lem = rfc_lem.predict(X_train_lemmed)
    y_pred_test_lem = rfc_lem.predict(X_test_lemmed)

    return y_pred_train_lem, y_pred_test_lem

def print_rfc_metric(X_train_stemmed, X_test_stemmed, y_train_stemmed, y_test_stemmed, X_train_lemmed, X_test_lemmed, y_train_lemmed, y_test_lemmed):

    y_pred_train_stem, y_pred_test_stem = rfc_stem(X_train_stemmed, X_test_stemmed, y_train_stemmed)
    y_pred_train_lem, y_pred_test_lem = rfc_lem(X_train_lemmed, X_test_lemmed, y_train_lemmed)

    # print stemmed/lemmed train rfc accuracy
    print(f"TRAIN\nRandom Forest Classifier Stemmed Accuracy: {round(accuracy_score(y_train_stemmed, y_pred_train_stem), 2)}")
    print(f"Random Forest Classifier Lemmed Accuracy: {round(accuracy_score(y_train_lemmed, y_pred_train_lem), 2)}")

    # print stemmed_lemmed test rfc accuracy
    print(f"\nTEST\nRandom Forest Classifier Stemmed Accuracy Test: {round(accuracy_score(y_test_stemmed, y_pred_test_stem ), 2)}")
    print(f"Random Forest Classifier Lemmed Accuracy Test: {round(accuracy_score(y_test_lemmed, y_pred_test_lem), 2)}")