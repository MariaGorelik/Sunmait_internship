import numpy as np


def main():
    arr1 = np.array([1, 2, 3])

    arr2 = np.array([4, 5, 6])

    result = arr1 @ arr2.T

    print(result)


if __name__ == "__main__":
    main()
