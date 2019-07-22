import csv

def read(filename):
	with open(filename, newline='') as books_list:
		books_reader = csv.reader(books_list, delimiter=' ', quotechar='|')
		for row in books_reader:
			print(', '.join(row))
