
"""
This module provides a Matrix class for matrix operations with Fraction support.

The module contains a single class, Matrix, which can be instantiated with a two-dimensional list of integers. The Matrix class provides methods for adding, subtracting, multiplying, and dividing matrices, as well as methods for various row operations.

The Matrix class also provides a __str__ method which returns a string representation of the matrix, with each element aligned to the left and separated by a space.

The Matrix class also provides a rref_calc method which calculates the RREF of a matrix.
"""
from fractions import Fraction

class Matrix:
    """
    Class for matrix operations with Fraction support
    
    @param args: a two-dimensional list of integers
    """
    matrix_template = []

    def __init__(self, args):
        """
        Initialization method for Matrix class
        
        @param args: a two-dimensional list of integers
        """
        self.matrix_output = ""
        self.matrix_template = args

    def __str__(self) -> str:
        """
        Returns a string representation of the matrix, with each element aligned to the left and separated by a space.
        Elements are displayed in a field of width 3, with negative numbers displayed in a field of width 4.
        """
        matrix_output =""
        for i in self.matrix_template:
            for c in i:
                if len(str(c)) < 3:
                    space = " "*(3-int(len(str(c))))
                    matrix_output += f" [{space}{c}] "
                else:
                    matrix_output += f" [{c}] "
            matrix_output += "\n"

        return matrix_output

    def add_trans(self, r1, r2, mult=None):
        
        """
        Adds row r2 to row r1, scaled by mult if provided
        
        @param r1: row number to add to
        @param r2: row number to add
        @param mult: optional scaling factor
        """
        if r1 not in range((len(self.matrix_template))) or r2 not in range((len(self.matrix_template))):
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

    def sub_trans(self, r1, r2, mult=None):
        """
        Subtracts row r2 from row r1, scaled by mult if provided

        @param r1: row number to subtract from
        @param r2: row number to subtract
        @param mult: optional scaling factor
        """
        if r1 not in range((len(self.matrix_template))) or r2 not in range((len(self.matrix_template))):
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

    def mult_trans(self, r, mult):
        """
        Scales row r by mult

        @param r: row number to scale
        @param mult: scaling factor
        """
        if r not in range((len(self.matrix_template))):
            pass
        if mult != 0:
            self.matrix_template[r - 1] = [
                self.matrix_template[r - 1][i] * mult
                for i in range(len(self.matrix_template[r - 1]))
            ]

    def div_trans(self, r, mult):
        """
        Divides row r by mult

        @param r: row number to divide
        @param mult: divisor
        """
        if r not in range((len(self.matrix_template))):
            pass
        if mult != 0:
            self.matrix_template[r - 1] = [Fraction(Fraction(self.matrix_template[r - 1][i]), Fraction(mult)) for i in range(len(self.matrix_template[r - 1]))] 

    def swap_trans(self, r1, r2):
        """
        Swaps row r1 with row r2

        @param r1: row number to swap
        @param r2: row number to swap
        """
        if r1 not in range((len(self.matrix_template))) or r2 not in range(
            (len(self.matrix_template))):
            pass
        self.matrix_template[r1 - 1], self.matrix_template[r2 - 1] = (
            self.matrix_template[r2 - 1],
            self.matrix_template[r1 - 1],
        )

    def rref_calc(self):
        """
        Finds the RREF of a matrix.
        
        @param self: a two-dimensional list of integers
        @return: the RREF of the matrix
        """
        def find_0(self, row_index, col, target,count1,rowd):
            """
            A helper function for calc_matrix. Finds the first element in a given row that is equal to a target value.
            If the element is found, it subtracts the element in the row above it (scaled by the element's value) from the element.
            If the element is not found, it divides the element by the element in the row below it.
            
            @param self: the matrix to operate on
            @param row_index: the row to search in
            @param col: the column to search in
            @param target: the target value to search for
            @param count1: a boolean indicating whether to add or subtract the element
            @param row_d: a list of row indices to search in
            @return: a boolean indicating whether the target value was found
            """
            if count1:
                if (self.matrix_template[row_index][col]
                    + ((self.matrix_template[rowd[-1]][col]) * self.matrix_template[row_index][col]*(-1))) == target:
                    self.add_trans(row_index + 1, rowd[-1]+1, self.matrix_template[row_index][col]*-1)
                    return True
            else:
                if row_index == 0:
                    self.div_trans(row_index + 1+len(row_d), self.matrix_template[row_index+len(row_d)][col])
                if (self.matrix_template[row_index][col]
                    + ((self.matrix_template[len(row_d)][col])* self.matrix_template[row_index][col]*(-1))) == target:
                    mult = self.matrix_template[row_index][col]*(-1)
                    self.add_trans(row_index + 1, 1+len(row_d),mult)
                    return True
            return False
        ranks = self.matrix_template[:]
        rows = len(self.matrix_template[0]) - 1
        row_d = []
        for n in range(rows):  # n is the column index
            r_index = 0
            count_1 = 0  # counts the number of rows with leading value "1" in this row
            for _ in ranks: # iterates through the rows
                if r_index == len(row_d) and count_1 == 0: # checks if this value needs to be changed to "1" 
                    temp_list_zero = []
                    count_index = 0
                    for item_zero in self.matrix_template[r_index]: #calculates the number of zeros in the row, and checks if the number of zeros is equal to the number of columns with leading value "1"
                        if item_zero == 0 and ((count_index in row_d) or (count_index == n)):
                            temp_list_zero.append(item_zero)
                        count_index += 1
                    if self.matrix_template[r_index][n] != 1 and (
                        len(temp_list_zero) != len(row_d) + 1 or len(row_d) == 0): # checks if the leading value is not "1"
                        if self.matrix_template[r_index][n] == 0: # if leading value is "0" it searches for a row with a leading value "1"
                            find_0(self, r_index, n, 1,count_1,row_d)
                        else: # if leading value is not "0" it is divided by itself to make it "1"
                            self.div_trans(
                                r_index + 1, self.matrix_template[r_index][n])
                    if self.matrix_template[r_index][n] == 1: # checks if the leading value is "1" and adds it to the list of row indices
                        row_d.append(n)
                        count_1 += 1
                elif self.matrix_template[r_index][n] != 0: # checks if the value is not "0"
                    temp_list_zero = []
                    count_index = 0
                    if len(row_d) == len(self.matrix_template): # checks if the number of rows with leading value "1" is equal to the number of rows in the matrix. If so, the matrix is in RREF
                        break
                    for item_zero in self.matrix_template[len(row_d)]: # calculates the number of zeros in the row
                        if item_zero == 0 and (
                            (count_index in row_d) or (count_index == n)):
                            temp_list_zero.append(item_zero)
                        count_index += 1
                    if len(temp_list_zero) == len(row_d) + 1: # checks if the number of zeros is equal to the number of columns with leading value "1"(+1), if so, we dont have to touch this row
                        continue
                    find_0(self, r_index, n, 0,count_1,row_d)
                r_index += 1

