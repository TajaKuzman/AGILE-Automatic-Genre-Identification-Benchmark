# AGILE - Automatic Genre Identification Benchmark

A benchmark for evaluating robustness of automatic genre identification models to test their usability for the automatic enrichment of large text collections with genre information. The benchmark is based on manually-annotated English EN-GINCO test dataset.

More information on the dataset and the X-GENRE classifier can be found in [`Automatic Genre Identification for Robust Enrichment of Massive Text Collections: Investigation of Classification Methods in the Era of Large Language Models` (Kuzman et al., 2023)](https://www.mdpi.com/2504-4990/5/3/59).

The X-GENRE classifier, which is state-of-the-art for this task, is freely available at the HuggingFace repository: https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier

The test dataset follows the same structure and genre schema as the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-multilingual-text-genre-dataset) on which the X-GENRE classifier was fined-tuned on.

The EN-GINCO dataset is not publicly available to prevent exposure to LLM models which would make any further evaluation of the capabilities of generative large language models on this test set unreliable. If you wish to contribute to the benchmark, the test dataset will be shared with you upon request.

## Benchmark scores

Benchmark scores were calculated only once per system. Fine-tuning hyperparameters are listed in the json submission files, where applicable.

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

## Dataset Details

The EN-GINCO dataset is a sample of the English [enTenTen20](https://www.sketchengine.eu/ententen-english-corpus/) corpus
that was manually annotated with genres by two expert annotators who previously annotated the Slovenian [GINCO](https://www.clarin.si/repository/xmlui/handle/11356/1467) dataset ([Kuzman et al., 2022](https://aclanthology.org/2022.lrec-1.170.pdf)), and to which the [X-GENRE schema](https://huggingface.co/datasets/TajaKuzman/X-GENRE-multilingual-text-genre-dataset#genre-labels) was mapped.

The dataset consists of around 300 texts and 100.000 words.

| dataset | # words | # texts |
|:---|---:|---:|
| EN-GINCO | 105,331 | 272 |

The texts are annotated with the following 8 genre labels:

```
labels_list=['Other', 'Information/Explanation', 'News', 'Instruction', 'Opinion/Argumentation', 'Forum', 'Prose/Lyrical', 'Legal', 'Promotion']
```

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
- a table with the results `results/results-en-ginco.md`
