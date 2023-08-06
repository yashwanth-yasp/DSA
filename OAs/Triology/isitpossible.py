class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve( self,A, B):
        if not B or A < 0:
            return [-1]
        result = [0]*(A+1)
        result[0] = -1
        M = len(B)
        for i in B:
            #checking for impossible args
            if i[0] + i[2] > i[1]:
                return [-1]
            result[i[1]] = M + 1
            
        dic = {}
        
        for i in range(len(B)):
            B[i].append(i+1)
            dic[B[i][1]] = B[i]
        
        dic = sorted(dic.items(), key = lambda x: x[0])
        
        for i in dic:
            j = i[1][0]
            count = i[1][2]
            while j != i[1][1] and count != 0:
                if result[j] == 0:
                    count -= 1
                    result[j] = i[1][3]
                j += 1
            if count != 0:
                return [-1]
        
        return result