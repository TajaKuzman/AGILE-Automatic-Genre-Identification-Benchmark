# AGILE - Automatic Genre Identification Benchmark

A benchmark for evaluating robustness of automatic genre identification models to test their usability for the automatic enrichment of large text collections with genre information.

The benchmark is based on two manually-annotated test datasets:
- English EN-GINCO test dataset. The dataset used for evaluation (with label "Other" removed) consists of 258 text instances.
- X-GINCO test dataset in 10 European languages: Albanian, Catalan, Croatian, Greek, Icelandic, Macedonian, Maltese, Slovenian, Turkish, and Ukrainian. The dataset consists of around 800 texts (approximately 80 texts per language) and 210,000 words.

Both datasets are available upon request - please write to taja.kuzman@ijs.si to get access to private GitHub repositories where they are deposited.

The datasets are not publicly available to prevent exposure to LLM models which would make any further evaluation of the capabilities of generative large language models on this test set unreliable. If you wish to contribute to the benchmark, the test datasets will be shared with you upon request.

The X-GENRE classifier, which is state-of-the-art for this task, is freely available at the HuggingFace repository: https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier

The test datasets follow the same structure and genre schema as the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) on which the X-GENRE classifier and other neural and non-neural classifiers were trained on.

The code for all evaluated models is available in the [systems](systems) directory.

## Benchmark scores

Benchmark scores were calculated only once per system. Fine-tuning hyperparameters are listed in the json submission files, where applicable.

All models that were not used in a zero-shot scenario were trained on the train split of the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) which comprises manually-annotated instances in Slovenian and English language.

As the EN-GINCO test dataset comprises English instances, the performance of the trained models is observed in a cross-dataset scenario. We remove from the EN-GINCO instances that were manually-annotated as "Other" prior to calculating the final results, reported below, as the X-GINCO datasets do not have this label. This means, that models are evaluated only on the 8 concrete genre labels from the X-GENRE schema.

The models are evaluated on a multilingual X-GINCO test dataset that comprises instances in Albanian, Catalan, Croatian, Greek, Icelandic, Macedonian, Maltese, Slovenian, Turkish, and Ukrainian, which means that for all languages except Slovenian the models are evaluated in a zero-shot cross-lingual scenario.

![](evaluation-of-results/genre-results-heatmap.png)


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
