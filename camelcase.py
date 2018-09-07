def camelcase(word):
    return word[0:1].upper() + word[1:].lower()

def main():

    sentence = input('Enter your sentence:  ')
    words = sentence.split(' ')
    camelcased_words = [ camelcase(word) for word in words ]
    camelcased_words[0] = camelcased_words[0].lower()
    output = ''.join(camelcased_words)

    print(output)

if __name__ == '__main__':
    main()


def camelcase(word):
    ''' Convert word to have uppercase first letter, rest in lowercase'''
    return word[0:1].upper() + word[1:].lower()
    # Slices don't produce index out of bounds errors.
    #  So this still works on empty strings, strings of length 1

def display_banner():
    '''Display program name in a banner'''
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')

def main():

    display_banner()

    sentence = input('Enter your sentence:  ')
    words = sentence.split(' ')
    camelcased_words = [ camelcase(word) for word in words ]
    camelcased_words[0] = camelcased_words[0].lower()
    output = ''.join(camelcased_words)
    print(output)

if __name__ == '__main__':
    main()

