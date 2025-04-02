# Web register multilingual classification model by TurkuNLP

We use the model [available on HuggingFace](https://huggingface.co/TurkuNLP/web-register-classification-multilingual). The model is based on XLM-RoBERTa-large and was fine-tuned on the multilingual CORE corpora across five languages (English, Finnish, French, Swedish, Turkish).

For setting up the model, we used the code that was included on the HuggingFace repository.

The model uses a different schema (CORE schema) than the X-GINCO and EN-GINCO test datasets. To evaluate it on these datasets, we used a mapping between schemata as proposed in https://arxiv.org/pdf/2406.19892v2 (Henriksson et al., 2024).

The mapping:
```python
	core_to_xgenre_mapping = {
		# machine-translated
		'MT': "Other",
		# Lyrical
		'LY': 'Prose/Lyrical',
		# Spoken
		'SP': "Other",
		# Interview
		'it': "Other",
		# Interactive Discussion
		'ID': "Forum",
		# Narrative
		'NA': "News",
		# news report
		'ne': "News",
		# sports report
		'sr': "News",
		# narrative blog
		'nb': "Opinion/Argumentation", 
		# How-to /Instructions
		'HI': "Instruction",
		# Recipe
		're': "Instruction",
		# Informational description
		'IN': 'Information/Explanation',
		# Encyclopedia article
		'en': 'Information/Explanation',
		# Research article
		'ra': 'Information/Explanation', 
		# Description of a thing or person
		'dtp': 'Information/Explanation',
		# Frequently asked questions
		'fi': "Instruction",
		# Legal terms and conditions
		'lt': "Legal",
		#Opinion
		'OP': 'Opinion/Argumentation',
		# Review
		'rv': 'Opinion/Argumentation',
		# Opinion blog
		'ob': 'Opinion/Argumentation',
		# Denominational religious blog or sermon
		'rs': "Prose/Lyrical",
		# Advice
		'av': 'Opinion/Argumentation',
		# Informational persuasion
		'IP': "Promotion",
		# Description with intent to sell
		'ds': "Promotion",
		# News & opinion blog or editorial
		'ed': 'Opinion/Argumentation'
	}
	```

The model can output multiple labels. In these cases, we used the label that is more specific (that is, a subcategory, e.g., 'ed') for the mapping. If the model didn't output any label, the output was mapped to "Mix" which is similar to how we use the X-GENRE classifier. If the model outputted more than one main category, the output is labelled as "Mix".

The model is described in the following work:

```
@misc{henriksson2024untanglingunrestrictedwebautomatic,
      title={Untangling the Unrestricted Web: Automatic Identification of Multilingual Registers}, 
      author={Erik Henriksson and Amanda Myntti and Anni Eskelinen and Selcen Erten-Johansson and Saara Hellström and Veronika Laippala},
      year={2024},
      eprint={2406.19892},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.19892}, 
}
```