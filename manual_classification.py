import os
import re
from collections import Counter

path="H:\\masters\\sem5\\special_topics_in_advanced_db\\"

f = open(path+'manual classification.txt','r')

p_pos_a_pos = 0
p_pos_a_neg = 0
p_neg_a_pos = 0
p_neg_a_neg = 0

for line in f:
    a = line.split(':')
    review = a[1].split()
    predicted = review[0].rstrip()
    actual = review[1].rstrip()
    if predicted == 'pos' and actual == 'pos':
        p_pos_a_pos = p_pos_a_pos + 1
    elif predicted == 'pos' and actual == 'neg':
        p_pos_a_neg = p_pos_a_neg + 1
    elif predicted == 'neg' and actual == 'pos':
        p_neg_a_pos = p_neg_a_pos + 1
    elif predicted == 'neg' and actual == 'neg':
        p_neg_a_neg = p_neg_a_neg + 1
f.close()

print('Predicted Positive Actual Positive: ',p_pos_a_pos)
print('Predicted Positive Actual Negative: ',p_pos_a_neg)
print('Predicted Negative Actual Positive: ',p_neg_a_pos)
print('Predicted Negative Actual Negative: ',p_neg_a_neg)
