## x-ginco

| Model                                                                                                              | Test Dataset   |   Macro F1 |   Micro F1 |
|:-------------------------------------------------------------------------------------------------------------------|:---------------|-----------:|-----------:|
| X-GENRE classifier                                                                                                 | x-ginco        |      0.848 |      0.845 |
| CORE register classifier                                                                                           | x-ginco        |      0.651 |      0.652 |
| LOGISTICREGRESSION                                                                                                 | x-ginco        |      0.174 |      0.185 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli)) | x-ginco        |      0.17  |      0.189 |
| SVC                                                                                                                | x-ginco        |      0.166 |      0.184 |
| fastText                                                                                                           | x-ginco        |      0.156 |      0.179 |
| COMPLEMENTNB                                                                                                       | x-ginco        |      0.143 |      0.171 |
| dummy-stratified                                                                                                   | x-ginco        |      0.106 |      0.113 |
| dummy-most_frequent                                                                                                | x-ginco        |      0.029 |      0.133 |