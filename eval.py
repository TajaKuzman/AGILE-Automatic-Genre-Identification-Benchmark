import os
import pandas as pd
import json
from sklearn.metrics import f1_score
from datasets import load_dataset

import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("submission", help="Absolute path to the folder with submission files in JSON format")
	args = parser.parse_args()

submission_folder = args.submission

# Based on the dataset that is being evaluated, extract a list of true labels and a list of unique labels

def extract_true_label(dataset_name):
    """The function takes the dataset name and dataset dictionary and returns the list of true labels from the test split.
    Args:
    - dataset_name: should be "x-genre-test" or "en-ginco"
    """
    # Load the dataset from the hugging face
    if dataset_name == "x-genre-test":
        test = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "test")
    elif dataset_name == "en-ginco":
        test = load_dataset("TajaKuzman/X-GENRE-multilingual-text-genre-dataset", "EN-GINCO")

    test_df = pd.DataFrame(test["train"])

    # Extract a list of unique labels
    labels = list(test_df.labels.unique())

    # Extract label list
    y_true = test_df.labels.to_list()

    return [y_true, labels]

#Calculate the scores
def testing(true, pred, labels):
    """
    This function takes the list of true labels and list of predictions and evaluates the model based on comparing them.
    It calculates micro and macro F1 scores.
    
    Args:
    - y_true: list of true labels
    - y_pred: list of predicted labels

    The function returns a dictionary with micro and macro F1.
    """
    y_true = true
    y_pred = pred
    LABELS = labels

    # Calculate the scores
    macro = f1_score(y_true, y_pred, labels=LABELS, average="macro")
    micro = f1_score(y_true, y_pred, labels=LABELS,  average="micro")
    #print(f"Macro f1: {macro:0.3}, Micro f1: {micro:0.3}")
    
    return {"Micro F1":micro, "Macro F1": macro}

# Open the jsonl file with all results
with open("results/results.json", "r") as result_file:
    results_list = json.load(result_file)


# Get paths to all the submission files
submission_files = os.listdir(submission_folder)

# Evaluate all submissions in the submissions directory
for submission_file in submission_files:
    # Use only files that start with "submission"
    if "submission-" in submission_file:
        # Open the submission to be evaluated
        with open("{}/{}".format(submission_folder,submission_file), "r") as sub_file:
            results = json.load(sub_file)

            # Get information on the dataset and the model
            model = results["system"]

            dataset_name = results["predictions"][0]["test"]

            test_file = extract_true_label(dataset_name)
            y_true = test_file[0]
            labels = test_file[1]

            # Extract information on arguments if they exist
            try:
                epochs = results["args"]["num_train_epochs"]
                lr = results["args"]["learning_rate"]
            except:
                epochs = None
                lr = None

            # Extract predictions
            y_pred = results["predictions"][0]["predictions"]

            #print("Evaluation: {} on {}".format(model, dataset))

            current_scores = testing(y_true, y_pred, labels)

            current_res_dict = {"Model": model, "Test Dataset": dataset_name, "Macro F1": current_scores["Macro F1"], "Micro F1": current_scores["Micro F1"], "Epochs": epochs, "Learning Rate": lr}

            # Add the results to all results
            results_list.append(current_res_dict)

            with open("results/results.json", "w") as new_result_file:
                json.dump(results_list, new_result_file, indent = 2)

    else:
        print("Error: the following file `{}` is either not a submission file or is incorrectly named - see the `README.md` on how to prepare submission files.")

print("All evaluations completed. The results are added to the `results/results.json` file.")

# Create a dataframe from all results

result_df = pd.DataFrame(results_list)

# For each dataset, create a table with results

def results_table(result_df, dataset):
    dataset_df = result_df[result_df["Test Dataset"] == dataset]

    # Sort values based on highest Macro F1
    dataset_df = dataset_df.sort_values(by="Macro F1", ascending=False)

    # Round scores to 3 decimal places
    dataset_df["Macro F1"] = dataset_df["Macro F1"].round(3)

    dataset_df["Micro F1"] = dataset_df["Micro F1"].round(3)

    print(dataset_df.to_markdown(index=False))

    return dataset_df


for dataset in ["x-genre-test", "en-ginco"]:
    print("New benchmark scores:\n")

    current_df = results_table(result_df, dataset)
    print("\n------------------------------------------\n")

    # Save the table in markdown
    with open("results/results-{}.md".format(dataset), "w") as result_file:
        result_file.write(current_df.to_markdown(index=False))
