#Published by Rob van der Leek article
from __future__ import print_function
import random

Buzz = ('continuous testing', 'continuous integration', 'continuous deployment',
        'continuous improvement', 'devops')

Adjectives = ('complete', 'modern', 'self-service',
              'integrated', 'end-to-end')

Adverbs = ('remarkably', 'enormously', 'substantially',
           'significantly', 'seriously')

Verbs = ('accelerates', 'improves', 'enhances',
         'revamps', 'boosts')

'''Returns random words.'''
def sample(listin, num=1):
    result = random.sample(listin, num)
    if num == 1:
        return result[0]
    return result

'''Return  buzzwords.'''
def generate_buzz():
    buzz_terms = sample(Buzz, 2)
    phrase = ' '.join([sample(Adjectives), buzz_terms[0], sample(Adverbs), sample(Verbs), buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print(generate_buzz())
