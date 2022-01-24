# Import the library
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--word', type=str, required=True)

# Parse the argument
args = parser.parse_args()
# Print "Hello" + the user input argument
print('To search the following word in the text file: ', args.word)

count = 0;  
words = []; 
       
#Opens a file in read mode  
file = open("tweets.txt", "r")  
 
    
for line in file:  
	#Splits each line into words  
	string = line.lower().replace(',','').replace('.','').split(" ");  
        #Adding all words generated in previous step into words  
	for s in string: 
		words.append(s);

		  
for i in range(0, len(words)):
	if(words[i] == args.word):  
		count = count +1;
		i = i+1;
	else:
		i = i+1;  
print("Count of the word ", args.word+ " is", count)
#print(words[2])
#print(args.word)
#print(len(words))	
file.close();           
          
