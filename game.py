import random

code = '%s%s%s%s' %(random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4),)

def checkBullsAndCows(test):
	testCode = list(code)
	noOfBulls = 0
	toReplace = list()
	for i in range(4):
		if testCode[i] == test[i]:
			noOfBulls += 1
			toReplace.append(testCode[i])
	for i in toReplace:
		while True:
			if i in testCode:
				testCode[testCode.index(i)] = 0
			else:
				break
	noOfCows = 0
	for i in test:
		if i in testCode:
			noOfCows += 1
			testCode.remove(i)
	return noOfBulls , noOfCows
	
def youwon():
	print 'Bingo! You figured out the code.'
	print 'It took you %d tries to do so' %noOfAttempts

def timeUp():
	print 'Oho! Sorry attempts over'
	print 'By the way, code was %s' %code
def tryagain(b,c,n):
	print '%d Bulls %d Cows'%(b,c)
	if nOA != 9953453994599:
		print '%d attempts left'%(nOA-n)

def gameStart():
	print 'This game is called bulls and cows'
	print 'The rules are very simple'
	print 'The system generates a code of four digits'
	print 'using the digits 1, 2, 3, and 4'
	print 'You have to guess the number in 8 attempts'
	print 'System will give you hints as follows'
	print 'Number of digits of your guessed number'
	print 'that are correctly placed are shown'
	print 'as number of bulls'
	print 'and the digits that are present in '
	print 'the actual code but are at incorrect place'
	print 'are shown as cows'
	print 'for example-'
	print 'if code is 1234, and you use 1424'
	print 'then you will get 2 bulls for 1 and 4'
	print 'and 1 cow for 2'
	print 'so let the games begin.........'

gameStart()
noOfAttempts = 0
print 'Unlimited tries or limited one??'
print 'Enter "U" for unlimited or "L <no. of tries>" (without double quotes) to set a limit'
attemptsSet = list(raw_input().split(' '))
if attemptsSet[0] == 'U':
	nOA = 9953453994599
elif attemptsSet[0] == 'L':
	nOA = int(attemptsSet[1])
while noOfAttempts<nOA:
	noOfAttempts+=1
	guess = raw_input('> ')
	if len(guess)==4:
		bulls,cows = checkBullsAndCows(list(guess))
		if guess==code:
			youwon()
			exit()
		else:
			tryagain(bulls,cows,noOfAttempts)
	else:
		print 'Code consists of four digits only'
		if nOA != 9953453994599:
			print 'You wasted this attempt'
			print '%d attempts left'%(nOA-noOfAttempts)

timeUp()