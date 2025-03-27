#실습1
input_file = open('GAI2008le_4.txt','r')
line = input_file.readline()
while line !='':
    print(line)
    line = input_file.readline()
input_file.close()
#실습2
file_1 = open('file_1', 'w')
file_1.write('create file_1')
file_1.close()
file_2 = open('file_2', 'w')
file_2.write('create file_2')
file_2.close()
path = '/Users/choinsu/Desktop/GAI2008/GAI2008_4/GAI2008le_4/file_3'
file_3 = open(path, 'w')
file_3.write('create flie_3')
file_3.close()
#실습3
input_emails = open('emails_yonsei.txt','r')
emails = input_emails.readlines()
input_emails.close()
storage_emails = open('emails_korea.txt','w')
for email in emails:
    storage_emails.write(email)
storage_emails.close()