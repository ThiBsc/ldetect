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
            with open(dicpath, 'r', encoding='utf-8') as dicfile:
                self.dic[isolang] = dicfile.read().split('\n')
        except IOError:
            print("Unable to open file {}".format(dicpath)) 

    def detect(self, text):
        ndict = len(self.dic)
        detection = None
        if ndict > 0:
            scores = dict.fromkeys(self.dic.keys(), 0)
            words = text.split(' ')
            for w in words:
                for iso in self.dic:
                    if w.lower() in self.dic[iso]:
                        scores[iso] += 1
            # Check if a language is alone on the podium
            iso_by_score = [k for k,v in sorted(scores.items(),
                                                key=lambda item: item[1],
                                                reverse=True)]
            firstScore = scores[iso_by_score[0]]
            if firstScore > 0:
                if ndict is 1:
                    detection = iso_by_score[0]
                elif ndict > 1:
                    secondScore = scores[iso_by_score[1]]
                    detection = iso_by_score[0] if firstScore > secondScore else None
            
        return detection

