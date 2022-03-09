def pig_it(text):
    result = []
    for w in text.split():
        if w.isalpha():
            w = w[1:] + w[0] + 'ay'
        result.append(w)
    return ' '.join(result)