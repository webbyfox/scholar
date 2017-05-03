import scholar
import csv
import subprocess

def read_data():
	with open ('Articles.csv' , 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=",")
		counter = 0;
		for row in spamreader:
			counter += 1;
			if counter != 1:
				article_title,article_type,article_author = row[1], row[2], row[3]
				# print article_title, article_type, article_author
				cmd = 'python scholar.py -c 1 --author ' + article_author + '--title ' + article_title
				p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
				out, err = p.communicate() 
				result = out.split('\n')
				for lin in result:
					for item in ['Title', 'URL','Citations']:
						if lin.find(item) != -1 and not lin.startswith('#'):
							# print(lin.strip())
				
							with open('result.csv', 'w') as csvfile:
							    fieldnames = ['Article', 'URL', 'Citation']
							    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

							    writer.writeheader()
							    writer.writerow({'Article': lin.strip(), 'URL': lin.strip(), 'Citation': lin.strip()})
							   

			if counter > 1:
				break;

if __name__ == "__main__":
	print "Starting reading csv..."
	read_data();
	print "Completed process..."