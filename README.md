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

| Model                  |   Slovenian (macro-F1) |   Slovenian (micro-F1) |   Croatian (macro-F1) |   Croatian (micro-F1) |   Macedonian (macro-F1) |   Macedonian (micro-F1) |   Catalan (macro-F1) |   Catalan (micro-F1) |   Ukrainian (macro-F1) |   Ukrainian (micro-F1) |   Icelandic (macro-F1) |   Icelandic (micro-F1) |   Albanian (macro-F1) |   Albanian (micro-F1) |   Turkish (macro-F1) |   Turkish (micro-F1) |   Greek (macro-F1) |   Greek (micro-F1) |   Maltese (macro-F1) |   Maltese (micro-F1) |   English (macro-F1) |   English (micro-F1) |
|:-----------------------|-----------------------:|-----------------------:|----------------------:|----------------------:|------------------------:|------------------------:|---------------------:|---------------------:|-----------------------:|-----------------------:|-----------------------:|-----------------------:|----------------------:|----------------------:|---------------------:|---------------------:|-------------------:|-------------------:|---------------------:|---------------------:|---------------------:|---------------------:|
| X-GENRE classifier     |                  0.936 |                  0.938 |                 0.894 |                 0.9   |                   0.911 |                   0.913 |                0.788 |                0.788 |                  0.933 |                  0.938 |                  0.775 |                  0.78  |                 0.854 |                 0.85  |                0.911 |                0.913 |              0.802 |              0.818 |                0.51  |                0.58  |                0.752 |                0.71  |
| GPT-4o                 |                  0.695 |                  0.7   |                 0.783 |                 0.8   |                   0.722 |                   0.738 |                0.769 |                0.75  |                  0.782 |                  0.775 |                  0.795 |                  0.8   |                 0.771 |                 0.767 |                0.815 |                0.812 |              0.739 |              0.763 |                0.545 |                0.786 |                0.737 |                0.771 |
| GPT-5                  |                  0.704 |                  0.717 |                 0.757 |                 0.775 |                   0.708 |                   0.7   |                0.76  |                0.75  |                  0.806 |                  0.8   |                  0.847 |                  0.855 |                 0.725 |                 0.725 |                0.746 |                0.75  |              0.811 |              0.812 |                0.534 |                0.8   |                0.759 |                0.8   |
| GPT-5-mini             |                  0.738 |                  0.763 |                 0.75  |                 0.763 |                   0.649 |                   0.638 |                0.788 |                0.763 |                  0.794 |                  0.788 |                  0.802 |                  0.818 |                 0.751 |                 0.75  |                0.772 |                0.763 |              0.818 |              0.818 |                0.506 |                0.786 |                0.761 |                0.784 |
| LLaMA 3.3              |                  0.704 |                  0.712 |                 0.728 |                 0.738 |                   0.674 |                   0.688 |                0.766 |                0.75  |                  0.739 |                  0.75  |                  0.745 |                  0.75  |                 0.691 |                 0.688 |                0.79  |                0.788 |              0.681 |              0.725 |                0.642 |                0.8   |                0.649 |                0.711 |
| Gemma 3                |                  0.63  |                  0.65  |                 0.726 |                 0.763 |                   0.748 |                   0.763 |                0.762 |                0.755 |                  0.776 |                  0.775 |                  0.706 |                  0.717 |                 0.787 |                 0.785 |                0.744 |                0.742 |              0.679 |              0.717 |                0.426 |                0.657 |                0.624 |                0.707 |
| Gemini 2.5 Flash       |                  0.755 |                  0.755 |                 0.704 |                 0.717 |                   0.671 |                   0.667 |                0.725 |                0.692 |                  0.732 |                  0.717 |                  0.748 |                  0.755 |                 0.747 |                 0.738 |                0.736 |                0.722 |              0.738 |              0.759 |                0.493 |                0.743 |                0.744 |                0.767 |
| Mistral Medium 3.1     |                  0.729 |                  0.738 |                 0.696 |                 0.712 |                   0.683 |                   0.7   |                0.718 |                0.712 |                  0.727 |                  0.738 |                  0.659 |                  0.675 |                 0.748 |                 0.75  |                0.766 |                0.763 |              0.689 |              0.725 |                0.545 |                0.7   |                0.721 |                0.721 |
| GPT-5-nano             |                  0.771 |                  0.775 |                 0.695 |                 0.712 |                   0.654 |                   0.638 |                0.76  |                0.738 |                  0.784 |                  0.775 |                  0.708 |                  0.7   |                 0.774 |                 0.775 |                0.745 |                0.738 |              0.756 |              0.763 |                0.499 |                0.771 |                0.639 |                0.709 |
| Qwen3                  |                  0.653 |                  0.642 |                 0.629 |                 0.642 |                   0.637 |                   0.625 |                0.675 |                0.675 |                  0.625 |                  0.638 |                  0.565 |                  0.553 |                 0.707 |                 0.692 |                0.711 |                0.704 |              0.649 |              0.679 |                0.407 |                0.619 |                0.533 |                0.632 |
| GPT-4o-mini            |                  0.67  |                  0.662 |                 0.592 |                 0.575 |                   0.615 |                   0.6   |                0.701 |                0.688 |                  0.663 |                  0.65  |                  0.541 |                  0.513 |                 0.769 |                 0.763 |                0.729 |                0.712 |              0.74  |              0.763 |                0.527 |                0.791 |                0.666 |                0.663 |
| GPT-3.5                |                  0.642 |                  0.646 |                 0.571 |                 0.581 |                   0.594 |                   0.615 |                0.658 |                0.654 |                  0.589 |                  0.6   |                  0.58  |                  0.584 |                 0.665 |                 0.675 |                0.683 |                0.697 |              0.629 |              0.637 |                0.379 |                0.522 |                0.536 |                0.652 |
| Gemma 2                |                  0.644 |                  0.616 |                 0.561 |                 0.588 |                   0.541 |                   0.538 |                0.67  |                0.638 |                  0.588 |                  0.588 |                  0.489 |                  0.481 |                 0.609 |                 0.629 |                0.665 |                0.638 |              0.641 |              0.662 |                0.38  |                0.543 |                0.635 |                0.635 |
| LLaMA 4 Scout          |                  0.411 |                  0.425 |                 0.365 |                 0.413 |                   0.354 |                   0.388 |                0.433 |                0.475 |                  0.281 |                  0.3   |                  0.3   |                  0.325 |                 0.516 |                 0.566 |                0.427 |                0.415 |              0.378 |              0.438 |                0.221 |                0.357 |                0.457 |                0.438 |
| Support Vector Machine |                  0.483 |                  0.494 |                 0.197 |                 0.241 |                   0.067 |                   0.138 |                0.077 |                0.112 |                  0.058 |                  0.112 |                  0.073 |                  0.138 |                 0.057 |                 0.1   |                0.093 |                0.138 |              0.159 |              0.175 |                0.075 |                0.2   |                0.572 |                0.512 |
| fastText               |                  0.422 |                  0.436 |                 0.169 |                 0.266 |                   0.094 |                   0.15  |                0.063 |                0.138 |                  0.117 |                  0.184 |                  0.052 |                  0.105 |                 0.024 |                 0.062 |                0.092 |                0.126 |              0.095 |              0.138 |                0.101 |                0.177 |                0.459 |                0.474 |
| DeepSeek-r1            |                  0.18  |                  0.196 |                 0.146 |                 0.137 |                   0.148 |                   0.158 |                0.355 |                0.393 |                  0.131 |                  0.145 |                  0.189 |                  0.22  |                 0.207 |                 0.211 |                0.202 |                0.198 |              0.198 |              0.213 |                0.071 |                0.136 |                0.319 |                0.275 |
| Naive Bayes Classifier |                  0.214 |                  0.3   |                 0.139 |                 0.214 |                   0.144 |                   0.164 |                0.1   |                0.221 |                  0.08  |                  0.125 |                  0.059 |                  0.169 |                 0.088 |                 0.151 |                0.094 |                0.126 |              0.093 |              0.138 |                0.092 |                0.1   |                0.336 |                0.38  |
| Dummy (Most Frequent)  |                  0.028 |                  0.125 |                 0.025 |                 0.112 |                   0.033 |                   0.15  |                0.02  |                0.088 |                  0.028 |                  0.125 |                  0.033 |                  0.15  |                 0.023 |                 0.1   |                0.03  |                0.138 |              0.028 |              0.125 |                0.053 |                0.229 |                0.038 |                0.178 |



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
