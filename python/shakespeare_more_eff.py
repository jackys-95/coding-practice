import string, random

def get_alphabet_space():
    alphabet_space = [x for x in string.ascii_lowercase]
    alphabet_space.append(' ')
    return alphabet_space

def construct_random_sentence():
    alphabet_space = get_alphabet_space()
    result = ""
    for i in range(28):
        result += alphabet_space[random.randint(0, 26)]
    return result

def get_random_character():
    alphabet_space = get_alphabet_space()
    return alphabet_space[random.randint(0, 26)]

def get_sentence_tokens(sentence, target):
    '''
    tokenizes sentence and replaces incorrect elements with '*'
    '''
    tokens = []
    for i in range(28):
        if sentence[i] == target[i]:
            tokens.append(sentence[i])
        else:
            tokens.append('*')
    return tokens
    
def main():
    start_str = construct_random_sentence()
    target = "methinks it is like a weasel"
    tokens = get_sentence_tokens(start_str, target)
    print(tokens)

    count = 0
    for token in tokens:
        if token == "*":
            char = ''
            while char != target[count]:
                char = get_random_character()
            tokens[count] = char
        count += 1

    print("".join(tokens))

if __name__ == "__main__":
    main()
