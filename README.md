# Internship-Task
*First time with text!*

A text classifier which predicts the class of a paragraph of text.

Naive Bayes approach is used for predicting the class lable for the text. The classifier does not make use of a predefined scikit learn model, rather it uses a the inverse dictionary approach for predicting the class.

A dictionary is mantained for the the words of each class. The frequency of words is recorded from the sentence. The model checks for the class for which word occurance is maximum. This way a new sentence is labeled under a class.
