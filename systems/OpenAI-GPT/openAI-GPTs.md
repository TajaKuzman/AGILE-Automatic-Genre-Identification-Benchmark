# OpenAI's GPT models

We evaluate the following models:
- GPT-4o ("gpt-4o-2024-08-06"),
- GPT-3.5-Turbo ("gpt-3.5-turbo-0125"),
- GPT-4o-mini ("gpt-4o-mini-2024-07-18")

We use the following prompt:
```json
			messages= [
			{
				"role": "user",
				"content": f"""
				### Task
				Your task is to classify the following text according to genre. Genres are text types, defined by the function of the text, author’s purpose and form of the text. Always provide a label, even if you are not sure.

				### Output format
					Return a valid JSON dictionary with the following key: 'genre' and a value should be an integer which represents one of the labels according to the following dictionary: {labels_dict}.

					
					Text: '{text}'
			"""
				}
```

The evaluation of the three models on the X-GINCO and EN-GINCO dataset cost 3.27$.