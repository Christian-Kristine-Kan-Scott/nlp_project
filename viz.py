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
    
    
    
------------------
    
def stemm_top_ten_words(df):
    '''
    '''
    
    # join rows of string together
    stemm_words = ' '.join(df.clean_stemmed)

    # split string by space to isolate words
    stemm_words_list = stemm_words.split()

    # create dataframe of word count
    stemm_word_count = pd.Series(stemm_words_list).value_counts().reset_index()
    stemm_word_count.columns=['word','count']

    # drop non-words
#     stemm_word_count = word_count.drop([0,2,5,12])

    stemm_top_10_words = stemm_word_count.head(10)

    return stemm_words, stemm_top_10_words


def lemm_top_ten_words(df):
    '''
    '''
    
    # join rows of string together
    lemm_words = ' '.join(df.clean_lemmatized)

    # split string by space to isolate words
    lemm_words_list = lemm_words.split()

    # create dataframe of word count
    lemm_word_count = pd.Series(lemm_words_list).value_counts().reset_index()
    lemm_word_count.columns=['word','count']

    # drop non-words
#     word_count = word_count.drop([0,2,5,12])

    lemm_top_10_words = lemm_word_count.head(10)
    
    return lemm_top_10_words, lemm_words


def stemm_top_ten(stemm_top_10_words):
    '''
    '''
    # plot bar graph for top 10 words
    sns.barplot(data=stemm_top_10_words, x='count', y='word')
    plt.title('Top 10 Most Common words')
    plt.show()
    
    
def lemm_top_ten(lemm_top_10_words):
    '''
    '''
    # plot bar graph for top 10 words
    sns.barplot(data=lemm_top_10_words, x='count', y='word')
    plt.title('Top 10 Most Common words')
    plt.show()
    
    
def stemm_wordcloud(stemm_words):
    '''
    '''
    
    # create word cloud image
    img = WordCloud(background_color='white').generate(stemm_words)
    # axis aren't very useful for a word cloud
    plt.axis('off')
    # WordCloud() produces an image object, which can be displayed with plt.imshow
    plt.imshow(img)
    plt.show()
    
    
    
def lemm_wordcloud(lemm_words):
    '''
    '''
    # create word cloud image
    img = WordCloud(background_color='white').generate(lemm_words)
    # axis aren't very useful for a word cloud
    plt.axis('off')
    # WordCloud() produces an image object, which can be displayed with plt.imshow
    plt.imshow(img)
    plt.show()
    
    
    
    




    
    
