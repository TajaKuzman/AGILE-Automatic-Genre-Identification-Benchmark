# Classification with dummy models

We evaluated the following classifiers:
- Dummy with "stratified" method: DummyClassifier(strategy="stratified"),
- Dummy with "most frequent" method: DummyClassifier(strategy="most_frequent")

The selection of the stratified and most frequent category is based on the training split of the [X-GENRE dataset](https://huggingface.co/datasets/TajaKuzman/X-GENRE-text-genre-dataset) that was used to fine-tune the X-GENRE classifier and most of the other models that are compared in the benchmark.
