# AGILE - Automatic Genre Identification Benchmark

A benchmark for evaluating robustness of automatic genre identification models to test their usability for the automatic enrichment of large text collections with genre information.

Create a pull-request to request the dataset for testing.

## Leaderboard

|                             |   micro F1 |   macro F1 |   accuracy |
|:----------------------------|-----------:|-----------:|-----------:|
| **XLM-RoBERTa, fine-tuned on the X-GENRE dataset - X-GENRE classifier**  (Kuzman et al. 2023)                   |       0.68 |       0.69 |       0.68 |
| GPT-4 (7/7/2023)  (Kuzman et al. 2023)            |       0.65 |       0.55 |       0.65 |
| GPT-3.5-turbo (Kuzman et al. 2023)    |       0.63 |       0.53 |       0.63 |
| SVM  (Kuzman et al. 2023)                       |       0.49 |       0.51 |       0.49 |
| Logistic Regression (Kuzman et al. 2023)        |       0.49 |       0.47 |       0.49 |
| FastText (Kuzman et al. 2023)                   |       0.45 |       0.41 |       0.45 |
| Naive Bayes  (Kuzman et al. 2023)             |       0.36 |       0.29 |       0.36 |
| mt0                        |       0.32 |       0.23 |       0.27 |
| Zero-Shot classification with `MoritzLaurer/mDeBERTa-v3-base-mnli-xnli` @ HuggingFace                 |       0.2  |       0.15 |       0.2  |
| Dummy Classifier (stratified) (Kuzman et al. 2023)|       0.14 |       0.1  |       0.14 |

The X-GENRE classifier, which is state-of-the-art for this task, is freely available at the HuggingFace repository: https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier

## More information

More information on the datasets, used for the benchmark, and the models on the leaderboard can be found in:
[Kuzman et al., 2023 (in print)]()

## Documentation
- non-neural classifiers (SVM, Logistic Regression, Naive Bayes, Dummy classifier): *Code-and-documentation/non-neural-classifiers-Kuzman.md*