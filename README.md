# Structure-Based-Hate-Speech-Detection
## IRE Major Project

### Team 26
- Ananya Arun 
- Vijayraj S
- Sumit Bhuin
- Virat Mishra

### Abstract

The main objective of our project is “Structure-based hate speech detection”. Traditional methods for hate speech detection use tons of training data to mine the hateful structure but due to disproportionate use of different terms, they are prone towards learning bias against specific objects, personalities or groups. Idea is to propose a method that takes into account the grammatical structure of the sentence to predict hatefulness. 

Hate speech is commonly defined as any communication that disparages a person or a group on the basis of some characteristic such as race, colour, ethnicity, gender, sexual orientation, nationality, religion, or other characteristics. With the rise of social media and user generated content, detecting and classifying hate speech is becoming quite important. To automate the process of hate-speech detection, we look at a system that tries to utilize the grammatical structure of the system as features in order to classify a sentence as hate-speech or not, in order to avoid bias towards certain named entities.

### Datasets

First dataset being used is text extracted from Stormfront, a white supremacist forum. (https://github.com/Vicomtech/hate-speech-dataset). The dataset has 10495 sentences labelled either as hate or non-hate. We also used a second dataset (https://github.com/t-davidson/hate-speech-and-offensive-language) which was used in the paper Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017. "Automated Hate Speech Detection and the Problem of Offensive Language." ICWSM.  This consists of 25,297 tweets which have been labelled whether the tweet comes under hate-speech, uses offensive language or falls under neither of the two categories.

Forboth the datasets we ran all the models for both naive and oversampled data. To include structure based analysis we also ran our models after stemming and/or performing POS Tagging.

### Models Implemented

We built baseline models for our reference and analysis which include 
- Naive Bayes
- SVM
- Logistic Regression
- Decision Trees
- N Grams

The DL models we have implemented are 
- LSTM
- CNN
- BERT
- Tree LSTM

Complete results and analysis are avilable in our Report.
