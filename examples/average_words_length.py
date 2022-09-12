"""
    For a given sentence, return the average word length.
    Note:
         Remember to remove punctuation first.
"""

sentence_1 = "Hi all, my name is Tom...I am originally from Australia."
sentence_2 = "I need to work very hard to learn more about algorithms in Python!"


def average_word_length(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')

    words = sentence.split()

    return round(sum(len(word) for word in words) / len(words), 2)


print(average_word_length(sentence_1))
print(average_word_length(sentence_2))
