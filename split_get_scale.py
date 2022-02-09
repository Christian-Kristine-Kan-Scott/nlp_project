from prepare import Prepare
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

class SplitGetScale:

    def split(self, df):

        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df["language"])

        return train, test

    def get_Xy(self, train, test, cols_train=None):

        if cols_train:
            X_train = train[cols_train]
            X_test = test[cols_train]

        tfidf = TfidfVectorizer()

        X_train = tfidf.fit_transform(X_train)
        X_test = tfidf.transform(X_test)

        y_train = train["language"]
        y_test = test["language"]

        return (X_train, y_train), (X_test, y_test)

    def scale(self, X_train, X_validate, X_test):

        scale = StandardScaler()
        scale.fit(X_train)

        X_train_scaled = pd.DataFrame(data=scale.transform(X_train), columns=X_train.columns)
        X_test_scaled = pd.DataFrame(data=scale.transform(X_test), columns=X_train.columns)

        return X_train_scaled, X_test_scaled, scale