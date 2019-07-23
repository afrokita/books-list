import csv

def read(filename):
	with open(filename, newline='') as books_list:
		books_reader = csv.DictReader(books_list, quotechar='"')
		header_row = next(books_reader)
		headers = ([*header_row])
		"""
		Necessary, since DictReader is an iterator
		and we want to print the first row too
		"""
		for header in headers:
			print(f"{header}: {header_row[header]}")
		for entry in books_reader:
			for header in headers:
				print(f"{header}: {entry[header]}")

read('list.csv')
