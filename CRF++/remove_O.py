#! /bin/python3
import sys

if (len(sys.argv) != 3):
    sys.exit(0)
train_data_file = open(sys.argv[1],"r")
train_final_file = open(sys.argv[1]+".without_O", "w")
test_data_file = open(sys.argv[2],"r")
test_final_file = open(sys.argv[2]+".without_O", "w")
train_data= train_data_file.read().split('\n')
test_data = test_data_file.read().split('\n')
for data in train_data:
    print(data)
    if data != '':
        word_data, concept = data.split("\t")
        if concept == "O":
            concept = "O-" + word_data
        train_final_file.write(word_data + "\t" + concept +"\n")
    else:
        train_final_file.write("\n")
for data in test_data:
    if  data != '':
        word_data, concept = data.split("\t")
        if concept == "O":
            concept = "O-" + word_data
        test_final_file.write(word_data + "\t" + concept +"\n")
    else:
        test_final_file.write("\n")
