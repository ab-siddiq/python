class A:
    print("I am from class A")
class B(A):
    print("I am from class B")
class C(B):
    print("I am from class C")
class D(C):
    print("I am from class D")
class E(D):
    print("I am from class E")
e=E()