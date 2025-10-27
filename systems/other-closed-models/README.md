# Other closed-source models

We access the models through the [OpenRouter](https://openrouter.ai/) platform which provides a single API to access various closed-source models, including those from Google, Anthropic, Claude etc.

We evaluate the following models:
- [`google/gemini-2.5-flash`](https://openrouter.ai/google/gemini-2.5-flash)
- [`mistralai/mistral-medium-3.1`](https://openrouter.ai/mistralai/mistral-medium-3.1/api)

Anthropic models were not included, because they do not enable the `response_format` parameter. We don't include [`google/gemini-2.5-pro`](https://openrouter.ai/google/gemini-2.5-pro) because it is too expensive (0.01€ per instance).

We use the same prompt as for the local and OpenAI models, and use the same code as for the OpenAI models:
```python

		completion = client.chat.completions.create(model=gpt_model,
		response_format= {"type": "json_object"},
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
		],
		temperature = 0)

```