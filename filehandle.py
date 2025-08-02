print("List maker")
while True:
	print("\nEnter [c] for creating tasks,[d] for display,[del] for deleting all notes,[b] for exit")
	Input = input("Enter:")
	if Input == 'c':
		file = open('lister.txt','a')
		g = str(input("Enter your notes:\n"))
		file.write(g+"\n")
		#file.write()
		file.close()
		print("Notes saved")
	elif Input == 'd':
		print("Your notes are:")
		h = open('lister.txt','r')
		print(h.read())
		h.close()
	elif Input == 'del':
		file = open('lister.txt','w')
		file.write("")
		file.close()
		print("Deleted succesfully")
	elif Input == 'b':
		break