"""
    Given two sentences, return an array that has the words that appear in one sentence and not
    the other and an array with the words in common.
"""

sentence_1 = 'We are really pleased to meet you in our city'
sentence_2 = 'The city was hit by a really heavy storm'


def match_and_mismatch_words(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    # ^ A.symmetric_difference(B), & A.intersection(B)
    return sorted(list(set1 ^ set2)), sorted(list(set1 & set2))


print(match_and_mismatch_words(sentence_1, sentence_2))
