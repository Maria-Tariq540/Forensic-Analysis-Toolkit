from PyPDF2 import PdfReader
from datetime import datetime


def format_pdf_date(date_string):

    try:

        if date_string.startswith("D:"):

            date_string = date_string[2:16]

            dt = datetime.strptime(
                date_string,
                "%Y%m%d%H%M%S"
            )

            return dt.strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    except:
        pass

    return str(date_string)


def analyze_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    metadata = reader.metadata

    results = {
        "Pages": len(reader.pages)
    }

    if metadata:

        for key, value in metadata.items():

            clean_key = str(key).replace("/", "")

            if "Date" in clean_key:
                results[clean_key] = format_pdf_date(
                    str(value)
                )
            else:
                results[clean_key] = str(value)

    return results