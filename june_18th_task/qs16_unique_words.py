sentence = input("Enter a sentence: ")

unique_words = set(sentence.lower().split())

print("Unique Words:")

for word in sorted(unique_words):
    print(word)