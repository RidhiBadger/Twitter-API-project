from datetime import datetime
import psycopg2
import argparse
import time
import math

#current_time = datetime.now().replace(microsecond=0,second=0) 
current_time = ["2021-12-05 12:12:00", "2021-12-05 12:11:00"] #FOR TESTING PURPOSES 
connection = psycopg2.connect("dbname=twitteranalysis user=gb760")
cursor = connection.cursor()
parser = argparse.ArgumentParser() 
parser.add_argument('--word',type=str,nargs='*',help='please type any word or phrase')
args = parser.parse_args()

word_search = args.word
word_count0 = []
vocab_size0 = []

if __name__ == '__main__':
	if args.word == None or args.word==[]:
		print('Please input the word or phrase')
	else:
		word_search = word_search[0]
		word_count = """select count(*) from words WHERE words = %s and time = %s;"""
		for i in range(2):
			values = (word_search, current_time[i])
			cursor.execute(word_count,values)
			connection.commit()
			result = cursor.fetchone()
			word_count0.append(result[0])
			#WE DO NOT HAVE ANY TWEETS IN OUR TABLE WITH TIME EQUAL TO 18:13:00 BUT THE CODE WORKS
			##where word = %s and time=%s

for i in range(2):
	connection = psycopg2.connect("dbname=twitteranalysis user=gb760")
	cursor = connection.cursor()
	vocab_size = """select count(distinct words) from words WHERE time = %s;"""
	cursor.execute(vocab_size,(current_time[i],))
	connection.commit()
	result = cursor.fetchone()
	vocab_size0.append(result[0])

probability = (1+word_count0[0])/vocab_size0[0]
probability1 = (1+word_count0[1])/vocab_size0[1]
log_prob = math.log10(probability)
log_prob1 = math.log10(probability1)
trendiness = log_prob/log_prob1 #there was also a formula for subtract?
print(trendiness)
#CALL WITH --word hello




