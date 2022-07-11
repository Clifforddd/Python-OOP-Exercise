"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """To return random words"""


    def __init__(self, path):

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):

        return [w.strip() for w in dict_file]

    def random(self):

        return random.choice(self.words)

    
class SpecialWF(WordFinder):
    """Read special character"""

    def parse(self, dict_file):

        return [i.strip() for i in dict_file
                if i.strip() and not i.startswith("#")]
