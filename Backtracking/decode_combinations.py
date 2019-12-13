This problem was asked by Facebook.
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.


def decode_iter(message, vocab):
    if len(message) < 1:
        return []
    res = [vocab[x] for x in message]

    for i in range(1, len(message)):
        aux = []
        if i < len(message)-1:
            aux.append(vocab[message[i] + message[i+1]])
            aux.append(vocab[message[i]])
        if i > 1:
            aux.append(vocab[message[i]])
            aux.append(vocab[message[i-1] + message[i]])
        if len(message) == 2:
            aux.append(vocab[message])
        res.append(aux)
    return res


decoder = {str(x): chr(96+x) for x in range(1, 27)}
print(decoder)
print(decode_iter('111', decoder))
