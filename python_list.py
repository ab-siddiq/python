# index    0  1  2  3  4  5  6  7  8  9  10  11  12 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# index  -12 -11 -10 -9 -8 -7 -6  -5  -4 -3  -2  -1
# pyyhon has negative indexing and starts from the end which is different from the typical programming
#python positive indexing
print(numbers[1])
# python negative indexing
print(numbers[-5])
# python range printing using positive indexing. it will print values index 1 to the index before 7.
print(numbers[1:7])
# python range printing with increment by. it will print index 1 to before 7 and increment by 1
print(numbers[1:7:1])
# python range printing with increment by. it will print index 1 to before 7 and increment by 2
print(numbers[1:7:2])
# print value index 1 to end
print(numbers[1:])
# print value index 0 to before 9
print(numbers[:9])
# print values reversly. index 9 to before index 2
print(numbers[9:2])
# print values reversly. index 9 to before index 2 and decrement by 1
print(numbers[9:2:-1])
# print values reversly. index 9 to before index 2 and decrement by 2
print(numbers[9:2:-2])
# print index 0 to end
print(numbers[:])
# start end and increment by -1 which will reverse the array very simply
print(numbers[::-1])