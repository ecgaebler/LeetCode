def countSegments(s):
    segments = 0
    last_char_was_space = True
    for char in s:
        if char == " ":
            last_char_was_space = True
        else:
            if last_char_was_space:
                last_char_was_space = False
                segments += 1
    return segments


#TESTING CODE BELOW THIS POINT
tests = [
    "Hallo",
    "multiple words (and punctuation!) in this sentence.",
    "",
    " ",
    "   ",
    ]
answers = [1, 7, 0, 0, 0]
for i in range(len(tests)):
    print(countSegments(tests[i]) == answers[i])
