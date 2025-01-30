def count_words_and_letters(sentence):
    words = sentence.strip().split()
    num_words = len(words)
    
    letters = sum([len(word) for word in words])
    return num_words, letters

def main():
    user_input = input("Введіть речення: ")
    num_words, num_letters = count_words_and_letters(user_input)
    print(f"Ваше речення містить в собі {num_words} слів, а також {num_letters} символів.")

if __name__ == "__main__":
    main()