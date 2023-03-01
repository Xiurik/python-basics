import sys

from PyPDF2 import PdfMerger, PdfReader, PdfWriter


# ? Open a pdf and rotate 90 degrees
def rotatePdf(filePath, outRotated):
    with open(filePath, "rb") as file:
        reader = PdfReader(file)
        page = reader.getPage(0)
        page.rotateCounterClockwise(90)
        writer = PdfWriter()
        writer.addPage(page)
        with open(outRotated, "wb") as nf:
            writer.write(nf)


# ? Merge pdfs
inputs = sys.argv[1:]


def mergePdfs(files, outFileName):
    merger = PdfMerger()
    for p in files:
        merger.append(f"exercises/pdf/{p}")

    merger.write(outFileName)


# ? Pdf Watermark
def watermarkPdf(pdfToMark, waterPdf, outPdfName):
    reader = PdfReader(pdfToMark)
    page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()
    for i in page_indices:
        content_page = reader.pages[i]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(waterPdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(outPdfName, "wb") as fp:
        writer.write(fp)


if __name__ == "__main__":
    # rotatePdf('exercises/pdf/dummy.pdf','exercises/pdf/test.pdf')
    # mergePdfs(inputs, 'exercises/pdf/mergedFile.pdf')
    watermarkPdf("exercises/pdf/mergedFile.pdf", "exercises/pdf/wtr.pdf", "exercises/pdf/watered.pdf")
