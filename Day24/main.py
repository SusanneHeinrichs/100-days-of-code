#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as names_file:
    for name in names_file:
        output = open("Output/ReadyToSend/out_"+ name +".txt", "wt")
        start = open("Input/Letters/starting_letter.txt", "rt")
        for line in start:
	        output.write(line.replace('[name]', name.replace('\n', '')))
#close input and output files
start.close()

