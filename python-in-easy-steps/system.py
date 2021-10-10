import sys, keyword
print('python version:', sys.version)
print('python interpreter location:', sys.executable)
print('python module search path:')
for dir in sys.path:
    print(dir)
print('python keywords:')
for word in keyword.kwlist:
    print(word)