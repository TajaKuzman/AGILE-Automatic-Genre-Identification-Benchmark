# Classification with Non-Neural Classifiers

We train the models on the X-GENRE dataset (1772 instances in English and Slovenian). The texts are represented using the TD-IDF representation (created with TfidfVectorizer from the Scikit-Learn library).

We use the following models, provided through the Scikit-Learn library:
-  Naive Bayes Classifier: This probabilistic machine learning algorithm learns the statistical relationships between the words present in the documents, taking into account also their frequency, and the corresponding genre categories. We use the Complement Naive Bayes implementation, which is especially suitable for imbalanced multi-class datasets. 
-  Logistic Regression Classifier: This algorithm models the relationship between the features (words) and the probability of belonging to a category using a logistic function. The cross-entropy loss is used to determine the most probable class. We use the implementation based on the limited-memory BFGS (L-BFGS) solver, which is suitable for addressing the complexities of a multi-class classification. 
-  Support Vector Machine (SVM): the SVM model is a linear classifier that determines the boundaries between classes in form of a separating hyperplane. Its efficacy is particularly notable in high-dimensional spaces, making it highly applicable in the context of text categorization tasks, where the feature set can encompass the entire dataset vocabulary. SVMs were successfully applied in multiple automatic genre identification studies, achieving up to 0.75 in micro F1 on the subset of the CORE dataset. In this study, we employ the SVC implementation with the linear kernel, which supports multi-class categorization.

Hyperparameters:
- Naive Bayes: ComplementNB model with the default hyperparameters.
- Logistic Regression: penalty set to None, as preliminary experiments showed that disabling regularization improves the results in our case.
- SVM: SVC model with the linear kernel and the regularization parameter C set to 2.

Code: *non-neural-classifiers.ipynb*