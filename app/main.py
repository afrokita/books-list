import display.cli as dcli
import handler.reader as hreader

def main():
	dcli.init()

	dcli.background_paint('Blue', "Greetings!")

	csv_data = hreader.read('list.csv')
	header_count = csv_data[0]
	content = csv_data[1]

	elements_printed = 0
	for element in content:
		dcli.foreground_paint('Yellow', element)
		elements_printed += 1

		if elements_printed % header_count == 0:
			dcli.foreground_paint('Yellow', '')

	dcli.deinit()

if __name__ == '__main__':
	main()
