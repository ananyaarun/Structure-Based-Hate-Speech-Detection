# Structure-Based-Hate-Speech-Detection
## IRE Major Project

### Team 26
- Ananya Arun
- Vijayraj S
- Sumit Bhuin
- Virat Mishra

### Problem statement 

The main objective of our project is “Structure-based hate speech detection”.  
Traditional methods for hate speech detection use tons of training data to mine the hateful structure but due to disproportionate use of different terms, they are prone towards learning bias against specific objects, personalities or groups. 
Idea is to propose a method that takes into account the grammatical structure of the sentence to predict hatefulness.


### Preprocessing

We preprocessed the dataset (https://www.aclweb.org/anthology/W18-5102/) into three different types.
The first dataset is basically hate speech and non hate speech tagged sentences.
For the second one we also did a part of speech tagging (POS tagging).
The third dataset has been stemmed (individual words were stemmed) and POS tagging was done on top of that.

### Analysis

We built 4 baseline models for our reference and analysis which include 
- Naive Bayes
- SVM
- Logistic regression
- Decision Trees

### Results

- For Naive Bayes we obtained the following Accuraries, F1, Precision and Recall.

| Dataset  | Accuracy  | F1  | Presicion  |  Recall |
|---|---|---|---|---|
| Normal Tagged  |  0.8780264961169484 | 0.5777016701529257  | 0.7493289048637335  | 0.5613263501868887  |
| POS tagged  | 0.8793969849246231  | 0.5673913043478261  | 0.7787907686439062  | 0.554525989092564  |
| POS + stemming  | 0.8784833257195066  | 0.5566990687447849  | 0.7784954160254882  | 0.5479326603848191  |

- For SVM we obtained the following Accuraries, F1, Precision and Recall.

| Dataset  | Accuracy  | F1  | Presicion  |  Recall |
|---|---|---|---|---|
| Normal Tagged  | 0.8725445408862494  | 0.47644373577481447  | 0.8113844393592677  | 0.5050760237844775  |
| POS tagged  | 0.8725445408862494 | 0.4730012037432532  | 0.9362139917695473  | 0.50355871886121  |
| POS + stemming  | 0.8725445408862494  | 0.47644373577481447  | 0.8113844393592677  | 0.5050760237844775 |



- For Logistic regression we obtained the following Accuraries, F1, Precision and Recall.

| Dataset  | Accuracy  | F1  | Presicion  |  Recall |
|---|---|---|---|---|
| Normal Tagged  | 0.8766560073092736  | 0.6367095298977183  | 0.7201042372243547  | 0.6090939442094347  |
| POS tagged  |0.8734582000913659  | 0.5960676159547006  | 0.7052683694713857  | 0.5753961592694554  |
| POS + stemming  | 0.8743718592964824  | 0.6191133324095499  | 0.7098678410432989  | 0.59412792736334  |


- For Decision Trees we obtained the following Accuraries, F1, Precision and Recall.

| Dataset  | Accuracy  | F1  | Presicion  |  Recall |
|---|---|---|---|---|
| Normal Tagged  | 0.8579259936043856  | 0.6394379549866136  | 0.6643687953770929  | 0.6241438931041429  |
| POS tagged  | 0.8579259936043856 | 0.596474256954484  | 0.6440535339515485  | 0.5801420503293866  |
| POS + stemming  | 0.8542713567839196  | 0.6247314965737432  | 0.6508532414471057  | 0.6099090176593029 |


### CNN

We also built a CNN model with word embedding.
The accuracies obtained here were as follows -

- Normal tagged - 0.7957038391224863
- POS tagged - 0.8281467719461217
- Stemmed and POS tagged - 0.8367626886145405


### LSTM

In the LSTM model we built with word embedding,
The accuracies obtained were as follows -

- Normal tagged - 0.8386654478976234
- POS tagged - 0.8137482582443103
- Stemmed and POS tagged - 0.8454503886602652

### Observations

- Since the dataset we used was skewed. That is most of the sentences were tagged as non hate speech, the accuracies obtained with almost all the baseline models were in the range 85-88 percent.
- However the F1 precision and recall scores were different as expected due to different models.

### Goals 

- For the final phase we plan to experiment with more models.
- We shall implement Tree lstms and n gram based models.
- We shall also try different datasets and other structure and semantic based analysis.
