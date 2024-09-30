from fractions import Fraction

#custom exeption class
class MatrixException(Exception):
    pass

class Matrix:
    matrix_template = []

    def __init__(self, args):
        
        try:
            size= len(args[0])
        except:
            raise MatrixException("Constructor: args not a matrix")
            
        if type(args) == list:
            for row in args:
                if type(row) == list:
                    if size == len(row):
                         for element in row:
                             if (type(element) != int) and (type(element) != Fraction) and (type(element) != float):
                                 raise MatrixException("Constructor: args not a matrix, not a matrix of numbers")
                    else:
                        raise MatrixException("Constructor: args not a matrix, rows have different length")
                else:
                    raise MatrixException("Constructor: args not a matrix, not 2d array")
            self.matrix_template = args
        else:
            raise MatrixException("Constructor: args not a matrix, not array")
        

    def __str__(self) -> str:
        matrix_output = ""
        for i in self.matrix_template:
            for c in i:
                if len(str(c)) < 3:
                    space = " "*(3-int(len(str(c))))
                    matrix_output += f" [{space}{c}] "
                else:
                    matrix_output += f" [{c}] "
            matrix_output += "\n"

        return matrix_output

    #Adds. r1(row number) += r2(row number)*mult
    def add_trans(self, r1, r2, mult=None):
        if r1 not in range((len(self.matrix_template))) or r2 not in range(
            (len(self.matrix_template))
        ):
            pass
        if mult:

            self.matrix_template[r1 - 1] = [
                (
                    self.matrix_template[r2 - 1][i] * mult
                    + self.matrix_template[r1 - 1][i]
                )
                for i in range(len(self.matrix_template[r2 - 1]))
            ]
        else:
            self.matrix_template[r1 - 1] = [
                (self.matrix_template[r2 - 1][i] + self.matrix_template[r1 - 1][i])
                for i in range(len(self.matrix_template[r2 - 1]))
            ]

    #Subtracts. r1(row number) -= r2(row number)*mult.
    def sub_trans(self, r1, r2, mult=None):
        if r1 not in range((len(self.matrix_template))) or r2 not in range(
            (len(self.matrix_template))
        ):
            pass
        if mult:
            self.matrix_template[r1 - 1] = [
                (
                    self.matrix_template[r1 - 1][i]
                    - self.matrix_template[r2 - 1][i] * mult
                )
                for i in range(len(self.matrix_template[r2 - 1]))
            ]
        else:
            self.matrix_template[r1 - 1] = [
                (self.matrix_template[r1 - 1][i] - self.matrix_template[r2 - 1][i])
                for i in range(len(self.matrix_template[r2 - 1]))
            ]

    #Multiplies r(row number)+=mult.
    def mult_trans(self, r, mult):
        if r not in range((len(self.matrix_template))):
            pass
        if mult != 0:
            self.matrix_template[r - 1] = [
                self.matrix_template[r - 1][i] * mult
                for i in range(len(self.matrix_template[r - 1]))
            ]

    #Divides r(row number)/=mult.
    def div_trans(self, r, mult):
        if r not in range((len(self.matrix_template))):
            pass
        if mult != 0:
            self.matrix_template[r - 1] = [
                Fraction(Fraction(self.matrix_template[r - 1][i]), Fraction(mult))
                for i in range(len(self.matrix_template[r - 1]))
            ]

    #Swaps two rows of the matrix.
    def swap_trans(self, r1, r2):
        if r1 not in range((len(self.matrix_template))) or r2 not in range(
            (len(self.matrix_template))
        ):
            pass
        self.matrix_template[r1 - 1], self.matrix_template[r2 - 1] = (
            self.matrix_template[r2 - 1],
            self.matrix_template[r1 - 1],
        )

