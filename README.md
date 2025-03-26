# AGILE - Automatic Genre Identification Benchmark

A benchmark for evaluating robustness of automatic genre identification models to test their usability for the automatic enrichment of large text collections with genre information.

The benchmark is based on two manually-annotated test datasets:
- English EN-GINCO test dataset
- X-GINCO test dataset in 10 European languages: Albanian, Catalan, Croatian, Greek, Icelandic, Macedonian, Maltese, Slovenian, Turkish, and Ukrainian

Both datasets are available upon request - please write to taja.kuzman@ijs.si to get access to private GitHub repositories where they are deposited.

The datasets are not publicly available to prevent exposure to LLM models which would make any further evaluation of the capabilities of generative large language models on this test set unreliable. If you wish to contribute to the benchmark, the test datasets will be shared with you upon request.

The X-GENRE classifier, which is state-of-the-art for this task, is freely available at the HuggingFace repository: https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier

The test datasets follow the same structure and genre schema as the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) on which the X-GENRE classifier and other neural and non-neural classifiers were trained on.

## Benchmark scores

Benchmark scores were calculated only once per system. Fine-tuning hyperparameters are listed in the json submission files, where applicable.

### EN-GINCO

All models that were not used in a zero-shot scenario were trained on the train split of the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) which comprises manually-annotated instances in Slovenian and English language. As the EN-GINCO test dataset comprises English instances, the performance of the trained models is observed in a cross-dataset scenario. In contrast, the performance of the models that have not been trained on the dataset (GPT models, mt0 model and `mDeBERTa-v3-base-mnli-xnli` model) is observed in a zero-shot scenario.

Performance of the models on the English test dataset:

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

### X-GINCO

All models that were not used in a zero-shot scenario were trained on the train split of the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) which comprises manually-annotated instances in Slovenian and English language. The models are evaluated on a multilingual test dataset that comprises instances in Albanian, Catalan, Croatian, Greek, Icelandic, Macedonian, Maltese, Slovenian, Turkish, and Ukrainian, which means that for all languages except Slovenian the models are evaluated in a zero-shot cross-lingual scenario.

Performance of the models on the multilingual test dataset:

| Model               | Test Dataset   |   Macro F1 |   Micro F1 | Epochs   | Learning Rate   |
|:--------------------|:---------------|-----------:|-----------:|:---------|:----------------|
| Logistic Regression  | x-ginco        |      0.174 |      0.185 |          |                 |
| SVC                 | x-ginco        |      0.166 |      0.184 |          |                 |
| Naive Bayes        | x-ginco        |      0.143 |      0.171 |          |                 |
| Dummy (stratified)    | x-ginco        |      0.106 |      0.113 |          |                 |
| Dummy (most frequent) | x-ginco        |      0.029 |      0.133 |          |                 |

### Performance on each language

The models are evaluated on EN-GINCO and X-GINCO test datasets that comprise instances in Albanian, Catalan, Croatian, Greek, English, Icelandic, Macedonian, Maltese, Slovenian, Turkish, and Ukrainian, which means that for all languages except Slovenian and English, the models are evaluated in a zero-shot cross-lingual scenario, since they have been trained on an English-Slovenian training dataset (X-GENRE dataset).

#### Albanian

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| Dummy (stratified)    | x-ginco        | Albanian   |      0.097 |      0.102 |
| Naive Bayes        | x-ginco        | Albanian   |      0.088 |      0.151 |
| Logistic Regression  | x-ginco        | Albanian   |      0.058 |      0.15  |
| SVC                 | x-ginco        | Albanian   |      0.057 |      0.1   |
| Dummy (most frequent) | x-ginco        | Albanian   |      0.023 |      0.1   |


#### Catalan

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| Dummy (stratified)    | x-ginco        | Catalan    |      0.146 |      0.139 |
| Naive Bayes        | x-ginco        | Catalan    |      0.1   |      0.221 |
| SVC                 | x-ginco        | Catalan    |      0.077 |      0.112 |
| Logistic Regression  | x-ginco        | Catalan    |      0.063 |      0.138 |
| Dummy (most frequent) | x-ginco        | Catalan    |      0.02  |      0.088 |


#### Croatian

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| SVC                 | x-ginco        | Croatian   |      0.197 |      0.241 |
| Naive Bayes        | x-ginco        | Croatian   |      0.139 |      0.214 |
| Logistic Regression  | x-ginco        | Croatian   |      0.117 |      0.155 |
| Dummy (stratified)    | x-ginco        | Croatian   |      0.055 |      0.064 |
| Dummy (most frequent) | x-ginco        | Croatian   |      0.025 |      0.112 |


#### English

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| SVC                 | en-ginco       | English    |      0.514 |      0.489 |
| Logistic Regression  | en-ginco       | English    |      0.464 |      0.471 |
| Naive Bayes        | en-ginco       | English    |      0.289 |      0.36  |
| Dummy (stratified)    | en-ginco       | English    |      0.088 |      0.154 |
| Dummy (most frequent) | en-ginco       | English    |      0.032 |      0.169 |


