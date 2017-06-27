cat NLSPARQL.train.data | cut -f 2 > label.data
paste NLSPARQL.train.feats.txt label.data > word_lemma_pos.train.data

cat NLSPARQL.test.data | cut -f 2 > test.label.data
paste NLSPARQL.test.feats.txt test.label.data > word_lemma_pos.test.data

crf_learn $1 word_lemma_pos.train.data $2

crf_test -m $2 word_lemma_pos.test.data > $3

perl conlleval.pl -d '\t' < $3 > $4
