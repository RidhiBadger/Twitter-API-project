# Twitter-API-project
Objective - Downloading the tweets from Twitter API, storing them in a text file, calculating frequency of the given word and then calculating the trendiness score

Step1 - Set up a Developer Account with Twitter, the crdentials will be required to extract tweets from the API.
Step2 - Run server.py using the command - < python server.py > on the virtual machine. The code with use Argparse python library to read the tweets from twitter, clean them and select the tweets in english language, input timestamp, userid and tweet in the text file tweets.txt
Step3 - Run the command - < python word_count.py --word WORD > to count the number of times the given WORD occurs in the sampled tweets. 
Step4 - Run the comman - < python vocabulary_size.py > to calculate the number of unique words in the sampled tweets file.  
