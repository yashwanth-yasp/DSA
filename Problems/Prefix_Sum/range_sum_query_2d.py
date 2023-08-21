
#medium

class NumMatrix:
    '''
    making the prefix sum 2d matrix for the whole matrix
    '''

    def __init__(self, matrix):
        self.matrix = matrix 
        temp = 0
        self.prefix_sum = [[] for _ in matrix]
        print(self.prefix_sum)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp += matrix[i][j]
                self.prefix_sum[i].append(temp)
            temp = 0
    
    def sumRegion(self, row1, col1, row2, col2):
        regionSum = 0
        for i in range(row1, row2+1):
            regionSum += self.prefix_sum[i][col2] - self.prefix_sum[i][col1 - 1]
        return regionSum

        
    def print_obj(self):
        print(self.prefix_sum)

def main():
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    solu = NumMatrix(matrix)
    solu.print_obj()
    print(solu.sumRegion(1,2,2,4))

main()