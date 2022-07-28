def runLengthEncode(text):
    result = ''
    a = ''
    count = 1
    for char in text:
        if char != a:
            if a:
                result += str(count) + a
            count = 1
            a = char
        else:
            count += 1
    else:
        result += str(count) + a
        return result


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:

        if char.isdigit():

            count += char
        else:

            decode += char * int(count)
            count = ''
    return decode


a = 'AAAAAAAccmmmmmNNNNNNNNzzzGGGGGGGFFFFFFFFF'
b = runLengthEncode(a)
c = rle_decode(b)
print(b)
