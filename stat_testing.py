# imports
import pandas as pd
from split_get_scale import SplitGetScale
from scipy.stats import f_oneway

# import dataframe
df = pd.read_csv("nutrition_repos_clean_stemmed_lemmatize.csv")

# creating train, test if required
sgs = SplitGetScale()
train, test = sgs.split(df)
train_for_stats = train.copy()

df = pd.read_csv("nutrition_repos_clean_stemmed_lemmatize.csv")

def get_unique_words(string):
    num_unique_words = len(set(string.split()))
    return num_unique_words

def get_unique_stemmed_anova():

    train_for_stats["cleaned_stemmed_unique"] = train_for_stats["clean_stemmed"].apply(get_unique_words)

    java_stemmed = train_for_stats["cleaned_stemmed_unique"][train_for_stats["language"] == "Java"]
    js_stemmed = train_for_stats["cleaned_stemmed_unique"][train_for_stats["language"] == "JavaScript"]
    python_stemmed = train_for_stats["cleaned_stemmed_unique"][train_for_stats["language"] == "Python"]
    other_stemmed = train_for_stats["cleaned_stemmed_unique"][train_for_stats["language"] == "other"]

    f, p = f_oneway(java_stemmed, js_stemmed, python_stemmed, other_stemmed)

    return f, p

def get_unique_lemmed_anova():

    train_for_stats["cleaned_lemmed_unique"] = train_for_stats["clean_lemmatized"].apply(get_unique_words)

    java_lemmed = train_for_stats["cleaned_lemmed_unique"][train_for_stats["language"] == "Java"]
    js_lemmed = train_for_stats["cleaned_lemmed_unique"][train_for_stats["language"] == "JavaScript"]
    python_lemmed = train_for_stats["cleaned_lemmed_unique"][train_for_stats["language"] == "Python"]
    other_lemmed = train_for_stats["cleaned_lemmed_unique"][train_for_stats["language"] == "other"]

    f, p = f_oneway(java_lemmed, js_lemmed,python_lemmed, other_lemmed)

    return f, p