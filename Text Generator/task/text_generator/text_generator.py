corpus = open(input(), "r", encoding="utf-8")
all_tokens = corpus.read().split()  # TODO fix the RegExp to add tokens with punctuation
unique_tokens = set(all_tokens)

print("Corpus statistics:\n"
      "All tokens:", len(all_tokens), "\n"
                                      "Unique tokens:", len(unique_tokens))
running = True
while running:
    user_input = input()
    if user_input == "exit":
        running = False
        break
    elif user_input.isalpha():
        print("Type Error")
    else:
        if int(user_input) >= len(all_tokens):
            print("Index Error")
        else:
            print(all_tokens[int(user_input)])