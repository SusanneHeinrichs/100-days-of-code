#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Names/invited_names.txt") as names_file:
    for name in names_file:
        start = open("Input/Letters/starting_letter.txt", "rt")
        output = open("Output/ReadyToSend/out_"+ name +".txt", "wt")
        #go through lines in starting_letter and replace name placeholder with name from list 
        for line in start:
	        output.write(line.replace('[name]', name.replace('\n', '')))
        #close start and output files
        start.close()
        output.close()

