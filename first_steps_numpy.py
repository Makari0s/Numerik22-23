"""
Numerik 22/23 (Jeffrey Bukieda 2430873, Tommy Riediger 2412359)
"""
import numpy as np

if __name__ == "__main__":
    b = np.array([1, 2, 3])
    A = np.array([[1, 2, 3],
                  [2, 3, 4],
                  [4, 5, 6]])
    b1 = np.array([1, 1, -1, -1])
    A1 = np.eye(3, dtype=int) * 5 + np.eye(3, k=1, dtype=int) * 4 + np.eye(3, k=-1, dtype=int) * 3
    b2 = np.zeros(3, dtype=int)
    A2 = np.ones((4, 2), dtype=int)
    print(b, "= b")
    print(A, "= A")
    print(b1, "= b1")
    print(A1, "= A1")
    print(b2, "= b2")
    print(A2, "= A2")
    print(b1[0])
    print(b2[2])
    print(A1[0, :])
    print(A2[:, 1])
