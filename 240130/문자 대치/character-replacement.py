word = input()

word = word.replace('XXXX', 'aaaa')
word = word.replace('XX', 'bb')

print(word if word.count('X') == 0 else -1)