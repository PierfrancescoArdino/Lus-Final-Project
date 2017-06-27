#! /usr/bin/python3

import sys
import math
import random
from collections import Counter

SEED = 782
random.seed(SEED)
train_file = open("data/NLSPARQL.train.data", "r")
train_feat = open("data/NLSPARQL.train.feats.txt", "r")

lexicon_word = open("data/lexicon_word.txt", "w")
lexicon_label = open("data/lexicon_label.txt", "w")

training_set = open("data/training_set", "w")
validation_set = open("data/validation_set", "w")

test_file = open("data/NLSPARQL.test.data", "r")
test_feat = open("data/NLSPARQL.test.feats.txt", "r")

split_f = train_feat.read().split('\n')
split_t = train_file.read().split('\n')
split_test_f = test_feat.read().split('\n')
split_test_t = test_file.read().split('\n')
validation_set_len = int(sys.argv[1])
word_lemma_pos_iob = []
words = []
iob = []
line = []
sentences = []

for x,y in zip(split_t, split_f):
    if x != '' and y != '':
        a, b = x.split('\t')  #word iob
        c, d, e = y.split('\t') #word pos lemma
        words.append(a)
        iob.append(b)
        line.append((a, b))
    else:
        sentences.append(line)
        line = []

for x,y in zip(split_test_t, split_test_f):
    if x != '' and y != '':
        a, b = x.split('\t')  #word iob
        c, d, e = y.split('\t') #word pos lemma
        iob.append(b)

random.shuffle(sentences)
###########################################################################################################
#                   LEXICON WORD

counted_words = Counter(words)
conta = 0

for i in counted_words:
    lexicon_word.write(str(i) + "\t" + str(conta) + "\n")
    conta += 1

lexicon_word.write("<UNK>\t" + str(conta) + "\n")

###########################################################################################################
#                   LEXICON IOB

counted_iob = Counter(iob)
conta1 = 0

for i in counted_iob:
    lexicon_label.write(str(i) + "\t" + str(conta1) + "\n")
    conta1 += 1

###########################################################################################################

validation_data = sentences[:validation_set_len]
train_data = sentences[validation_set_len:]

for i in train_data:
    for x in i:
        training_set.write(str(x[0]) + "\t" + str(x[1]) + "\n")
    training_set.write("\n")

for i in validation_data:
    for x in i:
        validation_set.write(str(x[0]) + "\t" + str(x[1]) + "\n")
    validation_set.write("\n")
