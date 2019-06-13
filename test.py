"""Test file for languagedetector"""

from languagedetector import LanguageDetector

# Notre variable pour savoir quand arrêter la partie
text_to_detect = str()
ld = LanguageDetector()
ld.addDict('fr', 'dict/dico_fr.txt')
ld.addDict('en', 'dict/dico_en.txt')
ld.addDict('de', 'dict/dico_de.txt')
ld.addDict('es', 'dict/dico_es.txt')
ld.addDict('it', 'dict/dico_it.txt')
ld.addDict('ru', 'dict/dico_ru.txt')

while text_to_detect != 'quit':
    text_to_detect = input("Enter a sentence: ")
    print(ld.detect(text_to_detect))
