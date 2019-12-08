#!/usr/bin/python

import os
import argparse
from pyPdf import PdfFileWriter, PdfFileReader


def create_parsers():

    p = argparse.ArgumentParser(
        prog='crop',
        description='"%(prog)s" split pdfs',
    )

    p.add_argument(
        '-i', '--input',
        type=str,
        required=True,
        help='Input pdf',
    )

    return p

if __name__ == '__main__':
    
	p = create_parsers()
	args = p.parse_args()

	input_filename = args.input
	output_filename = os.path.splitext(input_filename)[0]
	output_extension = os.path.splitext(input_filename)[-1]

	inputpdf = PdfFileReader(open(input_filename, "rb"))

	for i in xrange(inputpdf.numPages):
		output = PdfFileWriter()
		output.addPage(inputpdf.getPage(i))

		with open(output_filename + str(i) + output_extension, "wb") as outputStream:
			output.write(outputStream)
