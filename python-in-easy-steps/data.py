import pickle, os
if not os.path.isfile('pickle.dat'):
    data = [0, 1]
    data[0] = input('enter topic:')
    data[1] = input('enter series:')
    file = open('pickle.dat', 'wb')
    pickle.dump(data, file)
    file.close()
else:
    file = open('pickle.dat', 'rb')
    data = pickle.load(file)
    file.close()
    print('welcome back to:' + data[0] + ',' + data[1])
