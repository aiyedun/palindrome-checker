def is_palindrome(string):
    string = string.replace(" ","")
    string = string.lower()
    return string == string[::-1]

print(is_palindrome("Nurses run"))