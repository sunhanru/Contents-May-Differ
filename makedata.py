import glob, os
import csv
import sys


def makedata(start=0):
    os.chdir("./")
    index = start
    for file in glob.glob("out*"):
        #print(file)
        
        targ = "data" + str(index) + ".txt"
        #print(targ)
        filenames = ["prob.tsp", file]
        with open(targ, mode='w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
        index = index + 1;

if __name__ == "__main__":
    path = "../../dataset/"
    dirs = os.listdir(path)
    highest = 0;

    for file in dirs:
        x = file.split(".")
        num = x[0]
        num = num[4:]
        num = int(num)
        if num > highest:
            highest = num

    highest = highest + 1
    makedata(highest)



#rm out*; rm data*; rm blah*; 
#./concorde -d -k50; python makedata.py 66; 
#mv data* ../../dataset/