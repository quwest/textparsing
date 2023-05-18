#!/usr/bin/python
# -*- coding: utf8 -*-
from collections import defaultdict
import spacy
from spacy import explain
from spacy import displacy

nlp = spacy.load("uk_core_news_sm")

def get_nlp_data_from_text(text: str) -> dict:
    doc = nlp(text)
    mydict = defaultdict(lambda: [0,[]])
    for token in doc:
        mydict[explain(token.pos_)][0] += 1
        mydict[explain(token.pos_)][1].append(token.text)

    return mydict

def make_nlp_img_from_text(text: str) -> str:
    doc = nlp(text)
    svg = displacy.render(doc, style="dep")

    return svg








# print(make_nlp_img_from_text('Привіт, як твої справи? У мене все добре я я я я я я я я я '))

#TODO: make svg to file if letters more than 100, add page to visualize result