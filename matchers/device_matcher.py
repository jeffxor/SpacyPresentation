#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)
phraseMatcher = PhraseMatcher(nlp.vocab)

# Get the ID of the 'DEVICE' entity type. This is required to set an entity.
DEVICE = nlp.vocab.strings['DEVICE']
TEMP = nlp.vocab.strings['TEMP']
MODE = nlp.vocab.strings['MODE']
OPERATION = nlp.vocab.strings['OPERATION']
YIELD = nlp.vocab.strings['YIELD']

def add_device_ent(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end] 
    entity = (DEVICE, start, end)
    doc.ents += (entity,)

def add_temp_ent(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end] 
    entity = (TEMP, start, end)
    doc.ents += (entity,)

def add_mode_ent(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end] 
    entity = (MODE, start, end)
    doc.ents += (entity,)

def add_operation_ent(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end] 
    entity = (OPERATION, start, end)
    doc.ents += (entity,)

def add_yield_ent(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    span = doc[start:end] 
    entity = (YIELD, start, end)
    doc.ents += (entity,)

matcher.add('DEVICE', add_device_ent,
            [{'LOWER': 'toaster'}, {'LOWER': 'oven', 'OP': '+'}],
            [{'LOWER': 'conventional'}, {'LOWER': 'oven', 'OP': '+'}],
            [{'LOWER': 'grill'}],
            [{'LOWER': 'microwave'}],
            [{'LOWER': 'oven'}]
    )

matcher.add('TEMP', add_temp_ent,
            [{'SHAPE': 'ddd'}, {'ORTH': '°'}, {'LOWER': 'f'}],
            [{'SHAPE': 'ddd'}, {'LOWER': 'degrees'}],
            [{'LOWER': 'high'}, {'IS_PUNCT': True}, {'LOWER': 'heat'}],
            [{'LOWER': 'medium'}, {'IS_PUNCT': True}, {'LOWER': 'heat'}],
            [{'LOWER': 'low'}, {'IS_PUNCT': True}, {'LOWER': 'heat'}],
            [{'LOWER': 'high'}],
            [{'LOWER': 'medium'}],
            [{'LOWER': 'low'}],
    )

matcher.add('MODE', add_mode_ent,
            [{'LOWER': 'preheat'}],
            [{'LOWER': 'heat'}],
            [{'LEMMA': 'bake'}]
    )

matcher.add('OPERATION', add_operation_ent,
            [{'ENT_TYPE': 'CARDINAL'}, {'ORTH': '.'}]
    )


def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == '°':
            doc[token.i].is_sent_start = False
        if token.text == ':' and doc[token.i+1].is_space:
            doc[token.i+2].is_sent_start = False
        if token.text == '.' and doc[token.i-1].is_digit and doc[token.i+1].is_space == False:
            doc[token.i+1].is_sent_start = False
        if token.text == '.' and doc[token.i-1].is_digit and doc[token.i+1].is_space:
            doc[token.i-1].is_sent_start = True
            doc[token.i+2].is_sent_start = False
            doc[token.i+3].is_sent_start = False
    return doc

nlp.add_pipe(set_custom_boundaries, before='parser')  

# doc = nlp(u'Cooking instructions - cooking times may vary depending on oven. Conventional oven - preheat oven to 425°f. Remove bread from bag. Place bread spread side up on baking pan. Place baking pan on middle oven rack. Heat 10 minutes or until golden brown. Grill - remove bread from bag, wrap in aluminum foil. Place bread on grill rack. Grill 10 to 15 minutes or until heated through. Turn frequently to prevent burning.')
# doc = nlp(u'Microwave Oven\n1.  Arrange frozen strips on microwave safe plate.\n2.  Heat on HIGH:\n\t1 strip for 1 1/2 to 2 minutes,\n\t2 strips for 2 to 3 minutes,\n\t3 strips for 3 to 3 1/2 minutes.\nDo not overheat.\n3.  Let stand 1 to 2 minutes before serving.\nAppliances vary.  Heating times approximate.')
# doc = nlp(u'CONVENTIONAL OVEN Preferred method.\n1. Preheat oven to 400°F.\n2. Place frozen nuggets on baking sheet.\n3. Heat 11 to 13 minutes.')
doc = nlp(u'Conventional Oven\nPreferred method.\n1.  Preheat oven to 400°F.\n2.  Place frozen strips on baking sheet coated with cooking spray.\n3.  Heat 15 to 20 minutes, turning strips over halfway through heating time.\nAppliances vary.  Heating times approximate.')

# for token in doc:
#     if(token.is_sent_start):
#         print(token.text)

sentences = list(doc.sents)
for sentence in sentences:
    doc_sent = nlp(sentence.text)
    print(sentence)
    print('--------------------------------------')
    matches = matcher(doc_sent)
    for ent in doc_sent.ents:        
        print(ent.text, ent.label_)
    print('======================================')    


# sentences = list(doc.sents)
# for sentence in sentences:
#     print(sentence)
#     print('---------------')
#     for token in sentence:
#         print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#             token.shape_, token.is_alpha, token.is_stop)    


