import spacy
from spacy import displacy
from spacy.symbols import nsubj, VERB, NOUN

nlp = spacy.load('en_core_web_sm')

TEXT = [
        # 'CONVENTIONAL OVEN Preferred method.\n1. Preheat oven to 400°F.\n2. Place frozen nuggets on baking sheet.\n3. Heat 11 to 13 minutes.'
        # 'Conventional Oven\nPreferred method.\n1.  Preheat oven to 400°F.\n2.  Place frozen strips on baking sheet coated with cooking spray.\n3.  Heat 15 to 20 minutes, turning strips over halfway through heating time.\nAppliances vary.  Heating times approximate.',
        # 'Microwave Oven\n1.  Arrange frozen strips on microwave safe plate.\n2.  Heat on HIGH:\n\t1 strip for 1 1/2 to 2 minutes,\n\t2 strips for 2 to 3 minutes,\n\t3 strips for 3 to 3 1/2 minutes.\nDo not overheat.\n3.  Let stand 1 to 2 minutes before serving.\nAppliances vary.  Heating times approximate.',
        'Cooking instructions - cooking times may vary depending on oven. Conventional oven - preheat oven to 425°f. Remove bread from bag. Place bread spread side up on baking pan. Place baking pan on middle oven rack. Heat 10 minutes or until golden brown.',
        # 'Grill - remove bread from bag, wrap in aluminum foil. Place bread on grill rack. Grill 10 to 15 minutes or until heated through. Turn frequently to prevent burning.'
]

doc = nlp(u'Cooking instructions - cooking times may vary depending on oven. Conventional oven - preheat oven to 425°f. Remove bread from bag. Place bread spread side up on baking pan. Place baking pan on middle oven rack. Heat 10 minutes or until golden brown.')
# displacy.serve(doc, style='dep', options=options)
sentences = list(doc.sents)
# print(len(doc))

# Print the each sentence in the text
for sentence in sentences:
    print (sentence)


# for token in doc:
#     print(token, token.lemma_, token.pos_, token.tag_, token.dep_,
#           token.shape_ )

# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)
#     ent.merge()

# Print the head word of each sentence.
# This is the grammatically most informative word.
# for sentence in doc.sents:
#     print(sentence.root)

# Print all noun chunks.
# These are contiguous noun phrases.
# for chunk in doc.noun_chunks:
    # print(chunk)    

# Print the dependency subtree of each token.
# These are the words operated upon by the token.
# for token in doc:
    # print(token, [child for child in token.subtree] )

# Print the dependency subtree of each token.
# These are the words operated upon by the token.
# token.flags,
# for token in doc:
    # print(token, token.tag_, token.is_punct )
    # print(nlp.vocab.morphology.tag_map[token.tag_])