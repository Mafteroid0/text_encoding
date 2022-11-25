def atbash(s, abc):
    return s.translate(str.maketrans(abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))
