#! /usr/bin/python3

import sys
import math
import random
from collections import Counter

SEED = 782
random.seed(SEED)
train_file = open("data/NLSPARQL.train.data", "r")
train_feat = open("data/NLSPARQL.train.feats.txt", "r")

lexicon_word = open("data/lexicon_word_wp.txt", "w")
lexicon_label = open("data/lexicon_label_wp.txt", "w")

training_set = open("data/training_set_wp", "w")
validation_set = open("data/validation_set_wp", "w")
testing_set = open("data/testing_set_wp", "w")
test_file = open("data/NLSPARQL.test.data", "r")
test_feat = open("data/NLSPARQL.test.feats.txt", "r")
validation_set_len=int(sys.argv[1])
split_f = train_feat.read().split('\n')
split_t = train_file.read().split('\n')
split_test_f = test_feat.read().split('\n')
split_test_t = test_file.read().split('\n')

word_lemma_pos_iob_train = []
words_train = []
iob = []
line_train = []
sentences_train = []
word_lemma_pos_iob_test = []
words_test = []
line_test = []
sentences_test = []
###########################################################################################################
#                    TRAIN FILE
for x,y in zip(split_t, split_f):
    if x != '' and y != '':
        a, b = x.split('\t')  #word iob
        c, d, e = y.split('\t') #word pos lemma
        wp =str(a)+"$"+str(d)
        words_train.append(wp)
        iob.append(b)
        line_train.append((wp, b))
    else:
        sentences_train.append(line_train)
        line_train = []
###########################################################################################################
#                    TEST FILE

for x,y in zip(split_test_t, split_test_f):
    if x != '' and y != '':
        a, b = x.split('\t')  #word iob
        c, d, e = y.split('\t') #word pos lemma
        wp =str(a)+"$"+str(d)
        words_test.append(wp)
        iob.append(b)
        line_test.append((wp, b))
    else:
        sentences_test.append(line_test)
        line_test = []

random.shuffle(sentences_train)
###########################################################################################################
#                   LEXICON WORD

counted_words = Counter(words_train)
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


validation_data = sentences_train[:validation_set_len]
train_data = sentences_train[validation_set_len:]

for i in train_data:
    for x in i:
        training_set.write(str(x[0]) + "\t" + str(x[1]) + "\n")
    training_set.write("\n")

for i in validation_data:
    for x in i:
        validation_set.write(str(x[0]) + "\t" + str(x[1]) + "\n")
    validation_set.write("\n")

for sentence in sentences_test:
    for line in sentence:
        testing_set.write(str(line[0]) + "\t" + str(line[1]) +"\n")
    testing_set.write("\n")
