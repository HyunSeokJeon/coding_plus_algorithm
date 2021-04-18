# 5주차 과제 1번
# 이진 탐색법은 정렬된 자료를 탐색하는 데에 사용할 수 있다. 
# 인덱스가 낮을 수록 더 작은 값으로 정렬된 2차원 리스트에서 
# target을 찾으면 True를 반환하고, target을 찾을 수 없으면 False를 반환하는 프로그램을 작성하시오.

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(matrix[0][:3])
def searchMatrix(matrix, target):
    if len(matrix) == 1:
        if len(matrix[0]) == 1:
            if target == matrix[0][0]:
                return True
            else:
                return False
        inIndex = len(matrix[0]) //2
        if target == matrix[0][inIndex]:
            return True
        elif target < matrix[0][inIndex]:
            return searchMatrix([matrix[0][:inIndex]], target)
        else:
            return searchMatrix([matrix[0][inIndex:]], target)
    else:
        out = len(matrix) // 2
        
        if target < matrix[out][0]:
            return searchMatrix(matrix[:out], target)
        else:
            return searchMatrix(matrix[out:], target)
target = 13
print(searchMatrix(matrix, target))
