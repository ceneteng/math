# app/math.py
import random

def getnums(numin, prbin):

    tot = numin + 1

    while tot>numin:
	num1 = random.randint(0,numin)
	num2 = random.randint(0,numin)

	if prbin == 'addition':
		tot = num1+num2
	elif prbin == 'subtraction':
		if num1>num2:
			tot = num1-num2
		else:
			tot = num2-num1
	

    eq = [num1,num2,tot]

    return eq
	
def main():
    
    name = str.title(raw_input("\n\nWhat is your name: "))
    myprobs = raw_input("%s, How many math problems would you like to do? " % (name))
    myres = True  
    corcount = 0
    wrcount = 0
    while corcount + wrcount  < int(myprobs):
	if myres == True:
		myeq = getnums()
		redo = 3
		myans = raw_input('\n*******\n%i + %i = ' % (myeq[0], myeq[1]))
		if int(myans) == myeq[2]:
			print "Correct! %d + %d = %d!\n" % (myeq[0], myeq[1], myeq[2])
			myres = True
			corcount = corcount + 1
		else:
			print 'Wrong. Try again!\n'
			myres = False
			redo = redo - 1
	else:
                
		myans = raw_input('\n*******\n%i + %i = ' % (myeq[0], myeq[1]))
                if int(myans) == myeq[2]:
                       	print "Correct!, %d + %d = %d!\n" % (name,myeq[0], myeq[1], myeq[2])
                	myres = True
			corcount = corcount + 1
			
		elif redo > 0:
	              	print 'Wrong. Try again! You have ' +str(redo)+ ' more tries.'
                       	myres = False
			redo = redo - 1
		else:
			myres = True
			wrcount = wrcount + 1 
    print "\n****************************************\n"
    print "Thanks for playing, %s!" % (name)
    print "You got %d correct and %d incorrect" % (corcount,wrcount)
    print "\n****************************************\n"

if __name__ == '__main__':
  main()
