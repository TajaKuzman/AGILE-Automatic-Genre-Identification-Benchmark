import json
import pandas as pd
import os
from sklearn.dummy import DummyClassifier
from datasets import load_dataset

# Get all the datasets from the HuggingFace
train = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "train")
test = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "test")
dev = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "dev")
EN_GINCO = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "EN-GINCO")

# To open them as Pandas DataFrame:
train_df = pd.DataFrame(train["train"])
test_df = pd.DataFrame(test["train"])
en_ginco = pd.DataFrame(EN_GINCO["train"])

print(train_df.shape, test_df.shape, en_ginco.shape)

def dummy(train_df, test_df, test_df_name):
    # Create X_train and Y_train parts, used for sci kit learning
    # List of texts in training split
    X_train = list(train_df.text)
    # List of labels in training split
    Y_train = list(train_df.labels)

    # List of texts in test split
    X_test = list(test_df.text)
    # List of labels in test split
    Y_test = list(test_df.labels)

    print(len(X_train), len(Y_train), len(X_test), len(Y_test))

    # Create a list of labels
    labels = list(test_df.labels.unique())
    print("Labels: {}".format(labels))

    for strategy in ["stratified", "most_frequent"]:
        model = f"dummy-{strategy}"

        dummy_mf = DummyClassifier(strategy=strategy)

        # Train the model
        dummy_mf.fit(X_train, Y_train)

        #Get the predictions
        y_pred_mf = dummy_mf.predict(X_test)

        y_pred = list(y_pred_mf)

        # Create a json with results
        current_results = {
            "system": model,
            "predictions": [
                {
                "train": "X-GENRE (train split)",
                "test": "{}".format(test_df_name),
                "predictions": y_pred,
                }
            ],
            #"model": model_type_dict[model][1],
            #"args": model_args,
            }

        # Save the results as a new json
        with open("submissions/submission-{}-{}.json".format(model, test_df_name), "w") as file:
            json.dump(current_results, file)

        print("Classification with {} on {} finished.".format(model, test_df_name))


dummy(train_df, test_df, "x-genre-test")

dummy(train_df, en_ginco, "en-ginco")