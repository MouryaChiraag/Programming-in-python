# string = "Python"
# vowels = ['a', 'e', 'i', 'o', 'u']
# for ch in string:
#     if ch in vowels:
#         print("This string contains vowel")
#     else:
#         print("This string doesnot contain a vowel")

# word = input("Enter a String : ")
# vowel = "aeiou"
# vowels = {i for i in word if i in vowel}
# print(vowels)

def check_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in word:
        if i in vowels:
            return True 
    return False 

word = input("Enter a word : ")
if check_vowel(word):
    print(f"{word} is a vowel")
else:
    print(f"{word} is not a vowel")
