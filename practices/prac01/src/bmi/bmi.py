#prac5
def calc_bmi(weight, height):
    bmi = weight / (height ** 2)
    print("شاخص توده بدنی شما: ", round(bmi, 2))

def main():
    weight = float(input("وزن (کیلوگرم) را وارد کنید: "))
    height = float(input("قد (متر) را وارد کنید: "))
    calc_bmi(weight, height)

main()