import csv

def write(filename, rows):
	with open(filename, 'a', newline='') as books_list:
		books_writer = csv.writer(books_list, quotechar='"', quoting=csv.QUOTE_MINIMAL, escapechar=' ')
		books_writer.writerows(rows)
