# importing time library to calculate the time it will take to execute our function
import time
# creating our class
class palindrome:
    def __init__(self, sentence):
        self.sentence=sentence
# creating our function that will split the sentence where there are white spaces
    def split_sentence(self):
# making words as a list to store words
        words=list(self.sentence.split())
# using for to get one word that is stored in word
        for word in words:
            print (word)
# checking if a word is a palindrome
            if(word[0::]==word[::-1]):
                print (f"{word} is a palindrome")
            else:
                print (f"{word} is not a palindrome")
# creating an object called pal then we pass a sentence to the class
pal= palindrome("33233 mam nun is my madam")
start=time.time()
pal.split_sentence()
end=time.time()
exec_time=end-start
print(f"execution time is {exec_time}")