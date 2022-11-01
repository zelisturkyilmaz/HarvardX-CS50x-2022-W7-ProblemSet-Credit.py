from cs50 import get_int, get_string

while True:
    number = get_int("Number: ")
    if type(number) == int:
        break

number_list = list(map(int, str(number)))

number_list.reverse()

digits = []

for i in range(1, len(number_list), 2):
    digits.append(number_list[i]*2)

newdigits = int("".join(map(str, digits)))

sumdigits = list(map(int, str(newdigits)))

sumof = sum(sumdigits)

sumof_eo = 0

for i in range(0, len(number_list), 2):
    sumof_eo += number_list[i]

total = sumof + sumof_eo

if total % 10 == 0:
    if len(number_list) == 15 and number_list[len(number_list)-1] == 3 and (number_list[len(number_list)-2] == 4 or number_list[len(number_list)-2] == 7):
        print("AMEX")
    elif len(number_list) == 16 and number_list[len(number_list)-1] == 5 and (number_list[len(number_list)-2] == 1 or number_list[len(number_list)-2] == 2 or number_list[len(number_list)-2] == 3 or number_list[len(number_list)-2] == 4 or number_list[len(number_list)-2] == 5):
        print("MASTERCARD")
    elif (len(number_list) == 16 or len(number_list) == 13) and number_list[len(number_list)-1] == 4:
        print("VISA")
else:
    print("INVALID")