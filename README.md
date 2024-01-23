# AGILE - Automatic Genre Identification Benchmark

A benchmark for evaluating robustness of automatic genre identification models to test their usability for the automatic enrichment of large text collections with genre information.

The benchmark consists of 2 test datasets, manually-annotated with genre (see more details in Section [Datasets](#datasets)):
- EN-GINCO: English genre dataset
- X-GENRE test: test split of the Slovenian-English manually-annotated genre dataset X-GENRE, which was used for fine-tuning the XLM-RoBERTa-based X-GENRE classifier

More information on the datasets and the X-GENRE classifier can be found in [`Automatic Genre Identification for Robust Enrichment of Massive Text Collections: Investigation of Classification Methods in the Era of Large Language Models` (Kuzman et al., 2023)](https://www.mdpi.com/2504-4990/5/3/59).

The X-GENRE classifier, which is state-of-the-art for this task, is freely available at the HuggingFace repository: https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier

## Benchmark scores

Benchmark scores were calculated only once per system. Fine-tuning hyperparameters are listed in the json submission files, where applicable.

### EN-GINCO

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

### X-GENRE-test


## Datasets

The datasets for training and testing the models are available for download on Hugging Face: https://huggingface.co/datasets/TajaKuzman/X-GENRE-multilingual-text-genre-dataset

To download them:
```python
from datasets import load_dataset

train = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "train")
test = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "test")
dev = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "dev")
EN_GINCO = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "EN-GINCO")

# To open them as Pandas DataFrame:
train_df = pd.DataFrame(train["train"])
```


 **Dataset sizes**

Dataset sizes in number of instances (texts) and words:

Dataset sizes:

| dataset | # words | # texts |
|---|---|---|
| X-GENRE-train | 1,940,317 | 1,772 |
| X-GENRE-test | 583,595 | 592 |
| X-GENRE-dev | 798,025 | 592 |
| EN-GINCO | 105,331 | 272 |
| **Total** | **3,427,268** | **3,228** |

The attributes in datasets are the following:
- text: text instance
- labels: genre label
- dataset: original manually-annotated genre dataset from which the text was obtained (CORE, GINCO, FTD or EN-GINCO)
- language: language of the text (Slovenian or English)
- length: the length of the text in number of words


labels_list=['Other', 'Information/Explanation', 'News', 'Instruction', 'Opinion/Argumentation', 'Forum', 'Prose/Lyrical', 'Legal', 'Promotion']

See more details on the datasets here: https://huggingface.co/datasets/TajaKuzman/X-GENRE-multilingual-text-genre-dataset

An example of how to use the prepared datasets with the simpletransformers library:

```python
import pandas as pd
from datasets import load_dataset

# Get all the datasets from the HuggingFace
train = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "train")
test = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "test")
dev = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "dev")
EN_GINCO = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "EN-GINCO")

# To open them as Pandas DataFrame:
train_df = pd.DataFrame(train["train"])
test_df = pd.DataFrame(test["train"])
en_ginco = pd.DataFrame(EN_GINCO["train"])

print(train_df.shape, test_df.shape, en_ginco.shape)

```

## Contributing to the benchmark

Should you wish to contribute an entry, feel free to submit a folder in the [systems](systems) directory with or without the code used (see the submission examples in the directory).

The results JSON file name should start with `submission-` and the content should be structured like this:

```python
{
    "system": "Pick a name for your system",
    "predictions": [
        {   "train": "what you trained on", # e.g. "X-GENRE-train (train split)"
            "test": "what you evaluated on",# should be "x-genre-test" or "en-ginco"
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
- a table with the results for each of the datasets `results/results-en-ginco.md` and `results/results-x-genre-test.md`
