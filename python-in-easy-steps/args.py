def echo(user, lang, sys):
    print('user:', user, 'language:', lang, 'platform:', sys)
echo('mike', 'python', 'windows')
echo(lang='python', sys='mac os', user='anne')
def mirror(user='carole', lang='python'):
    print('\nuser:', user, 'language:', lang)
mirror()
mirror(lang='java')
mirror(user='tony')
mirror('susan', 'c++')