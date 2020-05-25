'''
Solution:
Time Complexity: O(m *n *n1) Would be the worst case if you have 1 element in every row or column but the average is still better here
Space Complexity: O(m*n1)
Did this code successfully run on Leetcode : Yes
Explanation:
A sparse matrix can be represented as a sequence of rows, each of which is a sequence of (column-number, value) pairs of the nonzero values in the row.
Save the indexes for each row from A which have non zero value into a list.
Use these saved indexes and values to multiply with matrix B to get the answer. Here columns with all 0's would be avoided.

Brute Force:
Time Complexity: O(m *n *n1) -> m and n are rows and columns of matrix 1 and n1 is the column of matrix2
Space Complexity: O(m*n1)
Did this code successfully run on Leetcode : Yes
Explanation: Multiply 2 matrixes through normal Matrix multiplication

'''
class Solution:

    # A sparse matrix can be represented as a sequence of rows, each of which is a sequence of (column-number, value) pairs of the nonzero values in the row.
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])
        nB = len(B[0])

        C = [[0 for i in range(0, nB)] for j in range(0, m)]

        # create an indexList of index, value for every non 0 value in A we will use this corresponding index in B
        # This will hence not iterating through a column in B which is 0
        indexList = [0 for i in range(m)]
        for i in range(0, m):
            tempList = []
            for j in range(0, n):
                if A[i][j] != 0:
                    tempList.append(j)
                    tempList.append(A[i][j])
            # Save the first row to be multipled as index, value inside indexList
            indexList[i] = tempList

        for i in range(0, m):
            elementA = indexList[i]
            # For first Row index, value which are non zero are saved
            # For Second Row index, value which are non zeroa are saved
            for k in range(0, len(elementA), 2):
                # Get column to multiply
                # Get value of A to multiply
                col = elementA[k]
                valA = elementA[k + 1]
                # Here c is created column wise
                # Here C is multiplied by valA which is non zero saved and the B array columns which the row values taken from A, we are hence skipping any column in B which is 0
                '''
                Example:
                Value to be multiplied
                1 7
                1 0
                1 0
                -1 7
                -1 0
                -1 0
                3 0
                3 0
                3 1
                '''
                for j in range(0, nB):
                    valB = B[col][j]
                    C[i][j] += valA * valB

                # [[7, 0, 0], [0, 0, 0]] -> 1st
                # [[7, 0, 0], [-7, 0, 0]] -> 2nd
                # [[7, 0, 0], [-7, 0, 3]] -> 3rd

        return C

    def multiplyBruteForce(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(A[0])
        nB = len(B[0])

        # m*n and n*k == m*k
        # i =0. k =0 j will take first element of A[0][0] * B[0][0] + [0][0] * [0][1]+[0][2] -> end of k then next j will be the next row[0][1] * row[0][0] + row[0][1]* row[0][1] + row[0][2] * row[0][2]
        C = [[0 for i in range(0, nB)] for j in range(0, m)]
        for i in range(m):
            for k in range(n):
                if A[i][k] != 0:
                    for j in range(nB):
                        C[i][j] += A[i][k] * B[k][j]

        return C