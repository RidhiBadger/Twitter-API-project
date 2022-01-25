from datetime import datetime

#current_time = datetime.now().replace(microsecond=0,second=0) 
current_time = "2021-12-05 12:12:00" # FOR TESTING PURPOSES 
import psycopg2
import argparse
from datetime import datetime
import time
connection = psycopg2.connect("dbname=twitteranalysis user=gb760")
cursor = connection.cursor()
parser = argparse.ArgumentParser() 
parser.add_argument('--word',type=str,nargs='*',help='please type any word or phrase')
args = parser.parse_args()

word_search = args.word

if __name__ == '__main__':
	if args.word == None or args.word==[]:
		print('Please input the word or phrase')
	else:
		word_search = word_search[0]
		word_count = """select count(*) from words WHERE words = %s and time = %s;"""
		values = (word_search, current_time)
		cursor.execute(word_count,values)
		connection.commit()
		result = cursor.fetchone()
		print(result[0])
	##where word = %s and time=%s
	





