def load_initial_data(server):
    server.set('1', 'init').addCallback(return_initial_data, server)
    server.set('2', 'hello')
    server.set('3', 'second')
    server.set('4', 'datas')


def done(result):
    print('key result returned: ' + str(result))


def return_initial_data(result, server):
    server.get('1').addCallback(done)




