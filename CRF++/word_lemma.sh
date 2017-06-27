cat NLSPARQL.train.feats.txt | cut -f 1,3 > word_lemma.train.txt
cat NLSPARQL.train.data | cut -f 2 > label.data
paste word_lemma.train.txt label.data > word_lemma.train.data

cat NLSPARQL.test.feats.txt | cut -f 1,3 > word_lemma.test.txt
cat NLSPARQL.test.data | cut -f 2 > test.label.data
paste word_lemma.test.txt test.label.data > word_lemma.test.data

crf_learn $1 word_lemma.train.data $2

crf_test -m $2 word_lemma.test.data > $3

perl conlleval.pl -d '\t' < $3 > $4
