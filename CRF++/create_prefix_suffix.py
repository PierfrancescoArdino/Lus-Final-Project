#! /bin/python3
import sys

if (len(sys.argv) != 6):
    print("Usage \n python create_prefix_suffix.py <train_data_file> <train_test_file> <test_data_file> <test_feats_file> <suf_pref_len>")
    sys.exit(0)
train_data_file = open(sys.argv[1],"r")
train_feat_file = open(sys.argv[2],"r")
train_final_file = open(sys.argv[1]+".enanched", "w")
test_data_file = open(sys.argv[3],"r")
test_feat_file = open(sys.argv[4],"r")
test_final_file = open(sys.argv[3]+".enanched", "w")
pref_suf_len=int(sys.argv[5])
pref = "O"
suff = "O"
train_data= train_data_file.read().split('\n')
train_feat = train_feat_file.read().split('\n')
test_data = test_data_file.read().split('\n')
test_feat = test_feat_file.read().split('\n')
for data, feat in zip(train_data, train_feat):
    print(data)
    if data != '':
        word_data, concept = data.split("\t")
        word_feat, pos, lemma = feat.split("\t")
        if len(word_data) >= pref_suf_len:
            pref = word_data[0:pref_suf_len]
            suff = word_data[-pref_suf_len:]
        else:
            pref = "NOP"
            suff = "NOP"
        train_final_file.write(word_data + "\t" + pos + "\t" + lemma + "\t" + pref + "\t" + suff  + "\t" + concept +"\n")
    else:
        train_final_file.write("\n")
for data, feat in zip(test_data, test_feat):
    if  data != '':
        word_data, concept = data.split("\t")
        word_feat, pos, lemma = feat.split("\t")
        if len(word_data) >= pref_suf_len:
            pref = word_data[0:pref_suf_len]
            suff = word_data[-pref_suf_len:]
        else:
            pref = "NOP"
            suff = "NOP"
        test_final_file.write(word_data + "\t" + pos + "\t" + lemma + "\t" + pref + "\t" + suff  + "\t" + concept +"\n")
    else:
        test_final_file.write("\n")
