import csv

def read(filename):
	with open(filename, newline='') as books_list:
		books_reader = csv.DictReader(books_list, quotechar='"')
		header_row = next(books_reader)
		headers = ([*header_row])
		"""
		Necessary, since DictReader is an iterator
		and we want to grab the first row too
		"""
		content = list()
		for header in headers:
			content.append(f"{header}: {header_row[header]}")
		for entry in books_reader:
			for header in headers:
				content.append(f"{header}: {entry[header]}")

	return [len(headers), content]
