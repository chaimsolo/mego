import txt

words = {"123456789": 0}
# txt.txt = input("Enter here the text you want to check >>> ")
txt.txt = txt.txt.split(" ")
for word in txt.txt:
    words.setdefault(word, 0)
    words[word] += 1
print(words)
max_occurrence = second_max_occurrence = third_max_occurrence = -1
common_word = second_common_word = "123456789"
for word in words:
    if words[word] > third_max_occurrence:
        if words[word] > second_max_occurrence:
            if words[word] > max_occurrence:
                third_max_occurrence = second_max_occurrence
                third_common_word = second_common_word
                second_max_occurrence = max_occurrence
                second_common_word = common_word
                max_occurrence = words[word]
                common_word = word
            else:
                third_max_occurrence = second_max_occurrence
                third_common_word = second_common_word
                second_max_occurrence = words[word]
                second_common_word = word
        else:
            third_max_occurrence = words[word]
            third_common_word = word


print(f"The most common word is {common_word} with {max_occurrence} times.\n"
      f"The second common word is {second_common_word} with {second_max_occurrence} times.\n"
      f"The third common word is {third_common_word} with {third_max_occurrence} times.")


