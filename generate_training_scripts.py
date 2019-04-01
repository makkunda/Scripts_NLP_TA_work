in_file = "entry_num.txt"
outer_path = "/home/cse/dual/cs5150459/scratch/nlp/submissions/"
train_file = "/home/cse/dual/cs5150459/scratch/nlp/data/train.json"
dev_file = "/home/cse/dual/cs5150459/scratch/nlp/data/dev.json"
f = open(in_file,'r')
f1 = open("training_scripts.sh",'w')
for entry_num in f:
    entry_num = entry_num.strip()
    line_1 = "#!/bin/sh\n### Set the job name\n"
    line_2 = "#PBS -N NLP_A1-1_train_"+entry_num+'\n'
    line_3 = "### Set the project name, your department code by default\n#PBS -P cse\n"
    line_4 = "####\n#PBS -l select=1:ncpus=1:ngpus=1\n### Specify \"wallclock time\" required for this job,hhh:mm:ss\n#PBS -l walltime=6:00:00\n"
    line_5 = "echo \"===============================\"\necho $PBS_JOBID\ncat $PBS_NODEFILE\necho \"===============================\"\ncd $PBS_O_WORKDIR\n"
    line_6 = "cd " + outer_path + entry_num + "\n"
    line_7 = ". /home/cse/dual/cs5150459/anaconda2/bin/activate nlp_a1_1\n"
    line_8 = "./compile.sh\n"
    line_9 = "./train.sh "+ train_file + " " + dev_file  + " " + entry_num + "_model\n"
    out_file = "training_scripts/" + entry_num + "_train.sh"
    f1.write('qsub ' + out_file+'\n')
    f_out = open(out_file,'w')
    f_out.write(line_1)
    f_out.write(line_2)
    f_out.write(line_3)
    f_out.write(line_4)
    f_out.write(line_5)
    f_out.write(line_6)
    f_out.write(line_7)
    f_out.write(line_8)
    f_out.write(line_9)
    f_out.close()
f.close()
f1.close()

