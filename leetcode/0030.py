from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []

        wordsCounter = Counter(words)
        numOfWords = len(words)
        wordLength = len(words[0])
        totalTokens = numOfWords * wordLength

        for k in range(wordLength):
            splitWordsCounter = Counter()

            numOfSplitWords = 0
            for i in range(k, len(s), wordLength):
                if numOfSplitWords >= numOfWords:
                    word = s[i - totalTokens: i - totalTokens + wordLength]
                    splitWordsCounter[word] -= 1

                word = s[i: i + wordLength]
                splitWordsCounter[word] += 1
                numOfSplitWords += 1
                if splitWordsCounter == wordsCounter:
                    result.append(i - totalTokens + wordLength)

        return result
