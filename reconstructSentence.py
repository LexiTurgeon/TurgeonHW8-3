#Resource: https://www.w3schools.com/python/python_for_loops.asp
#Resource: https://www.geeksforgeeks.org/python-list/
#Resource: https://www.w3schools.com/python/python_file_write.asp
#Resource: https://www.programiz.com/python-programming/methods/list/append
 
import sys

input1file = []
input2file = []

file1 = open(sys.argv[1], "r")
file2 = open(sys.argv[2], "r")

for eachWordFile1 in file1:
	input1file.extend(eachWordFile1.split())
print "List Number One is: ", input1file
file1Length = len(input1file)
print "The Length of File 1 is: ", file1Length

for eachWordFile2 in file2:
	input2file.extend(eachWordFile2.split())
print "List Number Two is: ", input2file
file2Length = len(input2file)
print "The Length of File 2 is: ", file2Length

if file1Length == file2Length:
	print "File Lengths are the Same, Try Two Different Files"
	sys.exit(0)

totalFileLength = file1Length + file2Length

holderList1 = []
holderList2 = []
totalLength = file1Length + file2Length
output = [None] * totalLength

result = [None]*(len(input1file)+len(input2file))
result[::2] = input1file
result[1::2] = input2file

length = len(result)
s = length
newResult = [None]*length
for item in result:
	s = s - 1
	newResult[s] = item

print newResult
