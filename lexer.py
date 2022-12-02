SYMBOLS = ['(',
           ')',
           ';',
           ',',
           ':',
           '\'',
           '"']

KEYWORDS = {'t': ['int'],
            'p':['main'],
            'f':['begin'],
            'd':['end'],
            'i':['if'],
            'b':['printf'],
            'o':['relop']
            }

OPERATORS = ['>', '<', '=','==','<=','>=']
line_count = 0


def getIndex(word):
    keys = list(KEYWORDS.keys())
    values = list(KEYWORDS.values())
    for value in values:
        if word in value:
            i = values.index(value)
            return keys[i]


def get_tokens(filename):
    tokens = []
    F = open(filename, encoding="utf8")
    for line in F:
        for word in line.split():
            token = getIndex(word)
            if token in KEYWORDS:
                tokens.append(token)
            else:
                cur = '-'
                buf = ''
                for i in word:
                    if i in SYMBOLS:
                        if len(buf)!=0:
                            token = getIndex(buf)
                            if token in KEYWORDS:
                                tokens.append(token)
                                buf = ''
                            elif buf in OPERATORS:
                                tokens.append('o')
                            elif buf.isnumeric():
                                tokens.append('n')
                            else:
                                tokens.append('v')
                        buf = ''
                        cur = '-'
                        tokens.append(i)
                    elif i.isalnum():
                        if cur=='o':
                            tokens.append('o')
                            buf = i
                            cur = 'l'
                        else:
                            buf = buf+i
                            cur = 'l'
                    else:
                        if cur=='l':
                            token = getIndex(buf)
                            if token in KEYWORDS:
                                tokens.append(token)
                            elif buf.isnumeric():
                                tokens.append('n')
                            else:
                                tokens.append('v')
                            buf = i
                            cur = 'o'
                        else:
                            buf = buf+i
                            cur = 'o'
                if len(buf)!=0:
                    token = getIndex(buf)
                    if token in KEYWORDS:
                        tokens.append(token)
                    elif buf in OPERATORS:
                        tokens.append('o')
                    elif buf.isnumeric():
                        tokens.append('n')
                    else:
                        tokens.append('v')    

    return tokens
