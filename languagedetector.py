class LanguageDetector:
    """Class to detect the language of a text
    with two approach (dictionnary and letter frequency)
    Members:
    - dic"""

    def __init__(self):
        """dic such as:
        {'fr', ['bonjour', 'maison'']}
        {'en', ['hello', 'house'']}"""
        self.dic = dict()

    def addDict(self, isolang, dicpath):
        try:
            with open(dicpath, 'r') as dicfile:
                self.dic[isolang] = dicfile.read().split('\n')
        except IOError:
            print("Unable to open file {}".format(dicpath)) 

    def detect(self, text):
        scores = dict.fromkeys(self.dic.keys(), 0)
        words = text.split(' ')
        for w in words:
            for iso in self.dic:
                if w.lower() in self.dic[iso]:
                    scores[iso] += 1
        return max(scores, key=scores.get)

