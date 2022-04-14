from random import sample
import json


regex_not = "(?:^|(?<= ))([^dr]+)(?:\n|(?= )|$)"
regex_contains = "(\b\S\S\Se\S)+"
class Wordle:
    def __init__(self, word_length):
        all_words = open("words.json", "r")
        all_words = json.load(all_words)
        self.dictionary = all_words[str(word_length)]
        self.word = sample(self.dictionary, 1)[0]
        self.word_options = len(self.dictionary)
        self.combinations = []

    def guess(self, candidate_word):
        correct = []
        contains = []
        not_in = []
        temp_word = self.word
        for i in range(len(candidate_word)):
            letter = candidate_word[i]
            if letter == temp_word[i]:
                correct.append((letter, i))
                idx = temp_word.find(letter)
                temp_word = temp_word[0:idx]+"?"+temp_word[idx+1:]
            elif letter in temp_word:
                contains.append((letter, i))
                idx = temp_word.find(letter)
                temp_word = temp_word[0:idx]+"?"+temp_word[idx+1:]
            else:
                not_in.append(letter)

        return correct, contains, not_in
    

test = Wordle(5)
print(test.word)
print(test.word_options)
print(test.guess("sssss"))


