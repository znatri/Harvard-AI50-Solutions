import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = dict()
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        if os.path.isfile(path):
            f = open(path)
            files[file] = f.read()
    return files

def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    words = list(
        word for word in nltk.word_tokenize(document.lower())
        if word not in nltk.corpus.stopwords.words("english") and \
            not all(char in string.punctuation for char in word)
    )
    
    return words

def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    file_idfs = dict()
    
    # Count the no. of files the word appears in
    for words in documents.values():
        for word in words:
            if word not in file_idfs:
                file_idfs[word] = 1
            else: 
                file_idfs[word] += 1
    
    # Calculate the IDFs of the word based on frequency
    tot_docs = len(documents.keys())
    for word, num_docs in file_idfs.items():
        file_idfs[word] = math.log(tot_docs/num_docs) 
    
    return file_idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tf_idf = list()
    idfs_ranking = dict()

    for file in files:
        val = float(0)
        for word in query:
            if word in files[file]:
                val += idfs[word]
                if files[file] not in tf_idf:
                    tf_idf.append(file)
        idfs_ranking[file] = val

    tf_idf.sort(key=idfs_ranking.get)

    for i in range(n):
        if len(tf_idf) != n:
            tf_idf.pop()

    return tf_idf

def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