#### Greek

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| Logistic Regression  | x-ginco        | Greek      |      0.223 |      0.238 |
| SVC                 | x-ginco        | Greek      |      0.159 |      0.175 |
| Dummy (stratified)    | x-ginco        | Greek      |      0.112 |      0.114 |
| Naive Bayes        | x-ginco        | Greek      |      0.093 |      0.138 |
| Dummy (most frequent) | x-ginco        | Greek      |      0.028 |      0.125 |


#### Icelandic

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| Dummy (stratified)    | x-ginco        | Icelandic  |      0.145 |      0.167 |
| Logistic Regression  | x-ginco        | Icelandic  |      0.075 |      0.113 |
| SVC                 | x-ginco        | Icelandic  |      0.073 |      0.138 |
| Naive Bayes        | x-ginco        | Icelandic  |      0.059 |      0.169 |
| Dummy (most frequent) | x-ginco        | Icelandic  |      0.033 |      0.15  |


#### Macedonian

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| Naive Bayes        | x-ginco        | Macedonian |      0.144 |      0.164 |
| Logistic Regression  | x-ginco        | Macedonian |      0.099 |      0.125 |
| SVC                 | x-ginco        | Macedonian |      0.067 |      0.138 |
| Dummy (stratified)    | x-ginco        | Macedonian |      0.065 |      0.065 |
| Dummy (most frequent) | x-ginco        | Macedonian |      0.033 |      0.15  |


#### Maltese

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| Dummy (stratified)    | x-ginco        | Maltese    |      0.1   |      0.132 |
| Naive Bayes        | x-ginco        | Maltese    |      0.092 |      0.1   |
| SVC                 | x-ginco        | Maltese    |      0.075 |      0.2   |
| Logistic Regression  | x-ginco        | Maltese    |      0.073 |      0.071 |
| Dummy (most frequent) | x-ginco        | Maltese    |      0.053 |      0.229 |


#### Slovenian

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| Logistic Regression  | x-ginco        | Slovenian  |      0.563 |      0.561 |
| SVC                 | x-ginco        | Slovenian  |      0.483 |      0.494 |
| Naive Bayes        | x-ginco        | Slovenian  |      0.214 |      0.3   |
| Dummy (stratified)    | x-ginco        | Slovenian  |      0.128 |      0.143 |
| Dummy (most frequent) | x-ginco        | Slovenian  |      0.028 |      0.125 |


#### Turkish

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| Dummy (stratified)    | x-ginco        | Turkish    |      0.129 |      0.14  |
| Logistic Regression  | x-ginco        | Turkish    |      0.096 |      0.125 |
| Naive Bayes        | x-ginco        | Turkish    |      0.094 |      0.126 |
| SVC                 | x-ginco        | Turkish    |      0.093 |      0.138 |
| Dummy (most frequent) | x-ginco        | Turkish    |      0.03  |      0.138 |


#### Ukrainian

| Model               | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------|:---------------|:-----------|-----------:|-----------:|
| Logistic Regression  | x-ginco        | Ukrainian  |      0.121 |      0.162 |
| Naive Bayes        | x-ginco        | Ukrainian  |      0.08  |      0.125 |
| SVC                 | x-ginco        | Ukrainian  |      0.058 |      0.112 |
| Dummy (stratified)    | x-ginco        | Ukrainian  |      0.056 |      0.064 |
| Dummy (most frequent) | x-ginco        | Ukrainian  |      0.028 |      0.125 |


## Contributing to the benchmark

Should you wish to contribute an entry, feel free to submit a folder in the [systems](systems) directory with or without the code used (see the submission examples in the directory).

The results JSON file name should start with `submission-` and the content should be structured like this:

```python
{
    "system": "Pick a name for your system",
    "predictions": [
        {   "train": "what you trained on", # e.g. "X-GENRE-train (train split)"
            "test": "what you evaluated on", # should be "en-ginco"
            "predictions": [....] # The length of predictions should match the length of test data
        },
    ],
    # Additional information, e.g. fine-tuning params:
    "model": "EMBEDDIA/crosloengual-bert",
    "lr": "4e-5",
    "epoch": "15"
}
```

All submission JSON files should be saved in a `submissions` directory inside the directory for your system. They will be evaluated against the datasets in the `data/datasets` directory.

It is highly encouraged that you also provide additional information about your system in a README file, and that you provide the code used for the classification with the system.

## Evaluation

Micro and Macro F1 scores will be used to evaluate and compare systems.

The submissions are evaluated using the following code with the path to the submissions directory (e.g., ``systems/dummy-classifier/submissions``) as the argument. The log file is to be saved in the relevant system directory:
```python eval.py "submission-path" > systems/dummy-classifier/evaluation.log```

The code produces:
- a JSON file with the results of all tested models: `results/results.json`
- a table with the results, e.g. `results/results-en-ginco.md`
