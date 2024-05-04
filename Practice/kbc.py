que = [
    "How many zeroes are ther in one million ?",
    "Name The Biggest Country in The World: ",
    "Who was the first Prime Minister of India",
]
cor = ["six", "russia", "nehru"]
ans = [
    "three",
    "four",
    "five",
    "six",
    "russia",
    "india",
    "usa",
    "china",
    "gandhiji",
    "nehru",
    "sardar patel",
    "bhagat singh",
]
o = 0
r = 0
for i in range(0, len(que)):

    print("Question : ", que[i])
    print("a: ", ans[o])
    print("b: ", ans[o + 1])
    print("c: ", ans[o + 2])
    print("d: ", ans[o + 3])
    o = o + 4

    use = input("Enter the correct Answer: ")
    if use == cor[i]:
        print("Your Answer is Correct")
        r = r + 15000
    else:
        print("Your Answer is Wrong")
        print("You Won ", r, " rupees")
        break

    print("You Won ", r, " rupees")

    print("\n------------------------------------------------", end="\n\n")
