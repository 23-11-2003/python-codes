def vowel_or_consonant(x):
    if(x =='a' or x =='e'or x=='i'or x =='o'or x=='u'):
        return"vowel"
    else:
        return "consonant"
character = input("Enter a character:")
result = vowel_or_consonant(character)
print(result)