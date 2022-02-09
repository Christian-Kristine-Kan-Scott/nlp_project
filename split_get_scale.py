from prepare import Prepare
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

class SplitGetScale:

    def split(self, df):

        train, test = train_test_split(df, test_size=.15, random_state=123)
        train, validate = train_test_split(train, test_size=.2, random_state=123)

        return train, validate, test

    def get_Xy(self, train, validate, test, cols_drop=None):

        if cols_drop:
            X_train = train.drop(cols_drop, axis=1)
            X_val = validate.drop(cols_drop, axis=1)
            X_test = test.drop(cols_drop, axis=1)

        tfid = TfidfVectorizer()

        X_train =
        X_val =
        X_test =

        y_train = train["language"]
        y_val = validate["language"]
        y_test = test["language"]



        return (X_train, y_train), (X_val, y_val), (X_test, y_test)

    def scale(self, X_train, X_validate, X_test):

        scale = StandardScaler()
        scale.fit(X_train)

        X_train_scaled = pd.DataFrame(data=scale.transform(X_train), columns=X_train.columns)
        X_val_scaled = pd.DataFrame(data=scale.transform(X_validate), columns=X_train.columns)
        X_test_scaled = pd.DataFrame(data=scale.transform(X_test), columns=X_train.columns)

        return X_train_scaled, X_val_scaled, X_test_scaled, scale