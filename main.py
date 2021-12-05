import numpy as np;
import os;

def getVariant():
    variant = int(input("Input variant: "));
    if (variant < 1 or variant > 7):
        raise ValueError("Varaint must be between 1 and 7 incl");
    return variant;

# TODO: implement variants 6, 7
def getMatrixByVariant(variant):
    if (variant == 6 or variant == 7):
        raise NotImplemented("implement variants 6, 7");
    matrices = dict();
    matrices[1] = np.array([
        [-3, 2.2, 0.8, 0],
        [0.4, -4.7, 6.8, 0.1],
        [0.3, -3.1, -4.4, 0.6],
        [-0.5, 0.8, 1.9, -1.3]
        ]);
    matrices[2] = np.array([
        [7, 2.19, 0.8, 0],
        [0.4, 5.29, 6.79, 0.1],
        [0.29, -3.1, 5.59, 5.9],
        [-0.49, 0.8, 1.89, 8.69]
    ]);

    matrices[3] = np.array([
        [5.012, 2.457, 2.507, 0.069],
        [0.691, 0.797, 7.463, 0.548],
        [0.223, -3.264, 1.166, 0.827],
        [-0.696, 0.421, 3.221, 7.691]
    ]);  

    matrices[4] = np.array([
        [0.7446, 0.1372, 0.0981, 0.0035],
        [0.0319, 0.5701, 0.4213, 0.0274],
        [0.0153, -0.1879, 0.5901, 0.0413],
        [-0.0376, 0.0348, 0.1533, 0.8846]
    ]);
    matrices[5] = np.array([
        [-0.9, 3.1, -0.2],
        [-0.4, -2.5, 3.2],
        [1.1, -1.5, -3.1]
    ]);  

    return matrices.get(variant);

def getCharacteristicEquationCoefficients(matrix):
    if (matrix.shape[0] != matrix.shape[1]):
        raise ValueError("Matrix is not square");
    out = [];
    out.append(1.0);
    A = matrix;
    for i in range(0, matrix.shape[1], 1):
        a = -1.0 * np.trace(A) / (i + 1);
        out.append(a);
        elementary = np.eye(matrix.shape[1]);
        B = A + elementary * a;
        A = np.dot(matrix, B);
    return out;

def getRaussMatrix(characteristicEquationCoefficients):
    n = len(characteristicEquationCoefficients) - 1;
    if (n <= 0):
        raise ValueError("Coefficients amount mut be > 0");
    out = None;
    if (n % 2 == 0):
        out = np.zeros((n, int((n + 2) / 2)));
    else:
        out = np.zeros((n + 1, int((n + 1) / 2)));

    for j in range(0, out.shape[1], 1):
        a1 = characteristicEquationCoefficients[j * 2] if 2 * j < len(characteristicEquationCoefficients) else 0.0;
        out[0][j] = a1;
        a2 = characteristicEquationCoefficients[j * 2 + 1] if 2 * j + 1 < len(characteristicEquationCoefficients) else 0.0;
        out[1][j] = a2;

    for i in range(2, out.shape[0], 1):
        factor = out[i - 2][0] / out[i - 1][0];
        for j in range(0, out.shape[1], 1):
            shouldNotBeZero = (j + 1) < out.shape[1];
            subtractFrom = out[i - 2][j + 1] if shouldNotBeZero else 0.0;
            multiplyTo = out[i - 1][j + 1] if shouldNotBeZero else 0.0;
            r = subtractFrom - factor * multiplyTo;
            out[i][j] = r;

    return out;

def isAsymptoticallyStable(raussMatrix):
    zeroColumn = raussMatrix[:, [0]];
    for e in zeroColumn:
        if (e <= 0):
            return False;
    return True;

def executeVariant(variant):
    print("{}\tVariant:{}{}".format(os.linesep, variant, os.linesep));

    matrix = getMatrixByVariant(variant);
    print("{}\tMatrix:{}".format(os.linesep, os.linesep));
    print(matrix);
    
    characteristicEquationCoefficients = getCharacteristicEquationCoefficients(matrix);
    print("{}\tCharastreristic equation coefficients:{}".format(os.linesep, os.linesep));
    print(characteristicEquationCoefficients);
    
    raussMatrix = getRaussMatrix(characteristicEquationCoefficients);
    print("{}\tRauss's matrix:{}".format(os.linesep, os.linesep));
    print(raussMatrix);

    asymptoticallyStable = isAsymptoticallyStable(raussMatrix);
    notPart = "" if asymptoticallyStable else " not";
    print("{}System is{} asymptotically stable{}".format(os.linesep, notPart, os.linesep));

def executeAll(maxVariant):
    for i in range(1, maxVariant + 1, 1):
        executeVariant(i);

def main():
    variant = getVariant();
    executeVariant(variant);
    #  Or you can execute everything (After making up your own 2 last matrices):
    # executeAll(7);

if __name__ == "__main__":
    main();
