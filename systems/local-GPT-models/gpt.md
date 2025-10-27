# Evaluation of local GPT models

The following GPT models were installed locally and ran through the [Ollama API service](https://ollama.com/). We used the quantized models as provided through the [Ollama library](https://ollama.com/library/).

The following models were evaluated:
- [Gemma 3 (27B model)](https://ollama.com/library/gemma3) `gemma3:27b`
- [Gemma 2 (27B model)](https://ollama.com/library/gemma2) `gemma2:27b`
- [DeepSeek-R1 (14B model)](https://ollama.com/library/deepseek-r1) `deepseek-r1:14b`
- [Llama 3.3 model (70B model)](https://ollama.com/library/llama3.3) `llama3.3:latest`
- [GaMS-Instruct model (9B model)](https://huggingface.co/cjvt/GaMS-9B-Instruct) `GaMS-9B-Instruct:latest`

The prompt:
```python

	labels_dict = {
		0: "Other",
		1: "Information/Explanation",
		2: "News",
		3: "Instruction",
		4: "Opinion/Argumentation",
		5: "Forum",
		6: "Prose/Lyrical",
		7: "Legal",
		8: "Promotion"
	}

	for text in texts:
		current_prompt = f"""
				### Task
				Your task is to classify the following text according to genre. Genres are text types, defined by the function of the text, author’s purpose and form of the text. Always provide a label, even if you are not sure.

				### Output format
					Return a valid JSON dictionary with the following key: 'genre' and a value should be an integer which represents one of the labels according to the following dictionary: {labels_dict}.

					
					Text: '{text}'
			"""

```

In some (rare) cases, the models' output was invalid, e.g. `{"genre": -1}`, `{ "genre": 13 }`. These cases were manually changed to `Mix`, a label used with the X-GENRE and CORE classifiers when the prediction confidence is low.