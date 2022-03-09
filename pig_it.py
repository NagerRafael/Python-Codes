def pig_it(text):
    text = text.split(" ")
    result = []
    for w in text:
        if w.isalpha():
            w = w[1:] + w[0] + 'ay'
        result.append(w)
    return ' '.join(result)