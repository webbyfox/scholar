import scholar
import csv

def read_data():
	with open ('Articles.csv' , 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=",")
		counter = 0;
		for row in spamreader:
			counter += 1;
			if counter != 1:
				article_title,article_type,article_author = row[1], row[2], row[3]
				print article_title, article_type, article_author
			
			if counter > 2:
				break;

if __name__ == "__main__":
	print "Starting reading csv..."
	read_data();
	print "Completed process..."