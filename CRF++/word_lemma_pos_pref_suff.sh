crf_learn $1 NLSPARQL.train.data.enanched $2

crf_test -m $2  NLSPARQL.test.data.enanched  > $3

perl conlleval.pl -d '\t' < $3 > $4
