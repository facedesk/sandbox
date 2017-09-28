story = '''
Once upon a time in a small village lived four Brahmins named Satyanand, Vidhyanand, Dharmanand and Sivanand. They had grown up together to become good friends. Satyanand, Vidhyanand and Dharmanand were very knowledgeable. But Sivanand spent most of his time eating and sleeping. He was considered foolish by everyone. 

Once famine struck the village. All the crops failed. Rivers and lakes started to dry up. The people of the villages started moving to other villages to save their lives. 

“We also need to move to another place soon or else we will also die like many others," said Satyanand. They all agreed with him. 
'''
village = input("enter a noun:")
lived = input("enter a verb:")
crops = input("enter a noun:")
good = input("enter an adjective:")
eating = input("enter a verb:")
story = story.replace("village",village)
story = story.replace("lived",lived)
story = story.replace("crops",crops)
story = story.replace("good",good)
story = story.replace("eating",eating)
print(story)
