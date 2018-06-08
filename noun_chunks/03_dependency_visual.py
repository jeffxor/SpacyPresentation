import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u"Autonomous cars shift insurance liability toward manufacturers")

displacy.serve(doc, style='dep')

# Universal POS tags
# http://universaldependencies.org/u/pos/
# ADJ 
# "The car is green."
# Adjectives are words that typically modify nouns and specify their properties or attributes. They may also function as predicates, as in
# http://universaldependencies.org/u/pos/ADJ.html

# NOUN
# Nouns are a part of speech typically denoting a person, place, thing, animal or idea.
# http://universaldependencies.org/u/pos/NOUN.html

# VERB
# A verb is a member of the syntactic class of words that typically signal events and actions, can constitute a minimal predicate in a clause, and govern the number and types of other constituents which may occur in the clause. Verbs are often associated with grammatical categories like tense, mood, aspect and voice, which can either be expressed inflectionally or using auxilliary verbs or particles.
# http://universaldependencies.org/u/pos/VERB.html

# ADP
# Adposition is a cover term for prepositions and postpositions. Adpositions belong to a closed set of items that occur before (preposition) or after (postposition) a complement composed of a noun phrase, noun, pronoun, or clause that functions as a noun phrase
# In many languages, adpositions can take the form of fixed multiword expressions, such as in spite of, because of, thanks to. 
# http://universaldependencies.org/u/pos/ADP.html

# Universal Dependency Relations
# http://universaldependencies.org/u/dep/
# https://nlp.stanford.edu/software/dependencies_manual.pdf

# amod - adjectival modifier
# An adjectival modifier of a noun is any adjectival phrase that serves to modify the meaning of the noun.
# "red meat"

# nsubj - nominal subject - http://universaldependencies.org/u/dep/nsubj.html
# A nominal subject (nsubj) is a nominal which is the syntactic subject and the proto-agent of a clause.
# "Clinton defeated"

# compound - compound - http://universaldependencies.org/u/dep/compound.html
# The compound relation is one of three relations for multiword expressions (MWEs)
# any kind of X0 compounding: noun compounds (e.g., phone book)

# dobj - direct object
# The direct object of a VP is the noun phrase which is the (accusative) object of the verb

# prep - prepositional modifier
# A prepositional modifier of a verb, adjective, or noun is any prepositional phrase that serves to modify
# the meaning of the verb, adjective, noun, or even another prepositon.

# pobj - object of a preposition
# The object of a preposition is the head of a noun phrase following the preposition, or the adverbs “here”
# and “there”. (The preposition in turn may be modifying a noun, verb, etc.)