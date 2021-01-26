def shortestCompletingWord(licensePlate, words):
    
    def letter_count(string):
        letters = {}
        for char in string:
            if char.isalpha():
                if char.lower() not in letters:
                    letters[char.lower()] = 0
                letters[char.lower()] += 1
        return letters
    
    plate_letters = letter_count(licensePlate)
    shortest_len = float("inf")
    shortest_word = ""
    for word in words:
        cont = False
        word_letters = letter_count(word)
        for letter in plate_letters:
            if (letter not in word_letters or 
                word_letters[letter] < plate_letters[letter]):
                cont = True
                break
        if cont:
            continue
        if len(word) < shortest_len:
            shortest_len = len(word)
            shortest_word = word
    return shortest_word

#TESTING CODE
tests = [("1s3 PSt", ["step","steps","stripe","stepple"], "steps"),
         ("1s3 456", ["looks","pest","stew","show"], "pest"),
         ("Ah71752", ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"], "husband"),
         ("OgEu755", ["enough","these","play","wide","wonder","box","arrive","money","tax","thus"], "enough"),
         ("iMSlpe4", ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"], "simple")]
for test in tests:
    print(shortestCompletingWord(test[0], test[1]) == test[2])
