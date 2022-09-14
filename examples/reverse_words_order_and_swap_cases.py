
def reverse_words_order_and_swap_cases(sentence):
    length = len(sentence)

    new_sentence = "".join([sentence[length - i] for i in range(length)])

    sentence = ""

    for c in new_sentence:
        if c.isupper():
            sentence += c.lower()
        else:
            sentence += c.upper()

    return sentence


reverse_words_order_and_swap_cases("aWESOME is cODING")
