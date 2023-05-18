import re
sentence = 'Start a sentence and bring it to an end'
pattern = re.compile(r'start',re.IGNORECASE)
matches = pattern.match(sentence)
print(matches)