# words = input('입력 고고: ')

# words 의 첫 글자와 마지막 글자를 출력하라
# first last
# print

# numbers = [1, 2, 3, 4, 5]

# numbers 의 첫 요소와 마지막 요소를 출력하라

# import random
# length = random.choice(range(1, 100))
# numbers = list(range(length))
# length - 1 ex. length = 50 [1, 2, ... 49]
# numbers[-1] : 마지막숫자
# print(numbers[length-1])
# print(numbers[-1])
# print(type(words))
# print(words[0], words[-1])

# my_list = list(words)
# print(type(my_list[0], my_list[-1]))


# 자연수 n 을 입력받고, 1부터 n까지 출력하라

# n = input('자연수를 입력하세요') 
# print(type(n))
# n = int(n) # str은 리스트가 될 수 있다. str => list(str) / str => int(str)
# print(type(n))

# n = input('자연수를 입력하세요')
# # n = 10
# n = int(n)
# for i in range(n):
#     print(i + 1, end=' ')
#     # end=' '

# 짝수/홀수를 구분하자, 2=> 짝!, 1=> 홀!
# string = input('숫자를 입력하세요: ')
# numbers = int(string)

# if numbers %2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# fizz buzz => 3의 배수에서 fizz를 나오게, 5의 배수에서 buzz, 15의 배수에서 fizz buzz
numbers = input('자연수를 입력하세요')
numbers = int(numbers)
# for i in range(1, numbers + 1):
#     print(i)
#     if i % 15 == 0:
#         print('fizz buzz')
#     elif i % 5 == 0:
#         print('buzz')
#     elif i % 3 == 0:
#         print('fizz')
#     else:
#         print(i)

for i in range(1, numbers + 1):
    if i % 15 == 0:
        print('fizz buzz')
    elif i % 5 == 0:
        print('buzz')
    elif i % 3 == 0:
        print('fizz')
    else:
        print(i)
