import json
import random
import sys

def write_json(data,file_name,test=False,test_out=None):
    f = open(file_name,'w')
    if(test):
    	f_label = open(test_out,'w')
    for line in data:
    	if test:
    		f_label.write(str(line['ratings']))
    		f_label.write('\n')
    		line['ratings'] = 0.0
        f.write(json.dumps(line))
        f.write('\n')
    f.close()
    if(test):
    	f_label.close()

input_file_size = int(sys.argv[1])
dev_file_size = int(sys.argv[2])
test_file_size = int(sys.argv[3])


in_file = "review_rating.json"

in_f = open(in_file,'r')

data = []

for line in in_f :
    data.append(json.loads(line))

random.seed(8797)

random.shuffle(data)

training_data = data[0:input_file_size]
dev_data = data[input_file_size:(input_file_size + dev_file_size)]
test_data = data[(input_file_size + dev_file_size):(input_file_size + dev_file_size+test_file_size)]

write_json(training_data,'train.json')
print("done training")
write_json(dev_data,'dev.json')
print("done dev")
write_json(test_data,'test.json',True,"true_label.txt")
print("done test")
