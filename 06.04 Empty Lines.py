Read="06.04 EmptyLinesInput.txt"
Write= "06.04 EmptyLinesOutput.txt"
fout=open(Write,"w")
rct=0
wct=0
with open(Read,"r") as f:
    for line in f:
        rct+=1
        if line.strip():
            wct+=1
            fout.write(line)
fout.close()
print(rct,'records read')
print(wct,'records written')