def calculate_circle(r):
    area = r**2 * 3.14
    circum = 2 * r * 3.14
    return area, circum

r=float(input("반지름을 입력하세요 : "))

print(f"반지름 {r}인 원의 면적은 {calculate_circle(r)[0]}, 원의 둘레는 {round(calculate_circle(r)[1],2)}")
