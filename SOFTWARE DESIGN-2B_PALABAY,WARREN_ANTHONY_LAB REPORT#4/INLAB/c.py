def reverse(s):
    if s != '':
        reverse(s[1:])
        print(s[0], end='')
reverse('pots&pans')


