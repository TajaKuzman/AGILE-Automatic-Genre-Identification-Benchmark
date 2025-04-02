# AGILE - Automatic Genre Identification Benchmark

A benchmark for evaluating robustness of automatic genre identification models to test their usability for the automatic enrichment of large text collections with genre information.

The benchmark is based on two manually-annotated test datasets:
- English EN-GINCO test dataset
- X-GINCO test dataset in 10 European languages: Albanian, Catalan, Croatian, Greek, Icelandic, Macedonian, Maltese, Slovenian, Turkish, and Ukrainian

Both datasets are available upon request - please write to taja.kuzman@ijs.si to get access to private GitHub repositories where they are deposited.

The datasets are not publicly available to prevent exposure to LLM models which would make any further evaluation of the capabilities of generative large language models on this test set unreliable. If you wish to contribute to the benchmark, the test datasets will be shared with you upon request.

The X-GENRE classifier, which is state-of-the-art for this task, is freely available at the HuggingFace repository: https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier

The test datasets follow the same structure and genre schema as the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) on which the X-GENRE classifier and other neural and non-neural classifiers were trained on.

The code for all evaluated models is available in the [systems](systems) directory.

## Benchmark scores

Benchmark scores were calculated only once per system. Fine-tuning hyperparameters are listed in the json submission files, where applicable.

### EN-GINCO

All models that were not used in a zero-shot scenario were trained on the train split of the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) which comprises manually-annotated instances in Slovenian and English language. As the EN-GINCO test dataset comprises English instances, the performance of the trained models is observed in a cross-dataset scenario.

The performance on EN-GINCO is generally lower than on X-GINCO datasets, because X-GINCO datasets contain only concrete labels, while EN-GINCO also has instances annotated as "Other".

Performance of the models on the English test dataset:

| Model                    | Test Dataset   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|-----------:|----------------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | en-ginco       |      0.687 |      0.684 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | en-ginco       |      0.62  |      0.735 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | en-ginco       |      0.545 |      0.588 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | en-ginco       |      0.534 |      0.632 |
| Support Vector Machine                      | en-ginco       |      0.514 |      0.489 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | en-ginco       |      0.494 |      0.625 |
| Logistic Regression       | en-ginco       |      0.464 |      0.471 |
| fastText                 | en-ginco       |      0.408 |      0.445 |
| Naive Bayes             | en-ginco       |      0.289 |      0.36  |
| Dummy classifier (stratified)         | en-ginco       |      0.088 |      0.154 |
| Dummy classifier (most frequent)      | en-ginco       |      0.032 |      0.169 |

### X-GINCO

All models that were not used in a zero-shot scenario were trained on the train split of the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) which comprises manually-annotated instances in Slovenian and English language. The models are evaluated on a multilingual test dataset that comprises instances in Albanian, Catalan, Croatian, Greek, Icelandic, Macedonian, Maltese, Slovenian, Turkish, and Ukrainian, which means that for all languages except Slovenian the models are evaluated in a zero-shot cross-lingual scenario.

Performance of the models on the multilingual test dataset:

| Model                    | Test Dataset   |   Macro F1 |   Micro F1 | 
|:-------------------------|:---------------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        |      0.847 |      0.845 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        |      0.776 |      0.769 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        |      0.688 |      0.67  |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        |      0.651 |      0.652 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        |      0.627 |      0.622 |
| Logistic Regression       | x-ginco        |      0.174 |      0.185 |
| Support Vector Machine                      | x-ginco        |      0.166 |      0.184 |
| fastText                 | x-ginco        |      0.156 |      0.179 |
| Naive Bayes             | x-ginco        |      0.143 |      0.171 |
| Dummy classifier (stratified)         | x-ginco        |      0.106 |      0.113 |
| Dummy classifier (most frequent)      | x-ginco        |      0.029 |      0.133 |

### Performance on each language

The models are evaluated on EN-GINCO and X-GINCO test datasets that comprise instances in Albanian, Catalan, Croatian, Greek, English, Icelandic, Macedonian, Maltese, Slovenian, Turkish, and Ukrainian, which means that for all languages except Slovenian and English, the models are evaluated in a zero-shot cross-lingual scenario, since they have been trained on an English-Slovenian training dataset (X-GENRE dataset).