#Converts the matrix to Reduced Row Echelon Form.
def solve_system_of_equations(mat_rix):
    def find_0(our_matrix, row_index, col, target,count1,rowd):
        if count1:
            if (our_matrix.matrix_template[row_index][col]
                + ((our_matrix.matrix_template[rowd[-1]][col]) * our_matrix.matrix_template[row_index][col]*(-1))) == target:
                our_matrix.add_trans(row_index + 1, rowd[-1]+1, our_matrix.matrix_template[row_index][col]*-1)
                return True
        else:
            if row_index == 0:
                our_matrix.div_trans(row_index + 1+len(row_d), mat_rix.matrix_template[row_index+len(row_d)][col])
                print(mat_rix.matrix_template[row_index+len(row_d)])
            if (our_matrix.matrix_template[row_index][col]
                + ((our_matrix.matrix_template[len(row_d)][col])* our_matrix.matrix_template[row_index][col]*(-1))) == target:
                mult = mat_rix.matrix_template[row_index][col]*(-1)
                our_matrix.add_trans(row_index + 1, 1+len(row_d),mult)
                return True
        return False
    ranks = mat_rix.matrix_template[:]
    rows = len(mat_rix.matrix_template[0]) - 1
    row_d = []
    for n in range(rows):
        r_index = 0
        count_1 = 0
        for _ in ranks:
            if r_index == len(row_d) and count_1 == 0:
                temp_list_zero = []
                count_index = 0
                for item_zero in mat_rix.matrix_template[r_index]:
                    if item_zero == 0 and ((count_index in row_d) or (count_index == n)):
                        temp_list_zero.append(item_zero)
                    count_index += 1
                if mat_rix.matrix_template[r_index][n] != 1 and (
                    len(temp_list_zero) != len(row_d) + 1 or len(row_d) == 0):
                    if mat_rix.matrix_template[r_index][n] == 0:
                        find_0(mat_rix, r_index, n, 1,count_1,row_d)
                    else:
                        mat_rix.div_trans(
                            r_index + 1, mat_rix.matrix_template[r_index][n])
                if mat_rix.matrix_template[r_index][n] == 1:
                    row_d.append(n)
                    count_1 += 1
            elif mat_rix.matrix_template[r_index][n] != 0:
                temp_list_zero = []
                count_index = 0
                if len(row_d) == len(mat_rix.matrix_template):
                    break
                for item_zero in mat_rix.matrix_template[len(row_d)]:
                    if item_zero == 0 and (
                        (count_index in row_d) or (count_index == n)):
                        temp_list_zero.append(item_zero)
                    count_index += 1
                if len(temp_list_zero) == len(row_d) + 1:
                    continue
                find_0(mat_rix, r_index, n, 0,count_1,row_d)
            r_index += 1
            
#Counts determinant header
def determinant(mat_rix):
    if len(mat_rix.matrix_template) != (len(mat_rix.matrix_template[0])-1):
        raise MatrixException("Not square matrix do not have determinant")
    
    if len(mat_rix.matrix_template) == 1:
        return mat_rix.matrix_template[0][0]
    
    mat_rix_square = []
    for row in range(len(mat_rix.matrix_template)):
        mat_rix_square.append([])
        for column in range(len(mat_rix.matrix_template)):
            mat_rix_square[row].append(mat_rix.matrix_template[row][column])

    return determinant_doer(mat_rix_square)

#Counts determinant doer
def determinant_doer(mat_rix):
    det = 0
    
    if len(mat_rix) == 2:
        det = mat_rix[0][0] * mat_rix[1][1] - mat_rix[0][1] * mat_rix[1][0]
    else:
        for col in range(len(mat_rix)):
            minor_mat_rix=[]
            for row in range(1,len(mat_rix)):
                minor_mat_rix.append([])
                for column in range(len(mat_rix)):
                    if column != col:
                        minor_mat_rix[row-1].append(mat_rix[row][column])
            
            det = det + pow(-1,col) * mat_rix[0][col] * determinant_doer(minor_mat_rix)
    return det
