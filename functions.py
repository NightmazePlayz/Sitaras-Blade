def logo():
	print(""" 
 ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
                                      .$"
                                     "
""")
print("""
  ________.__  __                   /\          __________.__             .___      
 /   _____|___/  |______ ___________)/   ______ \______   |  | _____    __| _/____  
 \_____  \|  \   __\__  \\_  __ \__  \  /  ___/  |    |  _|  | \__  \  / __ _/ __ \ 
 /        |  ||  |  / __ \|  | \// __ \_\___ \   |    |   |  |__/ __ \/ /_/ \  ___/ 
/_______  |__||__| (____  |__|  (____  /____  >  |______  |____(____  \____ |\___  >
        \/              \/           \/     \/          \/          \/     \/    \/ 
""");
def prolougeresponse():
	prolougeHavePlayed = input("Welcome! Have you played before? (Y/N)")
	if prolougeHavePlayed == "y":
		 print("Welcome Back! Select your Player!")
	if prolougeHavePlayed == "n":
		story = input("Would you like to know the story?(Y/N)")
		if story == "y":
			print("Once upon a time there was a blacksmith named Sitara. He was renowned by his town, and known for the best weapons in the world. One night, a man came and visited him. He hired him to make a blade, and gave him the materials to do so. After long hours in the forge, the man beheld his creation in horror. This was no ordinary blade, and it held the power to slay gods. In an attempt to fix his mistake, he tried to destroy the blade. He failed and the man took his life. The blade, however, was lost, and ever since he has looked for it, for he who holds the blade is mightier than any mortal.")
			searchforblade = input("Do you want to search for the blade? (Y/N)")
			if searchforblade == "y":
				print("Awesome!")
			while searchforblade != "y":
				print("Choose again! :-(")
				searchforblade = input("Do you want to search for the blade? (Y/N)")
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


	

