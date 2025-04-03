# NLI classifier

Natural Language Inference (NLI) models are known to be capable of high zero-shot classification in various tasks. That's why we included an example of such model in the benchmark.

We evaluate the [multilingual mDeBERTa-v3-base-mnli-xnli](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli) model that is based on the multilingual mDeBERTa model pre-trained on CC100 multilingual dataset and that was fine-tuned on XNLI dataset.

Model authors:
```
@article{laurer2024less,
  title={Less annotating, more classifying: Addressing the data scarcity issue of supervised machine learning with deep transfer learning and BERT-NLI},
  author={Laurer, Moritz and Van Atteveldt, Wouter and Casas, Andreu and Welbers, Kasper},
  journal={Political Analysis},
  volume={32},
  number={1},
  pages={84--100},
  year={2024},
  publisher={Cambridge University Press}
}
```