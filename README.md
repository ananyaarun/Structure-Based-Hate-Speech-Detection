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
| Normal Tagged  |   |   |   |   |
| POS tagged  |  |   |   |   |
| POS + stemming  |   |   |   |   |


- For Decision Trees we obtained the following Accuraries, F1, Precision and Recall.

| Dataset  | Accuracy  | F1  | Presicion  |  Recall |
|---|---|---|---|---|
| Normal Tagged  |   |   |   |   |
| POS tagged  |  |   |   |   |
| POS + stemming  |   |   |   |   |








 











