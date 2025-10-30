# Evaluation of local GPT models

The following GPT models were installed locally and ran through the [Ollama API service](https://ollama.com/). We used the quantized models as provided through the [Ollama library](https://ollama.com/library/).

The following models were evaluated:
- [Gemma 3 (27B model)](https://ollama.com/library/gemma3) `gemma3:27b`
- [DeepSeek-R1 (14B model)](https://ollama.com/library/deepseek-r1) `deepseek-r1:14b`
- [Llama 3.3 model (70B model)](https://ollama.com/library/llama3.3) `llama3.3:latest`
- [Llama 4 Scout model (17B active parameters, 109B total parameters, 16 experts)](https://ollama.com/library/llama4) `llama4:scout`
- [Qwen 3 (32B)](https://ollama.com/library/qwen3) `qwen3:32b`
- [GaMS-Instruct model (27B model)](https://huggingface.co/mradermacher/GaMS-27B-Instruct-i1-GGUF) `hf.co/mradermacher/GaMS-27B-Instruct-i1-GGUF:i1-Q4_K_M`

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

label_dict_with_description_ext = {
		"Information/Explanation - An objective text that describes or presents an event, a person, a thing, a concept etc. Its main purpose is to inform the reader about something. Common features: objective/factual, explanation/definition of a concept (x is …), enumeration. E.g., research article, encyclopedia article, informational blog, product specification, course materials, general information, job description, manual, horoscope, travel guide, glossaries, historical article, biographical story/history.": 1,
		"News - An objective or subjective text which reports on an event recent at the time of writing or coming in the near future. Common features: adverbs/adverbial clauses of time and/or place (dates, places), many proper nouns, direct or reported speech, past tense. E.g., news report, sports report, travel blog, reportage, police report, announcement.": 2,
		"Instruction - An objective text which instructs the readers on how to do something. Common features: multiple steps/actions, chronological order, 1st person plural or 2nd person, modality (must, have to, need to, can, etc.), adverbial clauses of manner (in a way that), of condition (if), of time (after …). E.g., how-to texts, recipes, technical support.": 3,
		"Opinion/Argumentation - A subjective text in which the authors convey their opinion or narrate their experience. It includes promotion of an ideology and other non-commercial causes. This genre includes a subjective narration of a personal experience as well. Common features: adjectives/adverbs that convey opinion, words that convey (un)certainty (certainly, surely), 1st person, exclamation marks. E.g., review, blog (personal blog, travel blog), editorial, advice, letter to editor, persuasive article or essay, formal speech, pamphlet, political propaganda, columns, political manifesto.": 4,
		"Forum - A text in which people discuss a certain topic in form of comments. Common features: multiple authors, informal language, subjective (the writers express their opinions), written in 1st person. E.g., discussion forum, reader/viewer responses, QA forum.": 5,
		"Prose/Lyrical - A literary text that consists of paragraphs or verses. A literary text is deemed to have no other practical purpose than to give pleasure to the reader. Often the author pays attention to the aesthetic appearance of the text. It can be considered as art. E.g., lyrics, poem, prayer, joke, novel, short story. ": 6,
		"Legal - An objective formal text that contains legal terms and is clearly structured. The name of the text type is often included in the headline (contract, rules, amendment, general terms and conditions, etc.). Common features: objective/factual, legal terms, 3rd person. E.g., small print, software license, proclamation, terms and conditions, contracts, law, copyright notices, university regulation.": 7,
		"Promotion - A subjective text intended to sell or promote an event, product, or service. It addresses the readers, often trying to convince them to participate in something or buy something. Common features: contains adjectives/adverbs that promote something (high-quality, perfect, amazing), comparative and superlative forms of adjectives and adverbs (the best, the greatest, the cheapest), addressing the reader (usage of 2nd person), exclamation marks. E.g., advertisement, promotion of a product (e-shops), promotion of an accommodation, promotion of company's services, invitation to an event.": 8,
		"Other - A text that which does not fall under any of other genre categories.": 0,

}

	for text in texts:
		current_prompt = f"""
				### Task
				Your task is to classify the following text according to genre. Genres are text types, defined by the function of the text, author’s purpose and form of the text. Always provide a label, even if you are not sure.

				### Output format
					Return a valid JSON dictionary with the following key: 'genre' and a value should be an integer which represents one of the labels according to the following dictionary: {label_dict_with_description_ext}.

					
					Text: '{text}'
			"""

```

In some (rare) cases, the models' output was invalid, e.g. `{"genre": -1}`, `{ "genre": 13 }`. These cases were manually changed to `Mix`, a label used with the X-GENRE and CORE classifiers when the prediction confidence is low.