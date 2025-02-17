import spacy

nlp = spacy.load('en_core_web_sm')

# sample text
text = "The water of Walden Pond is so beautifully blue. The water of the lake is clear and clean. The water of the lake is deep and cold."

# tokenize text with spacy
doc = nlp(text) 

size = len(doc);
print(size)

triagram = []


