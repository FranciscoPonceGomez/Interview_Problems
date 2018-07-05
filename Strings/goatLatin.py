# Goat Latin is a made-up language based off of English, sort of like Pig Latin.
# The rules of Goat Latin are as follows:
# 1. If a word begins with a consonant, remove the first
#    letter and append it to the end, then add 'ma'.
#    For example, the word 'Goat' becomes 'oatGma'.
#    list of vouals
# 2. If a word begins with a vowel, append 'ma' to the end of the word.
#    For example, the word 'Uber' becomes 'Uberma'.
# 3. Add one letter "a" to the end of each word per its word index in the
#    sentence, starting with 1. That is, the first word gets "a" added to the
#    end, the second word gets "aa" added to the end, the third word in the
#    sentence gets "aaa" added to the end, and so on.

# Write a function that, given a string of words making up one sentence, returns
# that sentence in Goat Latin. For example:
#
#  string_to_goat_latin('Uber loves Goat Latin')
#
# would return: 'Ubermaa oveslmaaa oatGmaaaa atinLmaaaaa'

# input: String
# output: String
CHARACTERS = 'ma'

def toGoatLatin(S):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    wordList = S.split(' ')
    for i in range(0,len(wordList)):
        if wordList[i][0] not in vowels:
            wordList[i] = processFirstCase(wordList[i], CHARACTERS)
        else:
            wordList[i] = processSecondCase(wordList[i], CHARACTERS)
        wordList[i] +=  (i+1) * 'a'
    return ' '.join(wordList)
        
def processFirstCase(word, characters):
    word = word[1:] + word[0]
    return processSecondCase(word, characters)
    
def processSecondCase(word, characters):
    return word + characters
    
string_to_goat_latin = 'Uber loves Goat Latin'
print(toGoatLatin(string_to_goat_latin))

