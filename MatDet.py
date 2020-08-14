
class MatDet:

    def __init__(self, ):
        self.minors = 0

    def det(self, m):
        print(f"m = {m}")
        print(f"len m =  {(len(m))}, len m[0] =  {len(m[0])}")
        if len(m) != len(m[0]):
            return "Invalid Operation: This operation works on square matrix only"
        elif len (m) == 1:
            return m[0][0]
        else:
            indices = [[(i, j) for j in range(len(m))]for i in range(len(m))]
            self.minors = [[0 for j in range(len(m))]for i in range(len(m))]
            sign_mat = [[0 for j in range(len(m))]for i in range(len(m))]
            # print(f"Indices = {indices}\nself.minors = {self.minors}\nsign_mat = {sign_mat}\n {('*') * 20} ")
            for coordinates in indices:
                for x, y in coordinates:
                    element_sign = (-1) ** (x + y)
                    n = list([m[i][j] for j in range(len(m))if i != x and j != y]for i in range((len(m))))
                    n.pop(x)
                    self.minors[x][y] = n
                    sign_mat[x][y] = element_sign
            self.co_factors =  [[sign_mat[i][j] * self.det(self.minors[i][j]) for j in range(len(self.minors))]for i in range(len(self.minors))]
            result = [[m[i][j] * self.co_factors[i][j]for i in range(len(m))]for j in range(len(m))]
            return sum(result[0])


def det(m):
    print(f"m = {[i for i in m]}")
    print(f"len m =  {(len(m))}, len m[0] =  {len(m[0])}")
    if len(m) != len(m[0]):
        return "Invalid Operation: This operation works on square matrix only"
    elif len (m) == 1:
        return m[0][0]
    else:
        indices = [[(i, j) for j in range(len(m))]for i in range(len(m))]
        minors = [[0  for j in range(len(m))]for i in range(len(m))]
        sign_mat = [[0  for j in range(len(m))]for i in range(len(m))]
        # print(f"Indices = {indices}\nminors = {minors}\nsign_mat = {sign_mat}\n {('*') * 20} ")
        for coordinates in indices:
            for x, y in coordinates:
                element_sign = (-1) ** (x + y)
                n = list([m[i][j] for j in range(len(m))if i != x and j != y]for i in range((len(m))))
                n.pop(x)
                minors[x][y]= n
                # print(minors)
                sign_mat[x][y] = element_sign
                # print(sign_mat)
        co_factors =  [[sign_mat[i][j] * det(minors[i][j]) for j in range(len(indices))]for i in range(len(indices))]
        result = [[m[i][j] * co_factors[i][j]for i in range(len(m))]for j in range(len(m))]
        return sum(result[0])

mat = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(det(mat))
print("*" * 50)
z = MatDet()
z.det(mat)
