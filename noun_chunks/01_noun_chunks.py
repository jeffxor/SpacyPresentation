import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u"Autonomous cars shift insurance liability toward manufacturers")
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
          chunk.root.head.text)

# Text: The original noun chunk text.
# Root text: The original text of the word connecting the noun chunk to the rest of the parse.
# Root dep: Dependency relation connecting the root to its head.
# Root head text: The text of the root token's head.
