'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
Bonus points (not really, but just for fun):
1. Avoid creating an array whose memory footprint is roughly as big as the input text.
2. Avoid sorting the entire array of unique words.
'''


def top_3_words(text):
    for char in text:
        if not (char.isalpha() or char == "'"):
            text = text.replace(char,' ')
    words,counts,out = [],[],[]

    for word in list(filter(None,text.lower().split())):
        if all([not c.isalpha() for c in word]):
            continue
        if word in words:
            counts[words.index(word)] += 1
        else:
            words.append(word); counts.append(0)

    while len(words)>0 and len(out)<3:
        out.append(words.pop(counts.index(max(counts))).lower())
        counts.remove(max(counts))
    return out


# second solution
# from collections import Counter
# import re


# def top_3_words(text):
#     c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
#     return [w for w,_ in c.most_common(3)]