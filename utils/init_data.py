def load_initial_data(server):
    server.set(1, [0, 'init'])
    server.set(2, [1, 'hello'])
    server.set(3, [2, 'second'])
    server.set(4, [3, 'datas'])


def done(result):
    print('key result returned: ' + str(result))


def return_initial_data(server):
    server.get(2).addCallback(done)




