testFile = open("Test2.txt", "w")
testFile.write("YOU SUCK\n")
testFile.close()

testFile = open("Test2.txt", "r")
print(testFile.read())
testFile.close()