# Twitter-API-project
**PROJECT PART A**
Objective - Downloading the tweets from Twitter API, storing them in a text file, calculating frequency of the given word (basis User input) and then calculating the trendiness score

Step1 - Set up a Developer Account with Twitter, the credentials will be required to extract tweets from the API.

Step2 - Run server.py using the command - < python server.py > on the virtual machine. The code will use Argparse python library to read the tweets from twitter. Further we clean the tweets and select only the tweets that are in english language. For all tweets read, we store the input timestamp, userid and tweet in the text file tweets.txt

Step3 - Run the command - < python word_count.py --word WORD > to count the number of times the given WORD occurs in the sampled tweets. 

Step4 - Run the command - < python vocabulary_size.py > to calculate the number of unique words in the sampled tweets file.  

Step5 - Run command < python wordintweet.py > to print tweets with the given word <#life> since the given date. We can limit the number of responses to n (=10 in this case)

**PROJECT PART B**
Repeat the above steps by using a datawarehouse (a PostgresSQL datawarehouse) instead of a data lake. Here I will use Python to write and access my tweets from the database

Step 1 - Select schema for the table to store tweets. Here since the goal is to store trendiness score in the given minute, the table will have 3 columns - word, timestamp (upto minute) and the number of occurences. Allocating a column for number of occurences will lead to optimal utilization of memory. 

Step 2 - Run server_postgres.py on the virtual machine. This will read the tweets from Twitter API and store them word by word, as per the format in the previous step. Here we use psycopg2 python library to read/write from/to Postgres SQL

Step 3 - Run word_count_postgres.py --word <life> to calculate the frequency of the word in the tweets in the given minute.
  
Step 4 - vocabulary_size_postgres.py will calculate the number of unique words used in the tweets in the given minute. 
  
Step 5 - Calculate the trendiness score using trendiness_postgres.py

