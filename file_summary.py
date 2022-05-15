from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def file_summary(decoded_file_data, length):
    # For Strings
    parser = PlaintextParser.from_string(decoded_file_data,Tokenizer("english"))

    # Using TextRank
    summarizer = TextRankSummarizer()
    #Summarize the document with 2 sentences
    summary_tuples = summarizer(parser.document, length)
    file_summary = ""
    for tuple in summary_tuples:
        file_summary+=str(tuple)

    # print("file summary")
    # print(file_summary)
    # print("****")
    return file_summary


import fitz # install using: pip install PyMuPDF
# with fitz.open("research.pdf") as doc:

def pdf_summary(fileName):
    fileName = "pdfFile.pdf"
    with fitz.open(fileName) as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    print(text)


# if __name__ == "__main__":
#     file_summary(1)
