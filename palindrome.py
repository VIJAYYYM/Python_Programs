def is_palindrome(word):
    return word == word[::-1]
def remove_palindrome_words(input_str):
    words = input_str.split()
    non_palindrome_words = [word for word in words if not is_palindrome(word)]
    result_str = ' '.join(non_palindrome_words)
    return result_str
input_str1 = "He did a good deed"
input_str2 = "Hari speaks malayalam"
output_str1 = remove_palindrome_words(input_str1)
output_str2 = remove_palindrome_words(input_str2)
print(output_str1)
print(output_str2)
