import string
from collections import deque
from typing import List, Dict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        depthBegin, depthEnd = {beginWord: 1}, {endWord: 1}
        queueBegin, queueEnd = deque([beginWord]), deque([endWord])

        def expand(queue: deque, depth: Dict, depthOther: Dict):
            s = queue.popleft()
            for i in range(len(s)):
                for ch in string.ascii_lowercase:
                    if ch == s[i]:
                        continue
                    t = s[:i] + ch + s[i + 1:]
                    if t not in wordSet or t in depth:
                        continue
                    if t in depthOther:
                        return depth[s] + depthOther[t]
                    depth[t] = depth[s] + 1
                    queue.append(t)
            return -1

        while queueBegin or queueEnd:
            times = len(queueBegin)
            for _ in range(times):
                result = expand(queueBegin, depthBegin, depthEnd)
                if result != -1:
                    return result

            times = len(queueEnd)
            for _ in range(times):
                result = expand(queueEnd, depthEnd, depthBegin)
                if result != -1:
                    return result

        return 0
