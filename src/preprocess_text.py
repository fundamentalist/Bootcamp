# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:29:33 2021

@author: vg11995
"""
import pandas

import string

import spacy

def remove_punctuation(text):
    """
    text: input text to remove punctuations from
    returns cleaned version of the text
    """
    
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree



def tokenize_text(text):
    
    """
    text - input text for which I need to tokenize
    output returns a list of tokens
    
    """
    return text.split()

def MyNer(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def something():
    return 2
