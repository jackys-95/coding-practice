class Solution(object):
    def findCircleNum(self, M):
        count = 0
        visited = [False for i in range(0, len(M))]
        for i in range(0, len(M)):
            if visited[i] == False:
                   self.dfs(M, visited, i)
                   count += 1
        return count
            

    def dfs(self, M, visited, m_index):
        for j in range(0, len(M[m_index])):
            if M[m_index][j] == 1 and visited[j] == False:
                visited[j] = True
                self.dfs(M, visited, j)
    
    def wrong_findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or len(M) == 0:
            return 0
            
        friend_dict, circles_dict = {}, {}
        for i in range(0, len(M)):
            friend = M[i]
            friend_set = self.generate_friend_set(friend)
            friend_dict[i] = friend_set
            # convert friend array into array of indices
            direct_friend = None
            for j in range(0, len(friend)):
                if (friend[j]) == 1 and j != i:
                    if j in friend_dict:
                        direct_friend = friend_dict[j]
                    else:
                        friend_dict[j] = self.generate_friend_set(M[j])
                        direct_friend = friend_dict[j]
                    if direct_friend is not None:
                        union = direct_friend | friend_set
                        friend_set = friend_dict[i] = friend_dict[j] = union
            if direct_friend:
                for item in direct_friend:
                    friend_dict[item] = union
                        
        print(friend_dict.values())
        for i in friend_dict:
            print(i, friend_dict[i])
        for value in friend_dict.values():
            value = frozenset(value)
            if value not in circles_dict:
                circles_dict[value] = 1

        return len(circles_dict.values())


    def generate_friend_set(self, friend):
        return {i for i in range(0, len(friend)) if friend[i] == 1}

sol = Solution()