#### Albanian

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Albanian   |      0.854 |      0.85  |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Albanian   |      0.771 |      0.767 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Albanian   |      0.769 |      0.762 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Albanian   |      0.709 |      0.728 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Albanian   |      0.665 |      0.675 |
| Dummy classifier (stratified)         | x-ginco        | Albanian   |      0.097 |      0.102 |
| Naive Bayes             | x-ginco        | Albanian   |      0.088 |      0.151 |
| Logistic Regression       | x-ginco        | Albanian   |      0.058 |      0.15  |
| Support Vector Machine                      | x-ginco        | Albanian   |      0.057 |      0.1   |
| fastText                 | x-ginco        | Albanian   |      0.024 |      0.062 |
| Dummy classifier (most frequent)      | x-ginco        | Albanian   |      0.023 |      0.1   |

------------------------------------------

#### Catalan

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Catalan    |      0.786 |      0.785 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Catalan    |      0.769 |      0.75  |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Catalan    |      0.701 |      0.688 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Catalan    |      0.662 |      0.642 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Catalan    |      0.658 |      0.654 |
| Dummy classifier (stratified)         | x-ginco        | Catalan    |      0.146 |      0.139 |
| Naive Bayes             | x-ginco        | Catalan    |      0.1   |      0.221 |
| Support Vector Machine                      | x-ginco        | Catalan    |      0.077 |      0.112 |
| Logistic Regression       | x-ginco        | Catalan    |      0.063 |      0.138 |
| fastText                 | x-ginco        | Catalan    |      0.063 |      0.138 |
| Dummy classifier (most frequent)      | x-ginco        | Catalan    |      0.02  |      0.088 |

------------------------------------------

#### Croatian

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Croatian   |      0.894 |      0.9   |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Croatian   |      0.783 |      0.8   |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Croatian   |      0.616 |      0.632 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Croatian   |      0.592 |      0.575 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Croatian   |      0.571 |      0.581 |
| Support Vector Machine                      | x-ginco        | Croatian   |      0.197 |      0.241 |
| fastText                 | x-ginco        | Croatian   |      0.169 |      0.266 |
| Naive Bayes             | x-ginco        | Croatian   |      0.139 |      0.214 |
| Logistic Regression       | x-ginco        | Croatian   |      0.117 |      0.155 |
| Dummy classifier (stratified)         | x-ginco        | Croatian   |      0.055 |      0.064 |
| Dummy classifier (most frequent)      | x-ginco        | Croatian   |      0.025 |      0.112 |

------------------------------------------

#### English

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | en-ginco       | English    |      0.687 |      0.684 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | en-ginco       | English    |      0.62  |      0.735 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | en-ginco       | English    |      0.545 |      0.588 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | en-ginco       | English    |      0.534 |      0.632 |
| Support Vector Machine                      | en-ginco       | English    |      0.514 |      0.489 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | en-ginco       | English    |      0.494 |      0.625 |
| Logistic Regression       | en-ginco       | English    |      0.464 |      0.471 |
| fastText                 | en-ginco       | English    |      0.408 |      0.445 |
| Naive Bayes             | en-ginco       | English    |      0.289 |      0.36  |
| Dummy classifier (stratified)         | en-ginco       | English    |      0.088 |      0.154 |
| Dummy classifier (most frequent)      | en-ginco       | English    |      0.032 |      0.169 |

------------------------------------------

#### Greek

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Greek      |      0.783 |      0.8   |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Greek      |      0.74  |      0.762 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Greek      |      0.739 |      0.762 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Greek      |      0.716 |      0.718 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Greek      |      0.629 |      0.637 |
| Logistic Regression       | x-ginco        | Greek      |      0.223 |      0.238 |
| Support Vector Machine                      | x-ginco        | Greek      |      0.159 |      0.175 |
| Dummy classifier (stratified)         | x-ginco        | Greek      |      0.112 |      0.114 |
| fastText                 | x-ginco        | Greek      |      0.095 |      0.138 |
| Naive Bayes             | x-ginco        | Greek      |      0.093 |      0.138 |
| Dummy classifier (most frequent)      | x-ginco        | Greek      |      0.028 |      0.125 |

------------------------------------------

#### Icelandic

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Icelandic  |      0.795 |      0.8   |
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Icelandic  |      0.775 |      0.78  |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Icelandic  |      0.58  |      0.584 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Icelandic  |      0.556 |      0.584 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Icelandic  |      0.541 |      0.512 |
| Dummy classifier (stratified)         | x-ginco        | Icelandic  |      0.145 |      0.167 |
| Logistic Regression       | x-ginco        | Icelandic  |      0.075 |      0.113 |
| Support Vector Machine                      | x-ginco        | Icelandic  |      0.073 |      0.138 |
| Naive Bayes             | x-ginco        | Icelandic  |      0.059 |      0.169 |
| fastText                 | x-ginco        | Icelandic  |      0.052 |      0.105 |
| Dummy classifier (most frequent)      | x-ginco        | Icelandic  |      0.033 |      0.15  |

