#open_file = open('C:\\Users\\abdul\\Desktop\\Git\\Pythontest\\Beginner Projects\\misc\\saveData.txt')
#readSaveData = open_file.read()
#print(readSaveData)

#--------------------------------------------------------------

write_file = open('C:\\Users\\abdul\\Desktop\\Git\\Pythontest\\Beginner Projects\\misc\\testWrite.txt', 'w')
write_file.write('''This is a test for writing a file in 'misc' directory''')
write_file.close()

#--------------------------------------------------------------

read_file = open('C:\\Users\\abdul\\Desktop\\Git\\Pythontest\\Beginner Projects\\misc\\testWrite.txt')
print(read_file.read())