while True:
    try:
        s = input()
        if not s:
            continue
        prev = s[0]
        resposta = s[0]
        for i in range(1, len(s)):
            if s[i] == ' ':
                resposta += ' '
                continue
            if s[i].isupper() and prev.islower() or s[i].islower() and prev.isupper():
                resposta += s[i]
                prev = s[i]
            elif s[i].isupper() and prev.isupper():
                resposta += s[i].lower()
                prev = s[i].lower()
            elif s[i].islower() and prev.islower():
                resposta += s[i].upper()
                prev = s[i].upper()
        print(resposta)
    except EOFError:
        break
