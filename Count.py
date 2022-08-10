
def count(text,character):
    count = 0
    for i in range(len(text)):
        if text[i]== character:
            count += 1
    return count

if __name__ == "__main__":
    text = input('Enter a String: ')
    character = input('Enter a Character: ')
    if character in text:
        print('The Character '+character+' has been repeted in the string '+ str(count(text,character))+' times')
    else:
        print('The Character does not exist in the provided string')