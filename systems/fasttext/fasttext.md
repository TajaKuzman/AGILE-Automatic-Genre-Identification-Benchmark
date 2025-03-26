# Prediction with the fastText model

FastText is a shallow neural model which has one hidden layer, where the word embeddings are created and averaged into a text representation. The document representation is then fed into a linear classifier, which predicts the genre labels.

For our experiments, we train the fastText model on the Slovenian-English [X-GENRE genre training dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset). 

## Hyperparameters

We use the following hyperparameters based on the hyperparameter search described in [Kuzman et al., 2023](https://www.mdpi.com/2504-4990/5/3/59):
```python
epoch = 350
wordNgrams=1
```