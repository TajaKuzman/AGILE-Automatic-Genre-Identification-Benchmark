import os
import pandas as pd
import json


# Open the jsonl file with all results
with open("results/results.json", "r") as result_file:
    results_list = json.load(result_file)


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