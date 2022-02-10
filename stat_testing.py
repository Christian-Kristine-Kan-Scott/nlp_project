# imports
import pandas as pd
from scipy.stats import f_oneway

# scott's start
def get_unique_words(string):
    num_unique_words = len(set(string.split()))
    return num_unique_words

def get_unique_stemmed_anova(df):

    df["cleaned_stemmed_unique"] = df["clean_stemmed"].apply(get_unique_words)

    java_stemmed = df["cleaned_stemmed_unique"][df["language"] == "Java"]
    js_stemmed = df["cleaned_stemmed_unique"][df["language"] == "JavaScript"]
    python_stemmed = df["cleaned_stemmed_unique"][df["language"] == "Python"]
    other_stemmed = df["cleaned_stemmed_unique"][df["language"] == "other"]

    f, p = f_oneway(java_stemmed, js_stemmed, python_stemmed, other_stemmed)

    return f, p

def get_unique_lemmed_anova(df):

    df["cleaned_lemmed_unique"] = df["clean_lemmatized"].apply(get_unique_words)

    java_lemmed = df["cleaned_lemmed_unique"][df["language"] == "Java"]
    js_lemmed = df["cleaned_lemmed_unique"][df["language"] == "JavaScript"]
    python_lemmed = df["cleaned_lemmed_unique"][df["language"] == "Python"]
    other_lemmed = df["cleaned_lemmed_unique"][df["language"] == "other"]

    f, p = f_oneway(java_lemmed, js_lemmed,python_lemmed, other_lemmed)

    return f, p
# scott's end

# christian start
def q3_stat_test(df):

    # STEMMED
    java_stemmed = df["cleaned_stemmed_length"][df["language"] == "Java"]
    js_stemmed = df["cleaned_stemmed_length"][df["language"] == "JavaScript"]
    python_stemmed = df["cleaned_stemmed_length"][df["language"] == "Python"]
    other_stemmed = df["cleaned_stemmed_length"][df["language"] == "other"]

# LEMMED
    java_lemmed = df["cleaned_lemmed_length"][df["language"] == "Java"]
    js_lemmed = df["cleaned_lemmed_length"][df["language"] == "JavaScript"]
    python_lemmed = df["cleaned_lemmed_length"][df["language"] == "Python"]
    other_lemmed = df["cleaned_lemmed_length"][df["language"] == "other"]

    print('The Anova test for Stemmed :', f_oneway(java_stemmed,js_stemmed,python_stemmed,other_stemmed))
    print('The Anova test for Lemmetize :', f_oneway(java_lemmed,js_lemmed,python_lemmed,other_lemmed))
# christian end