
#### Albanian

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Albanian   |      0.854 |      0.85  |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Albanian   |      0.787 |      0.785 |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Albanian   |      0.774 |      0.775 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Albanian   |      0.771 |      0.767 |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Albanian   |      0.769 |      0.767 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Albanian   |      0.769 |      0.762 |
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Albanian   |      0.751 |      0.75  |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Albanian   |      0.748 |      0.75  |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Albanian   |      0.747 |      0.738 |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Albanian   |      0.725 |      0.725 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Albanian   |      0.709 |      0.728 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Albanian   |      0.707 |      0.692 |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Albanian   |      0.691 |      0.688 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Albanian   |      0.665 |      0.675 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Albanian   |      0.609 |      0.629 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Albanian   |      0.516 |      0.566 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Albanian   |      0.404 |      0.408 |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Albanian   |      0.207 |      0.211 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Albanian   |      0.207 |      0.213 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Albanian   |      0.097 |      0.102 |
| Naive Bayes                                                                                                                                       | x-ginco        | Albanian   |      0.088 |      0.151 |
| Logistic Regression                                                                                                                               | x-ginco        | Albanian   |      0.058 |      0.15  |
| Support Vector Machine                                                                                                                            | x-ginco        | Albanian   |      0.057 |      0.1   |
| fastText                                                                                                                                          | x-ginco        | Albanian   |      0.024 |      0.062 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Albanian   |      0.023 |      0.1   |

------------------------------------------

#### Catalan

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Catalan    |      0.788 |      0.788 |
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Catalan    |      0.788 |      0.762 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Catalan    |      0.769 |      0.75  |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Catalan    |      0.766 |      0.75  |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Catalan    |      0.762 |      0.755 |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Catalan    |      0.76  |      0.75  |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Catalan    |      0.76  |      0.738 |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Catalan    |      0.742 |      0.725 |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Catalan    |      0.725 |      0.692 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Catalan    |      0.718 |      0.712 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Catalan    |      0.701 |      0.688 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Catalan    |      0.675 |      0.675 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Catalan    |      0.67  |      0.638 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Catalan    |      0.662 |      0.642 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Catalan    |      0.658 |      0.654 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Catalan    |      0.433 |      0.475 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Catalan    |      0.431 |      0.418 |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Catalan    |      0.355 |      0.393 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Catalan    |      0.168 |      0.187 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Catalan    |      0.146 |      0.139 |
| Naive Bayes                                                                                                                                       | x-ginco        | Catalan    |      0.1   |      0.221 |
| Support Vector Machine                                                                                                                            | x-ginco        | Catalan    |      0.077 |      0.112 |
| Logistic Regression                                                                                                                               | x-ginco        | Catalan    |      0.063 |      0.138 |
| fastText                                                                                                                                          | x-ginco        | Catalan    |      0.063 |      0.138 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Catalan    |      0.02  |      0.088 |

------------------------------------------

#### Croatian

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Croatian   |      0.894 |      0.9   |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Croatian   |      0.795 |      0.805 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Croatian   |      0.783 |      0.8   |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Croatian   |      0.757 |      0.775 |
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Croatian   |      0.75  |      0.762 |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Croatian   |      0.728 |      0.738 |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Croatian   |      0.726 |      0.762 |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Croatian   |      0.704 |      0.717 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Croatian   |      0.696 |      0.712 |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Croatian   |      0.695 |      0.712 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Croatian   |      0.629 |      0.642 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Croatian   |      0.616 |      0.632 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Croatian   |      0.592 |      0.575 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Croatian   |      0.571 |      0.581 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Croatian   |      0.561 |      0.588 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Croatian   |      0.365 |      0.412 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Croatian   |      0.35  |      0.392 |
| Support Vector Machine                                                                                                                            | x-ginco        | Croatian   |      0.197 |      0.241 |
| fastText                                                                                                                                          | x-ginco        | Croatian   |      0.169 |      0.266 |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Croatian   |      0.146 |      0.137 |
| Naive Bayes                                                                                                                                       | x-ginco        | Croatian   |      0.139 |      0.214 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Croatian   |      0.119 |      0.169 |
| Logistic Regression                                                                                                                               | x-ginco        | Croatian   |      0.117 |      0.155 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Croatian   |      0.055 |      0.064 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Croatian   |      0.025 |      0.112 |

------------------------------------------

