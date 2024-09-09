"""
Meta follow-up coding interview question on 2024-08-29

Input: a string
Output1: words and number of words
Output2: frequencies of non-alphanumeric character

Date: 2024-08-29
"""

import collections


def count1(string: str) -> dict:
    words = string.split(" ")
    print(words)

    wc = len(words)
    print(wc)

    dic = collections.Counter(string)
    print(dic)

    # nonalpha = "\"~!@#$%^&*()_+`-={}[]:";'<>,.?/'"

    # print("non-alphanumerical characters:")
    # for k, v in dic.items():
    #     # # check for non-alphanumerical
    #     if not k.isalnum():
    #         print(k, v)

    dic2 = {}
    # print("alphanumerical characters:")
    for k, v in dic.items():
        # check for alphanumerical
        if k.isalnum():
            # print(k, v)
            dic2[k] = v

    dic2 = dict(sorted(dic2.items()))
    return dic2


def count2(sentens: str) -> dict:
    dic2 = {}
    chars = sorted(set(sentens))
    # print(chars)

    for char in chars:
        value: int = 0
        for _, s in enumerate(sentens):
            if char == s and char.isalnum():
                value += 1
                dic2[char] = value
    return dic2


if __name__ == "__main__":
    sentence: str = '"Updates are coming to your card account", he said.'
    print("count1:")
    print(count1(sentence))
    print("\n")
    print("count2:")
    print(count2(sentence))
