import sys

sys.path.append('./display')
import colors as dclr

sys.path.append('./handler')
import reader as hreader

sys.path.append('./io')
import io_main, io_read, io_write

def main():
        io_main.greet('Blue')
        while True:
            choice = io_main.get_action()

            if choice == "r":
                question = "Are you sure you want to read and display the list's contents? [y/n]"
                choice = io_main.query_yes_no(question)

                if choice == "y":
                    io_read.read_and_display()
                else:
                    pass
            else:
                """
                question = "Are you sure you want to write entries in the list? [y/n]"
                choice = io_main.query_yes_no(question)

                if choice == "y":
                    io_write.write()
                else:
                    pass
                """

            return

	
if __name__ == '__main__':
	main()
