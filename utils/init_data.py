def load_initial_data(server):
    key = 1
    server.set('{}'.format(key), 'init').addCallback(return_initial_data, server, key)
    key = 2
    server.set('{}'.format(key), 'hello').addCallback(return_initial_data, server, key)
    key = 3
    server.set('{}'.format(key), 'second').addCallback(return_initial_data, server, key)
    key = 4
    server.set('{}'.format(key), 'datas').addCallback(return_initial_data, server, key)


def done(result):
    print('key result returned: ' + str(result))


def return_initial_data(result, server, key):
    server.get('{}'.format(key)).addCallback(done)




