import re, glob, os
from bs4 import BeautifulSoup
import zip2srt as unzip

def create_corpus_from_srt_files(srt_dir = "data/marvel_movies_srt/srt/", output_file_name = "data/corpus.txt"):
    corpus = ""
    for file_name in glob.glob(srt_dir + "*.srt"):
        print("Processing: ", os.path.split(file_name)[-1])
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()

        text, cleantext = "", ""

        for line in lines:
            if re.search('^[0-9]+$', line) is None and re.search('^[0-9]{2}:[0-9]{2}:[0-9]{2}', line) is None and re.search('^$', line) is None:
                text += ' ' + line.rstrip('\n')
            text = text.lstrip()
            cleantext = BeautifulSoup(text, "lxml").text

        corpus = corpus + "\n\n" + cleantext


    with open(output_file_name, "w") as outfile:
        outfile.write(corpus)

    print("Corpus Saved:", output_file_name)



if __name__ == "__main__":
    unzip.unzip_files(zip_dir = "data/marvel_movies_srt/zip/", directory_to_extract_to = "data/marvel_movies_srt/srt/")
    create_corpus_from_srt_files(srt_dir="data/marvel_movies_srt/srt/", output_file_name="data/corpus.txt")