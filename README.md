# Natural Language Processing Project 

## This file/repo contains information related to our nlp project, using scraped data from git hub repositories


## Project Goals
Our overall goal is to identify key words among a variation of REPOs on Guthub and create a model to predict what programming language that a repository is based on the text included in the README files.

## Project Description
In this project, we will utilize the text in README files of 130 repositories that relate to health, explore initial questions and find common words that have a correlation to various programming languages.  We will use machine learning to create a classification model that predicts what programming language a repository is, depending on what text is included in the README file.


## The Plan

**Plan - Acquire - Prepare - Explore - Model - Deliver**

- Wrangle
    - Acquire data via webscraping Github through class provided script
    - Prepare data by creating basic clean functions such as tokenize, removing stopwords, lemmatize
    - We will create a function that we can reference later to acquire and prepare the data by storing the function in a file name wrangle.py
    - We will split our data to a train, validate, and test
- Explore
    - Create visualizations of data to pin point key text words that correllate to programming languages
    - Create a visualizations correlating to hypotheses statements
    - Run statistical tests that will support whether the hypothesis has been rejected or not
    - Create explore.py file to will store visualizations needed for final report
- Modeling
    - Establish baseline
    - Ensure models are tested on appropriate validate and test datasets
    - Determine best performing model and test on test dataset
- Delivery
    - README with project details
    - Python modules with acquire and prepare functions
    - Final Report in Jupyter Notebook
    - Presentation with slide show entailing executive summary details





 
## Initial Questions

- What are the most common words in READMEs?

- What does the distribution of IDFs look like for the most common words?

- Does the length of the README vary by programming language?

- Do different programming languages use a different number of unique words?




##  Steps to Reproduce
- Clone my repo (including an acquire.py and prepare.py) (confirm .gitignore is hiding your env.py file)
- Libraries used are pandas, matplotlib, seaborn, numpy, sklearn.
- Document conclusions, takeaways, and next steps in the Final Report Notebook.





## Data Dictionary

 

| Variable          | Description                                                  |Data types|
| ----------------- | -----------------------------------------------------------  |----------|
| language          |The programming language the README is in                     |          |
| readme_contents   |The text included in each README                              |          |
| clean             |Clean Version of the README contents                          |          |
| clean_stemmed     |The contents of the README that has been stemmed              |          |
| clean_lemmatized  |The contents of the README that has been lemmatized           |          |
| 
 
## Key findings, recommendations and takeaways
- There are significant differences between the mean length of each README per programming language.
- There are significant differences between the mean of the amount of unique words in each README per programming language.
- While the Logistic Regression did better than the Random Forest Classifier on stemmed README's, it was the opposite for lemmatized README's.
- Logistic Regression and Random Forest Classifer are overfit.
- Decision Tree Classifier was overfit.
- The KNN Classifier was overfit by a smaller margin.
 

 
## Recommendations
- Scrape more data to build a more accurate model
 

## Next steps