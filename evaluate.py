import sys
import numpy as np

all_students = sys.argv[1]
true_data_file = sys.argv[2]
output_file = sys.argv[3]

f_in = open(all_students,'r')
f_out = open(output_file,'w')
f_out.write("Entry Number,MSE\n")

true_data = np.genfromtxt(true_data_file)

for line in f_in:
	line = line.strip()
	file_name = "output/" + line
	stud_data = np.genfromtxt(file_name)
	entry_num = line.split('_')[0]
	score = 0.0
	if(true_data.shape[0]==stud_data.shape[0]):
		error = true_data - stud_data
		error_2 = error**2
		score = np.mean(error_2)
	elif(stud_data.shape[0]>true_data.shape[0]):
		stud_data = stud_data[0:true_data.shape[0]]
		error = true_data - stud_data
		error_2 = error**2
		score = np.mean(error_2)
	else:
		true_data_copy = true_data[0:stud_data.shape[0]]
		error = true_data_copy - stud_data
		extra_size = true_data.shape[0]-stud_data.shape[0]
		extra_error = np.ones((extra_size,),dtype=np.float32)
		extra_error = extra_error*4
		error = np.concatenate((error,extra_error))
		error_2 = error**2
		score = np.mean(error_2)
	out_str = entry_num + ',' + str(score) + '\n'
	f_out.write(out_str)
f_in.close()
f_out.close()
