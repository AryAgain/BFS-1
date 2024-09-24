# Submitted by : Aryan Singh_RN12MAY2023
# Time Complexity : O(n)
# Space Complexity : Average : O(n) in BFS and O(h) in DFS
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

#1. using BFS :

class Solution:
    '''
    - Do bfs traversal and store a new list
    - during each level iteration, based on the queue size.
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        result = []
        queue.append(root)
        while queue:
            #logic
            tmplist = []
            size = len(queue)
            for i in range(size):
                temp_node = queue.popleft()
                tmplist.append(temp_node.val)
                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
            result.append(tmplist)
        return result
    
#2. using DFS:

class Solution:
    '''
    - Do a dfs traversal and add a list for first time at each recursive step
    - after which add the numbers, in the corresponding list based on recursive step count.
    '''
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def dfs(node, level):
            if not node:
                return None
            #logic
            if len(levels) <= level:
                tmplist = []
                tmplist.append(node.val)
                levels.append(tmplist)
            else:
                levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return levels   