#### English

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | en-ginco       | English    |      0.688 |      0.75  |
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | en-ginco       | English    |      0.686 |      0.684 |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | en-ginco       | English    |      0.655 |      0.735 |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | en-ginco       | English    |      0.653 |      0.761 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | en-ginco       | English    |      0.62  |      0.735 |
| Gemini 2.5 Pro                                                                                                                                    | en-ginco       | English    |      0.618 |      0.739 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | en-ginco       | English    |      0.599 |      0.688 |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | en-ginco       | English    |      0.586 |      0.684 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | en-ginco       | English    |      0.564 |      0.603 |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | en-ginco       | English    |      0.56  |      0.676 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | en-ginco       | English    |      0.545 |      0.588 |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | en-ginco       | English    |      0.541 |      0.672 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | en-ginco       | English    |      0.534 |      0.632 |
| Support Vector Machine                                                                                                                            | en-ginco       | English    |      0.514 |      0.489 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | en-ginco       | English    |      0.494 |      0.625 |
| Logistic Regression                                                                                                                               | en-ginco       | English    |      0.464 |      0.471 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | en-ginco       | English    |      0.449 |      0.599 |
| fastText                                                                                                                                          | en-ginco       | English    |      0.408 |      0.445 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | en-ginco       | English    |      0.396 |      0.415 |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | en-ginco       | English    |      0.293 |      0.229 |
| Naive Bayes                                                                                                                                       | en-ginco       | English    |      0.289 |      0.36  |
| GaMS-9B-Instruct                                                                                                                                  | en-ginco       | English    |      0.255 |      0.351 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | en-ginco       | English    |      0.149 |      0.202 |
| Dummy Classifier (stratified)                                                                                                                     | en-ginco       | English    |      0.088 |      0.154 |
| Dummy classifier (most frequent)                                                                                                                  | en-ginco       | English    |      0.032 |      0.169 |

------------------------------------------

#### Greek

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Greek      |      0.818 |      0.818 |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Greek      |      0.811 |      0.812 |
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Greek      |      0.802 |      0.818 |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Greek      |      0.783 |      0.8   |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Greek      |      0.756 |      0.762 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Greek      |      0.74  |      0.762 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Greek      |      0.739 |      0.762 |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Greek      |      0.738 |      0.759 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Greek      |      0.716 |      0.718 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Greek      |      0.689 |      0.725 |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Greek      |      0.681 |      0.725 |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Greek      |      0.679 |      0.717 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Greek      |      0.649 |      0.679 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Greek      |      0.641 |      0.662 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Greek      |      0.629 |      0.637 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Greek      |      0.378 |      0.438 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Greek      |      0.284 |      0.299 |
| Logistic Regression                                                                                                                               | x-ginco        | Greek      |      0.223 |      0.238 |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Greek      |      0.198 |      0.213 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Greek      |      0.196 |      0.2   |
| Support Vector Machine                                                                                                                            | x-ginco        | Greek      |      0.159 |      0.175 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Greek      |      0.112 |      0.114 |
| fastText                                                                                                                                          | x-ginco        | Greek      |      0.095 |      0.138 |
| Naive Bayes                                                                                                                                       | x-ginco        | Greek      |      0.093 |      0.138 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Greek      |      0.028 |      0.125 |

------------------------------------------

#### Icelandic

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Icelandic  |      0.847 |      0.855 |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Icelandic  |      0.821 |      0.838 |
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Icelandic  |      0.802 |      0.818 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Icelandic  |      0.795 |      0.8   |
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Icelandic  |      0.775 |      0.78  |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Icelandic  |      0.748 |      0.755 |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Icelandic  |      0.745 |      0.75  |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Icelandic  |      0.708 |      0.7   |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Icelandic  |      0.706 |      0.717 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Icelandic  |      0.659 |      0.675 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Icelandic  |      0.58  |      0.584 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Icelandic  |      0.565 |      0.553 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Icelandic  |      0.556 |      0.584 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Icelandic  |      0.541 |      0.512 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Icelandic  |      0.489 |      0.481 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Icelandic  |      0.327 |      0.351 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Icelandic  |      0.3   |      0.325 |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Icelandic  |      0.189 |      0.22  |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Icelandic  |      0.171 |      0.201 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Icelandic  |      0.145 |      0.167 |
| Logistic Regression                                                                                                                               | x-ginco        | Icelandic  |      0.075 |      0.113 |
| Support Vector Machine                                                                                                                            | x-ginco        | Icelandic  |      0.073 |      0.138 |
| Naive Bayes                                                                                                                                       | x-ginco        | Icelandic  |      0.059 |      0.169 |
| fastText                                                                                                                                          | x-ginco        | Icelandic  |      0.052 |      0.105 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Icelandic  |      0.033 |      0.15  |

------------------------------------------

