import csv

def write(filename, **kwargs):
	title = kwargs.get('title', "None")
	author = kwargs.get('author', "None")
	year = kwargs.get('year', "None")
	publisher = kwargs.get('publisher', "None")
	with open(filename, 'a', newline='') as books_list:
		books_writer = csv.writer(books_list, quotechar='"', quoting=csv.QUOTE_MINIMAL)
		books_writer.writerow([title] + [author] + [year] + [publisher])
