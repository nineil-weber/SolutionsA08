num = 0
l = []
flag=True
while num < 0 or num > 100  or flag==True:
	try:
		num = int(input("Enter a score:"))
		if num < 0 or num > 100:
			raise Exception("Value must be between 0 and 100")
		else:
			l.append(num)
			o = input("Press s to enter another score or press c to calculate: ")
			if o =="c":
				flag=False

	except ValueError:
		print("\nSorry, the scores must be a number.\n")
	except:
		print("\nSorry, the scores must be positive and between [0-100].\n")

print("\n")
print("High: "+ str(max(l)))
print("Low: "+ str(min(l)))
print("Average: "+ str(int( sum(l) / len(l))))
print("Number of Students: "+str(len(l)))
print("\n")
