import argparse

from pyPdf import PdfFileWriter, PdfFileReader


def create_parsers():

    p = argparse.ArgumentParser(
        prog='crop',
        description='"%(prog)s" crop pdfs',
    )

    p.add_argument(
        '-i', '--input',
        type=str,
        nargs='*',
        required=True,
        help='Input pdf',
    )

    p.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help='Output pdf',
    )

    return p


if __name__ == '__main__':
    
    p = create_parsers()
    args = p.parse_args()

    input_filename = args.input
    output_filename = args.output

    if len(input_filename) < 2:
        raise("Input must contain more than one document")

    for i in range(len(input_filename)-1):
        left_pdf  = PdfFileReader(file(input_filename[i], "rb"))
        right_pdf = PdfFileReader(file(input_filename[i+1], "rb"))
        output = PdfFileWriter()

        # get the first page from each pdf
        left_page = left_pdf.pages[0]
        right_page = right_pdf.pages[0]

        page = output.addBlankPage(
            width=left_page.mediaBox.getWidth() + right_page.mediaBox.getWidth(),
            height=max(left_page.mediaBox.getHeight(), right_page.mediaBox.getHeight()),
        )

        # draw the pages on that new page
        page.mergeTranslatedPage(left_page, 0, 0)
        page.mergeTranslatedPage(right_page, left_page.mediaBox.getWidth(), 0)

        # write to file
        outputStream = file(output_filename, "wb")
        output.write(outputStream)
        outputStream.close()
