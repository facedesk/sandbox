story = '''
Once upon a time in a small village lived four Brahmins named Satyanand, Vidhyanand, Dharmanand and Sivanand. They had grown up together to become good friends. Satyanand, Vidhyanand and Dharmanand were very knowledgeable. But Sivanand spent most of his time eating and sleeping. He was considered foolish by everyone. 

Once famine struck the village. All the crops failed. Rivers and lakes started to dry up. The people of the villages started moving to other villages to save their lives. 

“We also need to move to another place soon or else we will also die like many others," said Satyanand. They all agreed with him. 
'''

changers = {}
while(input("replace word? y/n").lower() == "y"):
	print(story)
	changers[input("Write a word that you'd like to change from the story:")]= input("What would you like to change it to?:")
print("okay")
for key,value in changers.items():
	story = story.replace(value,key)
print(story)


