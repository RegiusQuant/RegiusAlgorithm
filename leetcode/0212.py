from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.count = 0
        self.child = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.count += 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        m, n = len(board), len(board[0])
        visit = [[False] * n for _ in range(m)]

        def dfs(x: int, y: int, s: str, node: TrieNode):
            if node.count > 0:
                result.add(s)

            m, n = len(board), len(board[0])
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if visit[nx][ny]:
                    continue
                ch = board[nx][ny]
                if ch in node.child:
                    visit[nx][ny] = True
                    dfs(nx, ny, s + ch, node.child[ch])
                    visit[nx][ny] = False


        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.child:
                    visit[i][j] = True
                    dfs(i, j, board[i][j], trie.root.child[board[i][j]])
                    visit[i][j] = False
        return list(sorted(result))
