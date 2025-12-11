# Q1:
# Write a Python program that takes a sentence from the user and prints:
# Number of characters
# Number of words
# Number of vowels
# Hint: Use split(), loops, and vowel checking.

s=input("Enter String: ")
words=s.split()

cnt=0
for word in words:
    cnt=cnt+len(word)

print("Number of Characters in string: ",cnt)
print("Number of words: ", len(words))

def count_vowels(text):
    count=0
    vowels="aeiouAEIOU"
    for char in text:
        if char in vowels:
            count+=1
    print("Number of vowels: ",count)

count_vowels(s)