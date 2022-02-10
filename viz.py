# imports
import pandas as pd
from split_get_scale import SplitGetScale
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# read in the dataframe
df = pd.read_csv("nutrition_repos_clean_stemmed_lemmatize.csv")

# if required split the data into training and testing
sgs = SplitGetScale()
train, test = sgs.split(df)
train_for_viz = train.copy()

def get_unique_words(string):
    num_unique_words = len(set(string.split()))
    return num_unique_words

def get_unique_groups():

    train_for_viz["cleaned_stemmed_unique"] = train_for_viz["clean_stemmed"].apply(get_unique_words)
    train_for_viz["cleaned_lemmed_unique"] = train_for_viz["clean_lemmatized"].apply(get_unique_words)

    lang_mean_unqiue_stemmed = train_for_viz.groupby("language")["cleaned_stemmed_unique"].agg(["mean"])
    lang_mean_unique_lemma = train_for_viz.groupby("language")["cleaned_lemmed_unique"].agg(["mean"])

    return lang_mean_unqiue_stemmed, lang_mean_unique_lemma

def get_unique_stemmed_viz():

    lang_mean_unqiue_stemmed, _ = get_unique_groups()
    sns.barplot(x=lang_mean_unqiue_stemmed.index, y=lang_mean_unqiue_stemmed["mean"])

def get_unique_lemmed_viz():

    _, lang_mean_unique_lemma = get_unique_groups()
    sns.barplot(x=lang_mean_unique_lemma.index, y=lang_mean_unique_lemma["mean"])
    
    


    
    
    
def idf_words_viz():
    '''
    Shows bar plot for 2 given points
    '''
    sns.barplot(data=words_idf, x='idf', y='words', palette="Blues_d")
    plt.title('IDF of most common words')
    plt.show()

    
def repo_language():
    '''
    Shows bar plot for 2 given points
    '''
    fig = plt.figure(figsize=(8, 5))
    ax = df.language.value_counts().plot.bar(width=.7, ec='black', color='teal')
    ax.set(title='Distribution of Languages in Health Repos', ylabel='Number of Repos', xlabel='Name of Language') 
    
    
def q3_viz():
    df = pd.read_csv('nutrition_repos_clean_stemmed_lemmatize.csv')
    df["cleaned_stemmed_length"] = df["clean_stemmed"].apply(get_readme_length)
    df["cleaned_lemmed_length"] = df["clean_lemmatized"].apply(get_readme_length)
    
    lem_df = df.groupby("language")["cleaned_lemmed_length"].agg(["mean"])
    lem_df_desc = lem_df.sort_values('mean', ascending=True)
    ax = lem_df_desc.plot(kind="barh")
    
    # Get a Matplotlib figure from the axes object for formatting purposes
    fig = ax.get_figure()
    # Change the plot dimensions (width, height)
    fig.set_size_inches(16, 10)
    # Change the axes labels
    ax.set_xlabel("Programming Language ")
    ax.set_ylabel("Average Length of READme")
