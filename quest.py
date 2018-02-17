life = 10 
import functions
def quest(desc, option1, option2, option3, effect1, effect2, effect3):
	print(desc)
	print("1 - ", option1)
	print("2 - ", option2)
	print("3 - ", option3)
	answer = input("What do you want to do? (Select 1, 2, or 3)")
	numberval = ["1","2","3"]
	if answer == "1":
		print(effect1)
	if answer == "2":
		print(effect2)
	if answer == "3":
		print(effect3)
	while answer not in numberval:
		print("Select again.")
		answer = input("What do you want to do? (Select 1, 2, or 3)")
	if "l" in effect1:
		effectnum = int(effect1[1])
		print(effectnum) 
		print(effect1[2])
		if effect1[2] == "l":
			global life
			life = life - effectnum
			print(life)
			