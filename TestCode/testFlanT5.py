from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

inputs = tokenizer("A step by step recipe to make bolognese pasta:", return_tensors="pt")

max_length = 1000


outputs = model.generate(**inputs,max_length=max_length)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True))