## en-ginco

| Model                                                                                                              | Test Dataset   |   Macro F1 |   Micro F1 |
|:-------------------------------------------------------------------------------------------------------------------|:---------------|-----------:|-----------:|
| X-GENRE classifier                                                                                                 | en-ginco       |      0.752 |      0.71  |
| CORE register classifier                                                                                           | en-ginco       |      0.593 |      0.613 |
| SVC                                                                                                                | en-ginco       |      0.572 |      0.512 |
| LOGISTICREGRESSION                                                                                                 | en-ginco       |      0.509 |      0.494 |
| fastText                                                                                                           | en-ginco       |      0.459 |      0.474 |
| COMPLEMENTNB                                                                                                       | en-ginco       |      0.336 |      0.38  |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli)) | en-ginco       |      0.16  |      0.231 |
| dummy-stratified                                                                                                   | en-ginco       |      0.102 |      0.166 |
| dummy-most_frequent                                                                                                | en-ginco       |      0.038 |      0.178 |