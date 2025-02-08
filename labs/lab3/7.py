def grams_to_ounces(grams):
    return 28.3495231 * grams
#Конвертация граммов в унции
print(grams_to_ounces(5))


def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
#Конвертация температуры из Фаренгейта в Цельсий

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return None  # Решение задачи с курицами и кроликами

# Фильтрация простых чисел из списка
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(nums):
    return [num for num in nums if is_prime(num)]

#    Перестановки строки
import itertools
def string_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]


#Переворачиваем слова в предложении

def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))


#Проверка на наличие двух "3" рядом в списке
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False


# Проверка на наличие последовательности 007 в списке

def spy_game(nums):
    spy_sequence = [0, 0, 7]
    index = 0
    for num in nums:
        if num == spy_sequence[index]:
            index += 1
        if index == 3:
            return True
    return False

#Вычисление объема сферы

import math
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

#Возврат нового списка с уникальными элементами (без использования set)
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

#Palindrome
def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()  # Убираем все неалфавитные символы и приводим к нижнему регистру
    return s == s[::-1]

# Печать гистограммы из списка чисел
def histogram(lst):
    for num in lst:
        print('*' * num)

#Игра "Угадай число"
      
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break








