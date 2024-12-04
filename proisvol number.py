def single_root_words(root_word, *other_words):
    same_words = []
    root_word.lower()

    for i in other_words:
        root_lower = root_word.lower()
        words = i.lower()

        if root_lower in words or words in root_lower:
            same_words.append(i)

    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)