#### Macedonian

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Macedonian |      0.911 |      0.912 |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Macedonian |      0.748 |      0.762 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Macedonian |      0.722 |      0.738 |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Macedonian |      0.708 |      0.7   |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Macedonian |      0.684 |      0.692 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Macedonian |      0.683 |      0.7   |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Macedonian |      0.674 |      0.688 |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Macedonian |      0.671 |      0.667 |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Macedonian |      0.654 |      0.638 |
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Macedonian |      0.649 |      0.638 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Macedonian |      0.637 |      0.675 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Macedonian |      0.637 |      0.625 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Macedonian |      0.615 |      0.6   |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Macedonian |      0.594 |      0.615 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Macedonian |      0.541 |      0.538 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Macedonian |      0.354 |      0.388 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Macedonian |      0.264 |      0.284 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Macedonian |      0.196 |      0.213 |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Macedonian |      0.148 |      0.158 |
| Naive Bayes                                                                                                                                       | x-ginco        | Macedonian |      0.144 |      0.164 |
| Logistic Regression                                                                                                                               | x-ginco        | Macedonian |      0.099 |      0.125 |
| fastText                                                                                                                                          | x-ginco        | Macedonian |      0.094 |      0.15  |
| Support Vector Machine                                                                                                                            | x-ginco        | Macedonian |      0.067 |      0.138 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Macedonian |      0.065 |      0.065 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Macedonian |      0.033 |      0.15  |

------------------------------------------

#### Maltese

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Maltese    |      0.642 |      0.8   |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Maltese    |      0.571 |      0.835 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Maltese    |      0.545 |      0.7   |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Maltese    |      0.545 |      0.786 |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Maltese    |      0.534 |      0.8   |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Maltese    |      0.527 |      0.791 |
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Maltese    |      0.51  |      0.58  |
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Maltese    |      0.506 |      0.786 |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Maltese    |      0.499 |      0.771 |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Maltese    |      0.493 |      0.743 |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Maltese    |      0.426 |      0.657 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Maltese    |      0.407 |      0.619 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Maltese    |      0.38  |      0.543 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Maltese    |      0.379 |      0.522 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Maltese    |      0.221 |      0.357 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Maltese    |      0.205 |      0.299 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Maltese    |      0.166 |      0.25  |
| fastText                                                                                                                                          | x-ginco        | Maltese    |      0.101 |      0.177 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Maltese    |      0.1   |      0.132 |
| Naive Bayes                                                                                                                                       | x-ginco        | Maltese    |      0.092 |      0.1   |
| Support Vector Machine                                                                                                                            | x-ginco        | Maltese    |      0.075 |      0.2   |
| Logistic Regression                                                                                                                               | x-ginco        | Maltese    |      0.073 |      0.071 |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Maltese    |      0.071 |      0.136 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Maltese    |      0.053 |      0.229 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Maltese    |      0     |      0     |

------------------------------------------

#### Slovenian

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Slovenian  |      0.936 |      0.938 |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Slovenian  |      0.771 |      0.775 |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Slovenian  |      0.755 |      0.755 |
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Slovenian  |      0.738 |      0.762 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Slovenian  |      0.729 |      0.738 |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Slovenian  |      0.705 |      0.726 |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Slovenian  |      0.704 |      0.717 |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Slovenian  |      0.704 |      0.712 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Slovenian  |      0.695 |      0.7   |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Slovenian  |      0.679 |      0.684 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Slovenian  |      0.67  |      0.662 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Slovenian  |      0.653 |      0.642 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Slovenian  |      0.644 |      0.616 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Slovenian  |      0.642 |      0.646 |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Slovenian  |      0.63  |      0.65  |
| Logistic Regression                                                                                                                               | x-ginco        | Slovenian  |      0.563 |      0.561 |
| Support Vector Machine                                                                                                                            | x-ginco        | Slovenian  |      0.483 |      0.494 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Slovenian  |      0.459 |      0.481 |
| fastText                                                                                                                                          | x-ginco        | Slovenian  |      0.422 |      0.436 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Slovenian  |      0.411 |      0.425 |
| Naive Bayes                                                                                                                                       | x-ginco        | Slovenian  |      0.214 |      0.3   |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Slovenian  |      0.18  |      0.196 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Slovenian  |      0.131 |      0.157 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Slovenian  |      0.128 |      0.143 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Slovenian  |      0.028 |      0.125 |

------------------------------------------

