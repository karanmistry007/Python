def secretCode():
    import string
    import random

    word = str(input("Enter The Word: "))
    code = ""
    decode = ""
    letters = string.ascii_lowercase
    rand1 = "".join(random.choice(letters) for i in range(3))
    code += str(rand1)
    if len(word) > 3:
        # for coding
        for i in word:
            if word.index(i) == 0:
                last = i
                continue
            code += str(i)

        code += str(last)
        rand2 = "".join(random.choice(letters) for i in range(3))
        code += str(rand2)

        # for decoding
        decode += code[-4]
        decode += code[3:-4]

    else:
        # for coding
        code = word[::-1]

        # for decoding
        decode = code[::-1]

    print("Secret Code is: ", code)
    print("Decoded word: ", decode)


secretCode()
