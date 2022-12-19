# def pythagorean_triple(integers):
#     if (integers[0] ** 2 + integers[1] ** 2 == integers[2] ** 2) or (
#             integers[0] ** 2 + integers[2] ** 2 == integers[1] ** 2) or (
#             integers[1] ** 2 + integers[2] ** 2 == integers[0] ** 2):
#         return True
#     else:
#         return False
# print(pythagorean_triple([5, 3, 4]))
# def pythagorean_triple(integers):
#     a, b, c = sorted(integers)
#     return a**2 + b**2 == c**2
# print(pythagorean_triple([12, 3, 4]))
# def to_jaden_case(string):
#     list_1 = string.split()
#     list_2 = []
#     for word in list_1:
#         list_2.append(word.capitalize())
#     return " ".join(list_2)
#
#
# print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
# def digital_root(n):
#     str_dig = str(n)
#     rez = 0
#     if len(str_dig) == 1:
#         return int(str_dig)
#     else:
#         while len(str_dig) > 1:
#             rez = 0
#             for i in str_dig:
#                 rez += int(i)
#                 str_dig = str(rez)
#         return rez
# print(digital_root(78))
# def sale_hotdogs(n):
#     if n < 5:
#         return n * 100
#     elif 5 <= n < 10:
#         return n * 95
#     else:
#         return n * 90
# print(sale_hotdogs(0))
# def minimum(arr_1):
#     return min(arr_1)
#
# print(minimum([-52, 56, 30, 29, -54, 0, -110]))
# def validate_pin(pin):
#     if pin.isdigit() and (len(pin)==4 or len(pin)==6):
#         return True
#     else:
#         return False
# print(validate_pin('12345'))
def solution(start, finish):
    ch = 0
    while start < finish:
        if start + 3 <= finish:
            start += 3
        else:
            start += 1
        ch +=1
    return ch
print(solution(1, 128))
