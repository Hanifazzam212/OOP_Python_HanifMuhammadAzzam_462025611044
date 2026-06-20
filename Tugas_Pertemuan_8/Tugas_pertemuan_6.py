# Class utama
class A:
    def __init__(self):
        print("Constructor A")

    def info(self):
        print("Method dari Class A")


# Class B mewarisi A
class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor B")

    def info(self):
        super().info()
        print("Method dari Class B")


# Class C juga mewarisi A
class C(A):
    def __init__(self):
        super().__init__()
        print("Constructor C")

    def info(self):
        super().info()
        print("Method dari Class C")


# Class D mewarisi B dan C
# Inilah yang disebut Diamond Problem
class D(B, C):
    def __init__(self):
        super().__init__()
        print("Constructor D")

    def info(self):
        super().info()
        print("Method dari Class D")


obj = D()

print("\n=== Output Method Info ===")
obj.info()

print("\n=== Method Resolution Order (MRO) ===")
print(D.__mro__)