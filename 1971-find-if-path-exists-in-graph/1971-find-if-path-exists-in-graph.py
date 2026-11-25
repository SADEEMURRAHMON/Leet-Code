class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph=[[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    if dfs(i):
                        return True
            return False
        return dfs(source)