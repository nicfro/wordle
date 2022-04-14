from random import sample
import json
from collections import namedtuple

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

    def guess(candidate_word, word):
        result = []
        Rule = namedtuple('Rule', 'rule_name letter index')
        for i in range(len(candidate_word)):
            letter = candidate_word[i]
            if letter == word[i]:
                result.append(Rule("correct", letter, i))
                idx = word.find(letter)
                word = word[0:idx]+"?"+word[idx+1:]
            elif letter in word:
                result.append(Rule("contains", letter, i))
                idx = word.find(letter)
                word = word[0:idx]+"?"+word[idx+1:]
            else:
                result.append(Rule("not_in", letter, i))
        return result
    

test = Wordle(5)
print(test.word)
print(test.word_options)
print(test.guess("sssss"))


