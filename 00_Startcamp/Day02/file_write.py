lunches = {
    '양자강' : '02-557-4565',
    '김밥카페' : '02-586-4501',
    '순남시래기' : '02-456-5486'
}

with open('lunch.csv', 'w', encoding='utf-8') as f:
    f.write('식당이름, 전화번호\n')
    for name, phone in lunches.items():
        f.write(f'{name}, {phone}\n')

# print(lunch)
# print(lunches[lunch])

# for k, v in lunches.items():
#     print(name, phone)