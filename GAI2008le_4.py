input_file = open('GAI2008le_4.txt','r')
line = input_file.readline()
while line !='':
    print(line)
    line = input_file.readline()
input_file.close()