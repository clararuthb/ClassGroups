#the ClassGroups program creates randomized groups of any size from a student roster.

import sys,random,os,time
#these are called modules

def na(w):
	while w != "yes" and w != "no":
		w = raw_input("please enter either \"yes\" or \"no\"\t")
	return w
	
def prnoun(namelist):
	for x in range(len(namelist)):
		namelist[x]	= namelist[x][0].upper() + namelist[x][1:]
	return namelist

def prname(name):
	return name[0].upper() + name[1:]

input = "C:/bin/ClassGroups/Students.txt"

roster_input = open(input, "r")
roster = roster_input.read()
roster_input.close()

roster = roster.lower(). split("\n")
todayroster = []

confirm = "nothing yet"
while confirm != "yes":
	absent = raw_input("\nEnter the names of absent students, separated by commas and spaces (e.g Kirk, Spock, Uhura) or if none, type \"none\": \n").lower().split(", ")
	for noshow in absent:
		while noshow not in roster:
			print "\nthis \"" + noshow + "\" is not on the list."
			noshow = raw_input("Re-enter student name or confirm \"none\" ").lower()
			if noshow in roster:
				absent.append(noshow)
			elif noshow == "none":
				break
	for noshow in absent:
		if noshow not in roster:
			absent.remove(noshow)
		
	print "\nso these students are absent: " + ", ".join(prnoun(absent)) + "\n"
	print "Remember, you can still add students back on the roster while this program is running by typing that student's name into the input field later."
	confirm = raw_input("confirm absences? ").lower()
	confirm = na(confirm)
	time.sleep(1)

if confirm == "yes":
	for student in roster:
		student = prname(student)
		if student not in absent:
			todayroster.append(student)
	print "\n===================================================================\n"
	time.sleep(1)
	print "DIRECTIONS:"
	print "You will be given an input line"
	print "To add a late student back onto the roster, enter that student's name."
	print "For 3 groups of students, enter \"3 groups\", for example."
	print "Or, for groups of 3 students, enter \"groups of 3\""
	print "To exit the program, enter \"exit\"\n"
	print "\n===================================================================\n"
	print "Today's roster is:\n", "\n".join(prnoun(todayroster)), "\n"
while confirm == "yes":
	mainvar = raw_input("Input: ")
	if mainvar == "exit" or mainvar == "Exit":
		sys.exit()
	elif prname(mainvar) in absent:
		todayroster.append(mainvar)
	else:
		random.shuffle(todayroster)
		assngroups = []
		try:
			#x = 0
			groupnum = int(mainvar[0])
			#grpsze = (len(todayroster))/groupnum
			for each in range(groupnum):
				assngroups.append([])
				#while x < len(todayroster) - len(todayroster)%groupnum:
			#print assngroups
			y = 0
			for student in todayroster:
				assngroups[y].append(student)
				#print assngroups[y]
				if y < groupnum-1:
					y = y + 1
				else:
					#print y
					y = 0
			print "\n===============================================================\n"
			for each in range(groupnum):
				print ", ".join(assngroups[each]) + "\n\n"
			time.sleep(5)
			print "JESUS WEPT!\n"
		except:
			groupsize = int(mainvar[len(mainvar)-1])
			#print groupsize
			grpnum = (len(todayroster))/groupsize
			for each in range(grpnum):
				assngroups.append([])
			y = 0
			for student in todayroster:
				assngroups[y].append(student)
				if y < grpnum-1:
					y = y + 1
				else:
					y = 0
			print "\n================================================================\n"
			for each in range(grpnum):
				print ", ".join(assngroups[each]) + "\n\n"
			time.sleep(5)
			print "JESUS WEPT!\n"