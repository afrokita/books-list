import sys

sys.path.append('../display')
import colors as dclr

sys.path.append('../handler')
import reader as hreader

def read_and_display():
    csv_data = hreader.read('list.csv')
    header_count = csv_data[0]
    content = csv_data[1]

    elements_printed = 0
    dclr.foreground_paint('Yellow', '')
    for element in content:
            dclr.foreground_paint('Yellow', element)
            elements_printed += 1

            if elements_printed % header_count == 0:
                    dclr.foreground_paint('Blue', '----')
