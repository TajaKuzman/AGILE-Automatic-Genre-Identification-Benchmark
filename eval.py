import os
import pandas as pd
import json
from sklearn.metrics import f1_score
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("submission", help="Absolute path to the folder with submission files in JSON format")
	args = parser.parse_args()

submission_folder = args.submission

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
    
    return {"Micro F1": micro, "Macro F1": macro}

def add_predictions_to_dataset(dataset_name, results):
    """The function takes the dataset name and dataset dictionary and returns test dataset with predictions.
    Args:
    - dataset_name: should be "x-ginco" or "en-ginco"
    """
    # Load the dataset from the hugging face
    if dataset_name == "x-ginco":
        test_df = pd.read_json("datasets/X-GINCO-test-set/X-GINCO.jsonl", lines=True)
    elif dataset_name == "en-ginco":
        test_df = pd.read_json("datasets/EN-GINCO-test-dataset/EN-GINCO.jsonl", lines=True)

    # Extract predictions
    y_pred = results["predictions"][0]["predictions"]
    test_df["y_pred"] = y_pred

    return test_df

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

            # Extract information on arguments if they exist
            try:
                epochs = results["args"]["num_train_epochs"]
                lr = results["args"]["learning_rate"]
            except:
                epochs = None
                lr = None

            test_df = add_predictions_to_dataset(dataset_name, results)

            # Calculate overall results
            y_true = test_df["labels"].to_list()
            y_pred = test_df["y_pred"].to_list()
            labels = list(test_df["labels"].unique())

            #print("Evaluation: {} on {}".format(model, dataset))

            current_scores = testing(y_true, y_pred, labels)

            # Calculate results for each language
            language_results_dict = {}
            
            eval_langs = list(test_df["language"].unique())

            for lang in eval_langs:
                cur_df = test_df[test_df["language"] == lang]
                y_true_lang = cur_df["labels"].to_list()
                y_pred_lang = cur_df["y_pred"].to_list()
                labels_lang = list(cur_df["labels"].unique())
                current_scores_lang = testing(y_true_lang, y_pred_lang, labels_lang)
                language_results_dict[lang] = {"Macro F1": float(current_scores_lang["Macro F1"]), "Micro F1": float(current_scores_lang["Micro F1"])}

            current_res_dict = {"Model": model, "Test Dataset": dataset_name, "Macro F1": current_scores["Macro F1"], "Micro F1": current_scores["Micro F1"], "Epochs": epochs, "Learning Rate": lr, "Language-Specific Scores": language_results_dict}

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
    dataset_df.drop(columns=["Language-Specific Scores", "Epochs", "Learning Rate"], inplace=True)

    print(dataset_df.to_markdown(index=False))

    return dataset_df


for dataset in ["x-ginco", "en-ginco"]:
    print("New benchmark scores:\n")

    current_df = results_table(result_df, dataset)
    
    print("\n------------------------------------------\n")

    # Save the table in markdown
    with open("results/results-{}.md".format(dataset), "w") as result_file:
        result_file.write("## {}\n\n".format(dataset))
        result_file.write(current_df.to_markdown(index=False))

# Create language-specific results
lang_results_dict = []

for lang in ["Albanian", "Catalan", "Croatian", "English", "Greek", "Icelandic", "Macedonian", "Maltese", "Slovenian", "Turkish", "Ukrainian"]:
	for result in results_list:
		cur_result = {"Model": result["Model"], "Test Dataset": result["Test Dataset"], "Language": lang}
		try:
			cur_macro = result["Language-Specific Scores"][lang]["Macro F1"]
			cur_micro = result["Language-Specific Scores"][lang]["Micro F1"]
			cur_result["Macro F1"] = cur_macro
			cur_result["Micro F1"] = cur_micro

			lang_results_dict.append(cur_result)
		except:
			continue

lang_results_df = pd.DataFrame(lang_results_dict)

# For each language, create a table with results

def results_table_lang(lang_results_df, lang):
    dataset_df = lang_results_df[lang_results_df["Language"] == lang]

    # Sort values based on highest Macro F1
    dataset_df = dataset_df.sort_values(by="Macro F1", ascending=False)

    # Round scores to 3 decimal places
    dataset_df["Macro F1"] = dataset_df["Macro F1"].round(3)

    dataset_df["Micro F1"] = dataset_df["Micro F1"].round(3)
    

    print(dataset_df.to_markdown(index=False))

    return dataset_df


lang_result_file = open("results/language-specific-results.md", "w")

for lang in ["Albanian", "Catalan", "Croatian", "English", "Greek", "Icelandic", "Macedonian", "Maltese", "Slovenian", "Turkish", "Ukrainian"]:

    current_df = results_table_lang(lang_results_df, lang)
    
    lang_result_file.write("\n#### {}\n\n".format(lang))
    lang_result_file.write(current_df.to_markdown(index=False))
    lang_result_file.write("\n\n------------------------------------------\n")

lang_result_file.close()