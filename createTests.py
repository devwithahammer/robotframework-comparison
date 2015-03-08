import os
def createTestFile(index):
	indexStr = str(index)
	filename = "tests/testCase" + indexStr + "/testCase" + indexStr + ".txt"

	d = os.path.dirname(filename)
	if not os.path.exists(d):
		os.makedirs(d)

	f = file(filename, 'w')

	f.write('*** Settings ***')
	f.write('\n')
	f.write('\n')				
	f.write('*** Test Cases ***')
	f.write('\n')
	f.write('Print Something')
	f.write('\n')
	f.write('	log	hello')
	f.write('\n')
	f.write('\n')
	f.write('\n')
	f.write('*** Keywords ***')
	f.write('\n')
	f.write('\n')

	f.close()

def createKeywordTestFile(index):
	indexStr = str(index)
	filename = "testKeywords/testCase" + indexStr + "/testCase" + indexStr + ".txt"

	d = os.path.dirname(filename)
	if not os.path.exists(d):
		os.makedirs(d)

	f = file(filename, 'w')

	f.write('*** Settings ***')
	f.write('\n')
	f.write('Library	TestKeyword'+ indexStr)
	f.write('\n')				
	f.write('*** Test Cases ***')
	f.write('\n')
	f.write('Check sum')
	f.write('\n')
	f.write('	${sum}=	returnSum	4	5')
	f.write('\n')
	f.write('	Should Be Equal As Integers	${sum}	9')
	f.write('\n')
	f.write('*** Keywords ***')
	f.write('\n')
	f.write('\n')

	f.close()


def createPythonKeyword(index):
	indexStr = str(index)
	filename = "pythonlib/TestKeyword" + indexStr + ".py"

	d = os.path.dirname(filename)
	if not os.path.exists(d):
		os.makedirs(d)

	f = file(filename, 'w')

	f.write('class TestKeyword'+ indexStr + ' :')
	f.write('\n')
	f.write('\n')				
	f.write('	def returnSum(self, inputOne, inputTwo) :')
	f.write('\n')
	f.write('\n')
	f.write('		return int(inputOne) + int(inputTwo)')
	f.write('\n')

	f.close()

for i in range(0, 3000):
	createTestFile(i)
	createKeywordTestFile(i)
	createPythonKeyword(i)