#### Turkish

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Turkish    |      0.911 |      0.912 |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Turkish    |      0.849 |      0.85  |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Turkish    |      0.815 |      0.812 |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Turkish    |      0.79  |      0.788 |
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Turkish    |      0.772 |      0.762 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Turkish    |      0.766 |      0.762 |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Turkish    |      0.746 |      0.75  |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Turkish    |      0.745 |      0.738 |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Turkish    |      0.744 |      0.742 |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Turkish    |      0.736 |      0.722 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Turkish    |      0.729 |      0.712 |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Turkish    |      0.711 |      0.704 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Turkish    |      0.71  |      0.721 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Turkish    |      0.683 |      0.697 |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Turkish    |      0.665 |      0.638 |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Turkish    |      0.427 |      0.415 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Turkish    |      0.414 |      0.413 |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Turkish    |      0.202 |      0.198 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Turkish    |      0.164 |      0.203 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Turkish    |      0.129 |      0.14  |
| Logistic Regression                                                                                                                               | x-ginco        | Turkish    |      0.096 |      0.125 |
| Naive Bayes                                                                                                                                       | x-ginco        | Turkish    |      0.094 |      0.126 |
| Support Vector Machine                                                                                                                            | x-ginco        | Turkish    |      0.093 |      0.138 |
| fastText                                                                                                                                          | x-ginco        | Turkish    |      0.092 |      0.126 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Turkish    |      0.03  |      0.138 |

------------------------------------------

#### Ukrainian

| Model                                                                                                                                             | Test Dataset   | Language   |   Macro F1 |   Micro F1 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-----------|-----------:|-----------:|
| [X-GENRE classifier](https://huggingface.co/classla/xlm-roberta-base-multilingual-text-genre-classifier) (without Mix label for lower confidence) | x-ginco        | Ukrainian  |      0.933 |      0.938 |
| GPT-5 (gpt-5-2025-08-07) (zero-shot)                                                                                                              | x-ginco        | Ukrainian  |      0.806 |      0.8   |
| Gemini 2.5 Pro                                                                                                                                    | x-ginco        | Ukrainian  |      0.803 |      0.797 |
| GPT-5-mini (gpt-5-mini-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Ukrainian  |      0.794 |      0.788 |
| GPT-5-nano (gpt-5-nano-2025-08-07) (zero-shot)                                                                                                    | x-ginco        | Ukrainian  |      0.784 |      0.775 |
| GPT-4o (gpt-4o-2024-08-06) (zero-shot)                                                                                                            | x-ginco        | Ukrainian  |      0.782 |      0.775 |
| Gemma 3 (27B) (zero-shot)                                                                                                                         | x-ginco        | Ukrainian  |      0.776 |      0.775 |
| [CORE register classifier](https://huggingface.co/TurkuNLP/web-register-classification-multilingual)                                              | x-ginco        | Ukrainian  |      0.769 |      0.784 |
| Llama 3.3 (70B) (zero-shot)                                                                                                                       | x-ginco        | Ukrainian  |      0.739 |      0.75  |
| Gemini 2.5 Flash (zero-shot)                                                                                                                      | x-ginco        | Ukrainian  |      0.732 |      0.717 |
| Mistral Medium 3.1 (zero-shot)                                                                                                                    | x-ginco        | Ukrainian  |      0.727 |      0.738 |
| GPT-4o-mini (gpt-4o-mini-2024-07-18) (zero-shot)                                                                                                  | x-ginco        | Ukrainian  |      0.663 |      0.65  |
| Qwen3 (32B) (zero-shot)                                                                                                                           | x-ginco        | Ukrainian  |      0.625 |      0.638 |
| GPT-3.5-Turbo (zero-shot)                                                                                                                         | x-ginco        | Ukrainian  |      0.589 |      0.6   |
| Gemma 2 (27B) (zero-shot)                                                                                                                         | x-ginco        | Ukrainian  |      0.588 |      0.588 |
| GaMS-9B-Instruct                                                                                                                                  | x-ginco        | Ukrainian  |      0.441 |      0.45  |
| Llama 4 - Scout (zero-shot)                                                                                                                       | x-ginco        | Ukrainian  |      0.281 |      0.3   |
| DeepSeek-R1 14B (zero-shot)                                                                                                                       | x-ginco        | Ukrainian  |      0.131 |      0.145 |
| Logistic Regression                                                                                                                               | x-ginco        | Ukrainian  |      0.121 |      0.162 |
| fastText                                                                                                                                          | x-ginco        | Ukrainian  |      0.117 |      0.184 |
| Naive Bayes                                                                                                                                       | x-ginco        | Ukrainian  |      0.08  |      0.125 |
| NLI zero-shot model ([mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli))                                | x-ginco        | Ukrainian  |      0.066 |      0.101 |
| Support Vector Machine                                                                                                                            | x-ginco        | Ukrainian  |      0.058 |      0.112 |
| Dummy Classifier (stratified)                                                                                                                     | x-ginco        | Ukrainian  |      0.056 |      0.064 |
| Dummy classifier (most frequent)                                                                                                                  | x-ginco        | Ukrainian  |      0.028 |      0.125 |

------------------------------------------
