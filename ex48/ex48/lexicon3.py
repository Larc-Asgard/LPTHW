lexicon = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb',
    'bear': 'noun',
    'princess': 'noun',
    'the': 'stop',
    'in': 'stop',
    'of': 'stop',
    "1234": 'number',
    '3 91234': 'number',
    '3': 'number',
    '91234': 'number',
    "ASDFASFASDF": 'error',
    "IAS": 'error'
}

def scan(sentence):
    words = sentence.split()
    result = []

    for word in words:
        pair = (lexicon[word], word)
        result.append(pair)


    return result
