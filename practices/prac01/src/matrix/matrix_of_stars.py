#prac1
def matrix_of_stars(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("*", end=" ")
        print()

def main():
    rows = int(input("تعداد سطرها را وارد کنید: "))
    cols = int(input("تعداد ستون‌ها را وارد کنید: "))
    matrix_of_stars(rows, cols)

main()