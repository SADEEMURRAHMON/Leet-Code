class Solution:
    def isBipartite(self, graph):
        color={}
        def dfs(node,c):
            color[node]=c
            for i in graph[node]:
                if i not in color:
                    if not dfs(i,1-c):
                        return False
                elif color[i]==c:
                    return False
            return True
        for i in range(len(graph)):
            if i not in color:
                if not dfs(i,0):
                    return False
        return True

    