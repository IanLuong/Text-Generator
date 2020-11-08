corpus = open(input("Input the path to the txt file"), "r", encoding="utf-8")
all_tokens = corpus.read().split()
# unique_tokens = set(all_tokens)

bigrams = [[all_tokens[j] for j in range(i, i + 2)] for i in range(len(all_tokens) - 1)]
# for i in range(len(all_tokens)-1):
#    to_be_appended = []
#    for j in range(i, i+2):
#        to_be_appended.append(all_tokens[j])
#    bigrams.append(to_be_appended)


# print("Corpus statistics:\n"
#      "All tokens:", len(all_tokens), "\n"
#                                      "Unique tokens:", len(unique_tokens))

print("Number of bigrams:", len(bigrams))

running = True
while running:
    user_input = input()
    if user_input == "exit":
        running = False
    else:
        try:
            print(f"Head: {bigrams[int(user_input)][0]}\tTail: {bigrams[int(user_input)][1]}")
        except ValueError:
            print("Type Error. Please input an integer.")
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
