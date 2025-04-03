## x-ginco

| Model                                                                                                              | Test Dataset   |   Macro F1 |   Micro F1 |
|:-------------------------------------------------------------------------------------------------------------------|:---------------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)           | x-ginco        |      0.847 |      0.845 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                             | x-ginco        |      0.776 |      0.769 |
| Llama 3.3 (70B) (zero-shot)                                                                                        | x-ginco        |      0.741 |      0.738 |
| Gemma 3 (27B) (zero-shot)                                                                                          | x-ginco        |      0.739 |      0.733 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                   | x-ginco        |      0.688 |      0.67  |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)               | x-ginco        |      0.651 |      0.652 |
| GPT-3.5-Turbo (zero-shot)                                                                                          | x-ginco        |      0.627 |      0.622 |
| Gemma 2 (27B) (zero-shot)                                                                                          | x-ginco        |      0.612 |      0.593 |
| DeepSeek-R1 14B (zero-shot)                                                                                        | x-ginco        |      0.197 |      0.204 |
| Logistic Regression                                                                                                | x-ginco        |      0.174 |      0.185 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli)) | x-ginco        |      0.17  |      0.189 |
| Support Vector Machine                                                                                             | x-ginco        |      0.166 |      0.184 |
| fastText                                                                                                           | x-ginco        |      0.156 |      0.179 |
| Naive Bayes                                                                                                        | x-ginco        |      0.143 |      0.171 |
| Dummy Classifier (stratified)                                                                                      | x-ginco        |      0.106 |      0.113 |
| Dummy classifier (most frequent)                                                                                   | x-ginco        |      0.029 |      0.133 |