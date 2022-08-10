
def remove(text,character):
    text = text.replace(character,'')
    return text

if __name__ == "__main__":
    text = input('Enter a String: ')
    character = input('Enter a Character to Remove: ')
    if character in text:
        print('The Character '+character+' has been removed, the new String is '+ remove(text,character))
    else:
        print('The Character does not exist in the provided string')