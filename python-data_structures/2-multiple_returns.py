# def multiple_returns(sentence):
#     length = len(sentence)
#     if length == 0:
#         first = None
#     else:
#         first = sentence[0]
#     return "Length: {:d} - First character: {}".format(length, first)


def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    else:
        return len(sentence), sentence[0]


sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
