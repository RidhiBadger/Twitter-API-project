import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--word', type=str)

args = parser.parse_args()
# Print "Hello" + the user input argument
words = []
file = open("tweets.txt", "r")

#Splits each line into words 
for line in file: 
	string = line.lower().replace(',','').replace('.','').split(" ");  
	#Adding all words generated in previous step into words  
	for s in string:
		if s not in words:
			words.append(s);
print("Number of unique words is ", len(words))

file.close();
