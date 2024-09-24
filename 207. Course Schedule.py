class Solution:
    '''
    - [a,b] b -> a req[1] -> req[0]
    - make adjaceny matrix of the dependent courses in a graph
    - if the graph has circular loop, courses can't be completed
    - use BFS and if total visited nodes more than numCourses provided, there is a cycle
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for i in range(numCourses)]
        adj = {}
        for req in prerequisites:
            indegree[req[0]] += 1
            if req[1] in adj:
                adj[req[1]].append(req[0])
            else:
                adj[req[1]] = [req[0]]
        # bfs
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        visitedCount = 0
        while queue:
            current = queue.popleft()
            visitedCount += 1
            if current in adj:
                for val in adj[current]:
                    indegree[val] -= 1
                    if indegree[val] == 0:
                        queue.append(val)
        return visitedCount == numCourses