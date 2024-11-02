#prac2
def three_digit_numbers_by(digits, allowed_digits):
    assert 4 > digits > 0, "عدد ورودی باید بین ۰ تا ۴ باشد"
    for i in range(10 ** (digits - 1), 10 ** digits):
        str_num = str(i)
        if all(int(d) in allowed_digits for d in str_num):
            print(i)

#prac3
def mirror_numbers(digits):
    assert 4 > digits > 0, "عدد ورودی باید بین ۰ تا ۴ باشد"
    start = 10 ** (digits - 1)
    end = 10 ** digits
    for i in range(start, end):
        str_num = str(i)
        if str_num[0] == str_num[-1]:
            print(i)

#prac4
def reverse(digits):
    reversed_number = digits[::-1]
    print("معکوس عدد: ", reversed_number)


def main():
    number = input("عدد مورد نظر را وارد کنید: ")
    reverse(number)

    number = int(input("تعداد رقم مورد نظر را وارد کنید: "))
    mirror_numbers(number)
    print()

    number = int(input("تعداد رقم مورد نظر را وارد کنید: "))
    three_digit_numbers_by(number, [1, 2])

main()