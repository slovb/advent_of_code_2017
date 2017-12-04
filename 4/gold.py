def test(phrase):
    words = phrase.split()
    memory = []
    for word in words:
        wordList = list(word)
        wordList.sort()
        word = ''.join(wordList)
        if word in memory:
            return False
        memory.append(word)
    return True

def read(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main(filename):
    phrases = read(filename)
    counter = 0
    for phrase in phrases:
        if test(phrase):
            counter += 1
    print counter
    

if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        main(f)
