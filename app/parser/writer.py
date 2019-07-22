import csv

def write(filename):
	with open(filename, 'a', newline='') as books_list:
		books_writer = csv.writer(books_list, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		books_writer.writerow(["I am a title"] + ["I'm an author"] + ["I am a year"] + ["I am a publisher"])
