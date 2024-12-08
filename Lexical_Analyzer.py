file = open("File1")

Articles = {'A': 'article', 'a': 'article', 'An': 'article', 'an': 'article',
            'The': 'article','the': 'article'}
Articles_key = Articles.keys()

helping_verb = {'am': 'helping_verb', 'have': 'helping_verb', 'do': 'helping_verb', 'are': 'helping_verb','as': 'helping_verb',
                'does': 'helping_verb','is': 'helping_verb','had': 'helping_verb','did': 'helping_verb',
                'was': 'helping_verb','can': 'helping_verb','may': 'helping_verb',
                'were': 'helping_verb','could': 'helping_verb','might': 'helping_verb','be': 'helping_verb',
                'should': 'helping_verb','must': 'helping_verb','being': 'helping_verb','will': 'helping_verb','been': 'helping_verb','would': 'helping_verb'}
helping_verb_key = helping_verb.keys()

punctuation_symbol = {'?': 'punctuation', '""': 'punctuation', '.': 'punctuation', ',': 'punctuaion','!': 'punctuaion'}
punctuation_symbol_key = punctuation_symbol.keys()

pronoun = {'I': 'pronoun','me': 'pronoun','my': 'pronoun','mine': 'pronoun','myself': 'pronoun','you': 'pronoun','yours': 'pronoun','yourself': 'pronoun','your': 'pronoun',
           'he': 'pronoun','He': 'pronoun','him': 'pronoun','himself': 'pronoun','his': 'pronoun','she': 'pronoun', 'her': 'pronoun','herself': 'pronoun',
           'it': 'pronoun','its': 'pronoun','itself': 'pronoun','we': 'pronoun','We': 'pronoun','us': 'pronoun','ourself': 'pronoun','our': 'pronoun','they': 'pronoun','They': 'pronoun','them': 'pronoun','themselves': 'pronoun'}
pronoun_key = pronoun.keys()

dataFlag = False

a = file.read()

count = 0
program = a.split("\n")
for line in program:
    count = count + 1
    print("line#", count, "\n", line)

    tokens = line.split(' ')

    print("Line#", count, "properties")
    for token in tokens:
        if token in Articles_key:
            with open("tokens.txt" , "a") as f1:
             f1.write(str([str(token)]) + ':' + Articles[token])
        if token in helping_verb_key:
            with open("tokens.txt", "a") as f1:
             f1.write(str([str(token)]) + ':' + helping_verb[token])
        if token in punctuation_symbol_key:
         with open("tokens.txt", "a") as f1:
             f1.write(str([str(token)]) + ':' + punctuation_symbol[token]+"\n")
        if token in pronoun_key:

            with open("tokens.txt", "a") as f1:
                f1.write(str([str(token)])  + ':' + pronoun[token]+"\n")

    dataFlag = False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")
