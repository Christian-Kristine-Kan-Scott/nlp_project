# imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(13, 7))
from wordcloud import WordCloud
import numpy as np



# scott's begin
def get_unique_words(string):
    num_unique_words = len(set(string.split()))
    return num_unique_words

def get_unique_groups(df):

    df["cleaned_stemmed_unique"] = df["clean_stemmed"].apply(get_unique_words)
    df["cleaned_lemmed_unique"] = df["clean_lemmatized"].apply(get_unique_words)

    lang_mean_unqiue_stemmed = df.groupby("language")["cleaned_stemmed_unique"].agg(["mean"])
    lang_mean_unique_lemma = df.groupby("language")["cleaned_lemmed_unique"].agg(["mean"])

    return lang_mean_unqiue_stemmed, lang_mean_unique_lemma

def get_unique_stemmed_viz(df):

    lang_mean_unqiue_stemmed, _ = get_unique_groups(df)
    sns.barplot(x=lang_mean_unqiue_stemmed.index, y=lang_mean_unqiue_stemmed["mean"])

def get_unique_lemmed_viz(df):

    _, lang_mean_unique_lemma = get_unique_groups(df)
    sns.barplot(x=lang_mean_unique_lemma.index, y=lang_mean_unique_lemma["mean"])
# end scott

# kristine's start
def idf(word):
    '''A simple way to calculate idf for demonstration. Note that this
    function relies on a globally defined blogs variable.'''

    filename = "nutrition_repos_clean_stemmed_lemmatize.csv"
    df = pd.read_csv(filename)

    docs = [doc for doc in df["clean_lemmatized"]]
    n_occurences = sum([1 for doc in docs if word in doc])
    return len(docs) / n_occurences

def data_words_idf(df):

    #create common words array
    common_words = np.array(['food', 'nutrition', 'user', 'data', 'gram', 'recipe','use','app','database','file'])

    # put the unique words into a data frame
    words_idf = (pd.DataFrame(dict(words=common_words))

    # calculate the idf for each word
    .assign(idf=lambda df: df.words.apply(idf))

    # sort the data for presentation purposes
    .set_index('words')
    .sort_values(by='idf', ascending=True))

    #reset index
    words_idf.reset_index(inplace=True)

    return words_idf


def idf_words_viz(words_idf):
    '''
    Shows bar plot for 2 given points
    '''
    sns.barplot(data=words_idf, x='idf', y='words', palette="Blues_d")
    plt.title('IDF of most common words')
    plt.show()


def repo_language(df):
    '''
    Shows bar plot for 2 given points
    '''
    fig = plt.figure(figsize=(8, 5))
    ax = df.language.value_counts().plot.bar(width=.7, ec='black', color='teal')

    ax.set(title='Distribution of Languages in Health Repos', ylabel='Number of Repos', xlabel='Name of Language')
# end kristine

# christian start
def get_readme_length(string):
    length = len(string.split())
    return length

def q3_viz(df):

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

    ax.set(title='Distribution of Languages in Health Repos', ylabel='Number of Repos', xlabel='Name of Language')
# christian end

# kan start
def stemm_top_ten_words(df):
    '''
    This function takes cleaned stemmed column from the df and joins them to make a string. 
    It splits the string by space to produce a list that then produces a value_counts df.
    '''

    # join rows of string together
    stemm_words = ' '.join(df.clean_stemmed)

    # split string by space to isolate words
    stemm_words_list = stemm_words.split()

    # create dataframe of word count
    stemm_word_count = pd.Series(stemm_words_list).value_counts().reset_index()
    stemm_word_count.columns=['word','count']

    # drop non-words
    stemm_word_count = stemm_word_count.drop([0,4,7])

    stemm_top_10_words = stemm_word_count.head(10)

    return stemm_words, stemm_top_10_words


def lemm_top_ten_words(df):
    '''
    This function takes cleaned lemmed column from the df and joins them to make a string. 
    It splits the string by space to produce a list that then produces a value_counts df.
    '''

    # join rows of string together
    lemm_words = ' '.join(df.clean_lemmatized)

    # split string by space to isolate words
    lemm_words_list = lemm_words.split()

    # create dataframe of word count
    lemm_word_count = pd.Series(lemm_words_list).value_counts().reset_index()
    lemm_word_count.columns=['word','count']

    # drop non-words
    lemm_word_count = lemm_word_count.drop([0,2,5,12])

    lemm_top_10_words = lemm_word_count.head(10)

    return lemm_top_10_words, lemm_words


def stemm_top_ten(stemm_top_10_words):
    '''
    This function creates barplot of the top ten most used stemmatized words
    '''
    # plot bar graph for top 10 words
    sns.barplot(data=stemm_top_10_words, x='count', y='word')
    plt.title('Top 10 Most Common Stemmed words')
    plt.show()


def lemm_top_ten(lemm_top_10_words):
    '''
    This function creates barplot of the top ten most used lemmatized words
    '''
    # plot bar graph for top 10 words
    sns.barplot(data=lemm_top_10_words, x='count', y='word')
    plt.title('Top 10 Most Common Lemmatized words')
    plt.show()


def stemm_wordcloud(stemm_words):
    '''
    This fuction prouces a word cloud from the stemm words column
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
    This functino produces a word cloud from the lemmatized words
    '''
    # create word cloud image
    img = WordCloud(background_color='white').generate(lemm_words)
    # axis aren't very useful for a word cloud
    plt.axis('off')
    # WordCloud() produces an image object, which can be displayed with plt.imshow
    plt.imshow(img)
    plt.show()
# kan end
