def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]
    return "Length: {:d} - First character: {}".format(length, first)


print(multiple_returns("At Holberton school, I learnt C!"))