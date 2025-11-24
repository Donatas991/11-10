# 1uzd
# def sum_to_n(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total

# 2uzd
# def count_char(banana, a):
#     count = 0
#     for i in banana:
#         if i == a:
#             count += 1
#     return count
# 3uzd
# def swap(arr, i, j):
#     arr[i], arr[j] == arr[j], arr[i]
#     return arr

#    4 uzd parasykfunkcija kuri iterpia i elementa i pasirinkta vieta.
# funkcija insert_at(arr,index,value):
# nenaudok insert()
masyvas = [1, 4, 7, 6, 3]
value = 8
index = 3

def insert_at(arr, index, value):
    b_arr = []
    
    for i in range(len(arr)):
        if i == index:
            b_arr.append(value)
            b_arr.append(arr(i))
    if index <= arr(i):
    return
