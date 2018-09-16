import spacy
# nlp = spacy.load('en')
nlp= spacy.load('my_model')
doc = nlp("can i get investment for the place in india?")
for ent in doc.ents:
    print(ent.text, ent.label_)
