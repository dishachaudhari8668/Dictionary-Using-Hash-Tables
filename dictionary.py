
size = 10
hash_table = [[] for _ in range(size)]

def hash_function(word):
    return sum(ord(ch) for ch in word) % size

def add_word(word, meaning):
    index = hash_function(word)

    for item in hash_table[index]:
        if item[0] == word:
            item[1] = meaning
            print("Meaning updated!")
            return

    hash_table[index].append([word, meaning])
    print("Word added successfully!")

def search_word(word):
    index = hash_function(word)

    for item in hash_table[index]:
        if item[0] == word:
            print("Meaning:", item[1])
            return

    print("Word not found!")

while True:
    print("\n1. Add Word")
    print("2. Search Word")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter word: ").lower()
        meaning = input("Enter meaning: ")
        add_word(word, meaning)

    elif choice == "2":
        word = input("Enter word to search: ").lower()
        search_word(word)

    elif choice == "3":
        break

    else:
        print("Invalid choice!")

