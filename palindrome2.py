def is_palindrome(word):
    return word == word[::-1]

def remove_palindrome_words(sentence):
    words = sentence.split()
    non_palindrome_words = [word for word in words if not is_palindrome(word)]
    return ' '.join(non_palindrome_words)

input_sentence = "He did a good deed"
output_sentence = remove_palindrome_words(input_sentence)
print(output_sentence)
