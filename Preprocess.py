import os
import pickle
import random

inputs = [f for f in os.listdir(os.getcwd()) if 'input' in f]
data = []

for f in inputs:
	lines = [line.strip() for line in open(f, 'r').readlines()]
	labels = [line.strip() for line in open(f.replace('input', 'gs'), 'r').readlines()]
	for i in range(len(lines)):
		line, label = lines[i], labels[i]
		if label == '':
			continue
		sent1, sent2 = line.split('\t')[:2]
		tmp = {'label': label, 'sent1': sent1, 'sent2': sent2}
		data.append(tmp)

train = []
test = []
for d in data:
	if random.random() > 0.8:
		test.append(d)
	else:
		train.append(d)

f = open('train.pkl', 'wb')
pickle.dump(train, f)
f.close()

f = open('test.pkl', 'wb')
pickle.dump(test, f)
f.close()