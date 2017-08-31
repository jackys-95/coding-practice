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

def check_score(sentence):
    total = 28
    correct = 0
    target = "methinks it is like a weasel"
    for i in range(total):
        if sentence[i] == target[i]:
            correct += 1
    return correct / total
    
def main():
    highscore = -1
    highscoresentence = ""
    i = 0
    while highscore != 100.0:
        score = 0
        if (i + 1) % 1000 == 0:
            print(highscore, highscoresentence)
            i = 0
        sentence = construct_random_sentence()
        score = check_score(sentence)
        if score > highscore:
            highscore = score
            highscoresentence = sentence
        i +=1

if __name__ == "__main__":
    main()
