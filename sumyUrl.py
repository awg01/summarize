from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import nltk
nltk.download('punkt')


LANGUAGE = "english"
SENTENCES_COUNT = 10

def summarize(url, length):
    # print("########################################## start of summary ##########################################")
    # url = "https://www.politifact.com/factchecks/2022/mar/15/michael-gableman/courts-have-repeatedly-upheld-grants-gableman-says/"
    SENTENCES_COUNT = length
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    # parser = PlaintextParser.from_string("Check this out.", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    summary = ""

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        # print(sentence)
        summary += str(sentence) + "\n"

    # print(summary)
    # print("########################################## end of summary ##########################################")
    return summary
