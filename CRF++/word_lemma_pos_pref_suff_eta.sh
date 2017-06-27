
cs=(0.5 0.75 1 1.25 1.5 1.75 2 3)
for c in "${cs[@]}"; do
  crf_learn -c ${c} $1 NLSPARQL.train.data.enanched $2_${c}
  crf_test -m $2_${c}  NLSPARQL.test.data.enanched  > $3_${c}
  perl conlleval.pl -d '\t' < $3_${c} > $4_${c}
done
