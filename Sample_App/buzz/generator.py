#Published by Rob van der Leek article
from __future__ import print_function
import random

BUZZ = ('continuous testing', 'continuous integration', 'continuous deployment',
        'continuous improvement', 'devops')

ADJECTIVES = ('complete', 'modern', 'self-service',
              'integrated', 'end-to-end')

ADVERBS = ('remarkably', 'enormously', 'substantially',
           'significantly', 'seriously')

VERBS = ('accelerates', 'improves', 'enhances',
         'revamps', 'boosts')


def sample(listin, num=1):
    '''Returns random words.'''
    result = random.sample(listin, num)
    if num == 1:
        return result[0]
    return result

def generate_buzz():
    '''Return  buzzwords.'''
    buzz_terms = sample(BUZZ, 2)
    phrase = ' '.join([sample(ADJECTIVES), buzz_terms[0], sample(ADVERBS),
                       sample(VERBS), buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print(generate_buzz())
