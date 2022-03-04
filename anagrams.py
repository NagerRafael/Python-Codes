def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)