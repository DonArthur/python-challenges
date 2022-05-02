#if the word starts with consonant, moves it to the end and add 'ay'. if vowel just add 'way'
word = input('Give me a word: ')

if (word[0] == "a" or word[0] == "i" or word[0] == "u" or word[0] == "e" or word[0] == "o") :
    print((word + 'way').lower())
else :
    print((word[1:(len(word))] + word[0] + 'ay').lower())