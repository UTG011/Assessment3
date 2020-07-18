word=input("Enter a word:")
def most_frequent(word):
    l=[]
    word=word.lower()
    for i in range(len(word)):
        l.append(word[i])
    letter_counts=dict()
    for letters in l:
        letter_counts[letters]=letter_counts.get(letters,0)+1
    sorted_dict=sorted(letter_counts.items(),key=lambda t:t[1], reverse=True)
    for letter,count in sorted_dict:
        print(letter,"=",count)


most_frequent(word)
