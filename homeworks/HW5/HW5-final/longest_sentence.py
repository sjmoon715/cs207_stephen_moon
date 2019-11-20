import sys
from linked_list import LinkedList, Nil
sys.setrecursionlimit(2000)

def get_list_of_sentences(chapter1='swansway-chapter1.txt'):
    def to_sentences(p):
            for delimiter in '.?!': p = p.replace(delimiter, '|')
            return [s.strip('\" ') for s in p.split('|')]
    with open(chapter1, 'r', encoding='UTF-8') as f:
        paragraphs = f.readlines()

    sentences = [s for p in paragraphs for s in to_sentences(p) if len(s) > 1]
    list_of_sentences = Nil()
    for s in sentences[::-1]:
        list_of_sentences = list_of_sentences.prepend(s)
    return list_of_sentences


def longest_sentence():
    # initializes list of sentences
    list_of_sentences = get_list_of_sentences()
    # returns the word count of each sentence in the list
    def count(f):
        return len(f.split())
    # compares sentences a and b and returns the longer one
    def compare(a,b):
        return a if a>b else b
    
    counts = list_of_sentences.for_each(count)
    longest_sentence = counts.reduce_right(compare)
    return longest_sentence

print(longest_sentence())