## en-ginco

| Model                                                                                                              | Test Dataset   |   Macro F1 |   Micro F1 |
|:-------------------------------------------------------------------------------------------------------------------|:---------------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier)           | en-ginco       |      0.687 |      0.684 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                             | en-ginco       |      0.62  |      0.735 |
| Llama 3.3 (70B) (zero-shot)                                                                                        | en-ginco       |      0.586 |      0.684 |
| Gemma 2 (27B) (zero-shot)                                                                                          | en-ginco       |      0.564 |      0.603 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)               | en-ginco       |      0.545 |      0.588 |
| Gemma 3 (27B) (zero-shot)                                                                                          | en-ginco       |      0.541 |      0.672 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                   | en-ginco       |      0.534 |      0.632 |
| Support Vector Machine                                                                                             | en-ginco       |      0.514 |      0.489 |
| GPT-3.5-Turbo (zero-shot)                                                                                          | en-ginco       |      0.494 |      0.625 |
| Logistic Regression                                                                                                | en-ginco       |      0.464 |      0.471 |
| fastText                                                                                                           | en-ginco       |      0.408 |      0.445 |
| DeepSeek-R1 14B (zero-shot)                                                                                        | en-ginco       |      0.293 |      0.229 |
| Naive Bayes                                                                                                        | en-ginco       |      0.289 |      0.36  |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli)) | en-ginco       |      0.149 |      0.202 |
| Dummy Classifier (stratified)                                                                                      | en-ginco       |      0.088 |      0.154 |
| Dummy classifier (most frequent)                                                                                   | en-ginco       |      0.032 |      0.169 |