------------------------------------------

#### Macedonian

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Macedonian |      0.911 |      0.912 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Macedonian |      0.722 |      0.738 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Macedonian |      0.637 |      0.675 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Macedonian |      0.615 |      0.6   |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Macedonian |      0.594 |      0.615 |
| Naive Bayes             | x-ginco        | Macedonian |      0.144 |      0.164 |
| Logistic Regression       | x-ginco        | Macedonian |      0.099 |      0.125 |
| fastText                 | x-ginco        | Macedonian |      0.094 |      0.15  |
| Support Vector Machine                      | x-ginco        | Macedonian |      0.067 |      0.138 |
| Dummy classifier (stratified)         | x-ginco        | Macedonian |      0.065 |      0.065 |
| Dummy classifier (most frequent)      | x-ginco        | Macedonian |      0.033 |      0.15  |

------------------------------------------

#### Maltese

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Maltese    |      0.545 |      0.786 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Maltese    |      0.527 |      0.791 |
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Maltese    |      0.509 |      0.574 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Maltese    |      0.379 |      0.522 |
| fastText                 | x-ginco        | Maltese    |      0.101 |      0.177 |
| Dummy classifier (stratified)         | x-ginco        | Maltese    |      0.1   |      0.132 |
| Naive Bayes             | x-ginco        | Maltese    |      0.092 |      0.1   |
| Support Vector Machine                      | x-ginco        | Maltese    |      0.075 |      0.2   |
| Logistic Regression       | x-ginco        | Maltese    |      0.073 |      0.071 |
| Dummy classifier (most frequent)      | x-ginco        | Maltese    |      0.053 |      0.229 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Maltese    |      0     |      0     |

------------------------------------------

#### Slovenian

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Slovenian  |      0.936 |      0.938 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Slovenian  |      0.695 |      0.7   |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Slovenian  |      0.679 |      0.684 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Slovenian  |      0.67  |      0.662 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Slovenian  |      0.642 |      0.646 |
| Logistic Regression       | x-ginco        | Slovenian  |      0.563 |      0.561 |
| Support Vector Machine                      | x-ginco        | Slovenian  |      0.483 |      0.494 |
| fastText                 | x-ginco        | Slovenian  |      0.422 |      0.436 |
| Naive Bayes             | x-ginco        | Slovenian  |      0.214 |      0.3   |
| Dummy classifier (stratified)         | x-ginco        | Slovenian  |      0.128 |      0.143 |
| Dummy classifier (most frequent)      | x-ginco        | Slovenian  |      0.028 |      0.125 |

------------------------------------------

#### Turkish

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Turkish    |      0.916 |      0.917 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Turkish    |      0.815 |      0.812 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Turkish    |      0.729 |      0.712 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Turkish    |      0.71  |      0.721 |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Turkish    |      0.683 |      0.697 |
| Dummy classifier (stratified)         | x-ginco        | Turkish    |      0.129 |      0.14  |
| Logistic Regression       | x-ginco        | Turkish    |      0.096 |      0.125 |
| Naive Bayes             | x-ginco        | Turkish    |      0.094 |      0.126 |
| Support Vector Machine                      | x-ginco        | Turkish    |      0.093 |      0.138 |
| fastText                 | x-ginco        | Turkish    |      0.092 |      0.126 |
| Dummy classifier (most frequent)      | x-ginco        | Turkish    |      0.03  |      0.138 |

------------------------------------------

#### Ukrainian

| Model                    | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:-------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)       | x-ginco        | Ukrainian  |      0.945 |      0.949 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)        | x-ginco        | Ukrainian  |      0.782 |      0.775 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual) (zero-shot) | x-ginco        | Ukrainian  |      0.769 |      0.784 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)   | x-ginco        | Ukrainian  |      0.663 |      0.65  |
| GPT-3.5-Turbo (gpt-3.5-turbo-0125) (zero-shot)       | x-ginco        | Ukrainian  |      0.589 |      0.6   |
| Logistic Regression       | x-ginco        | Ukrainian  |      0.121 |      0.162 |
| fastText                 | x-ginco        | Ukrainian  |      0.117 |      0.184 |
| Naive Bayes             | x-ginco        | Ukrainian  |      0.08  |      0.125 |
| Support Vector Machine                      | x-ginco        | Ukrainian  |      0.058 |      0.112 |
| Dummy classifier (stratified)         | x-ginco        | Ukrainian  |      0.056 |      0.064 |
| Dummy classifier (most frequent)      | x-ginco        | Ukrainian  |      0.028 |      0.125 |

------------------------------------------


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
