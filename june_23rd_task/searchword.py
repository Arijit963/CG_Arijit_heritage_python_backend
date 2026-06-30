def search_word(words, target):

    for word in words:

        if word == target:
            return True

    return False


print(search_word(["apple", "banana", "mango"], "banana"))