class Matrix:
    def __init__(self) -> None:
        self.matrix = [[1,3]]
        self.target = 3 

    def searchMatrix(self) -> bool:
        found = False
        rowN = 0

        rows, cols = len(self.matrix) - 1, len(self.matrix[0]) - 1
        
        left, right = 0, rows

        while left <= right:
            mid = (left + right) // 2 
            
            if self.matrix[mid][0] <= self.target <= self.matrix[mid][cols]:
                rowN = mid
                break
            elif self.target > self.matrix[mid][cols]:
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, len(self.matrix[rowN]) 
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if self.matrix[rowN][mid] == self.target:
                found = True
                break
            elif self.matrix[rowN][mid] > self.target:
                right = mid - 1
            else:
                left = mid + 1
        return found
m = Matrix()
print(m.searchMatrix())
