
def viz(text, keyword, lang):
    key = ""
    x = 0
    for letter in text:
        if letter in lang:
            key += list(keyword)[x]
            x += 1
            if x == len(keyword):
                x = 0
        else:
            key += letter
    cry = ""
    numlist = []
    for x in range(len(text)):
        if key[x] in lang:
            if lang.index(text[x]) + lang.index(key[x]) > len(lang):
                numlist.append((lang.index(text[x]) + lang.index(key[x])) - len(lang))
            else:
                numlist.append(lang.index(text[x]) + lang.index(key[x]))
        else:
            numlist.append(key[x])
    for el in numlist:
        if type(el) == int:
            cry += lang[int(el)]
        else:
            cry += str(el)
    return (cry)

#encrypt
def viz_enc(cry, keyword, lang):
    key = ""
    x = 0
    for letter in cry:
        if letter in lang:
            key += list(keyword)[x]
            x += 1
            if x == len(keyword):
                x = 0
        else:
            key += letter
    text = ""
    numlist = []
    for x in range(len(cry)):
        if key[x] in lang:
            if lang.index(cry[x]) - lang.index(key[x]) < 0:
                numlist.append((lang.index(cry[x]) - lang.index(key[x])) + len(lang))
            else:
                numlist.append(lang.index(cry[x]) - lang.index(key[x]))
        else:
            numlist.append(key[x])
    for el in numlist:
        if type(el) == int:
            text += lang[int(el)]
        else:
            text += str(el)
    return(text)
