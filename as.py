import inflect
p=inflect.engine()

from datetime import date

print(date.today())

words = p.number_to_words(12345)
print(words)
