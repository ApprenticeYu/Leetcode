class Solution:
    def word_search(self,matrix,word):
        position = [(0,1),(0,-1),(1,0),(-1,0)]
        def check(i,j,k):
            if matrix[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            find = False
            visited.add((i,j))
            for temp_i,temp_j in position:
                new_i,new_j = temp_i + i,temp_j + j
                if new_i >= 0 and new_i < len(matrix) and new_j >= 0 and new_j < len(matrix[0]):
                    if (new_i,new_j) not in visited:
                        if check(new_i,new_j,k + 1):
                            find = True
                            break
            visited.remove((i,j))
            return find
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if check(i,j,0):
                    return True
        return False
result = Solution()
matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(result.word_search(matrix,word))
