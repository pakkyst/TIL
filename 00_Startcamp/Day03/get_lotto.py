import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text

data = json.loads(response)
# print(type(data), data)
print(data['bnusNo'])

real_numbers = []
# for i in range(6):
#     real_numbers[i] = data[f'drwtNo{i+1}']

for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)

print(real_numbers)


# print(response['bnusNo'])
