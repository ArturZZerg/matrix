
# **MATRIX OPERATIONS LIBRARY**

This is a Python library that provides functionality to perform basic matrix operations and convert matrices to **Reduced Row Echelon Form (RREF)**. The library supports operations with fractions to maintain precision in calculations.

## **FEATURES**

- Create and manipulate matrices
- Add, subtract, multiply, and divide matrices
- Swap rows of a matrix
- Convert a matrix to **Reduced Row Echelon Form (RREF)**
- Perform operations using fractions (`fractions.Fraction`) for accurate results

## **REQUIREMENTS**

- Python 3.7 or later
- The library depends on Python's built-in `fractions.Fraction` for precise fractional arithmetic.

## **INSTALLATION**

To install this library, clone this repository:

    ```bash
git clone https://github.com/yourusername/matrix-operations.git
    ```

Once cloned, install any necessary dependencies:

    ```bash
pip install -r requirements.txt
    ```

> If you're using fractions in your code, ensure that you have Python's `fractions` module available, which comes by default with Python installations.

## **USAGE**

Here's an example of how to use the library:


    ```python
from matrix import Matrix,calc_matrix

# Create a matrix using a two-dimensional list
A = Matrix([[1, 2], [3, 4]])

# Convert to RREF
calc_matrix(A)
print(A)
    ```

## **MATRIX CLASS METHODS**

### **Initialization**
    ```python
Matrix(matrix: list[list[float]])
    ```
Initialize the matrix with a 2D list of numbers.


### **Basic Operations**
- rows in matrix starts from 1.
- `add_trans(self, r1, r2, mult=None)`: Subtracts. r1(row number) += r2(row number)*mult
- `sub_trans(self, r1, r2, mult=None)`: Subtracts. r1(row number) -= r2(row number)*mult.
- `mult_trans(self,r, mult)`: Multiplies r(row number)+=mult.
- `div_trans(matrix: Matrix)`: Divides r(row number)/=mult.
- `swap_trans(row1: int, row2: int)`: Swaps two rows of the matrix.

### **RREF Conversion**
- `calc_matrix("matrix")`: Converts the matrix to **Reduced Row Echelon Form**.

## **CONTRIBUTING**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request.

## **CONTACT**

For questions or suggestions, please contact me at **artur.vakula@gmail.com**.

