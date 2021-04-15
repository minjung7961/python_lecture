st = 'Programming'
# 자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch not in ['a','e','i','o','u']:
        continue
    print(ch)
print('The end')