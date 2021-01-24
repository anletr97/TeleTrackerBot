'''Store my constants here'''

class Command:
    '''Constant for command'''
    START = '/start'
    ADD = '/add'
    GET = '/list'
    HELP = '/help'
    DELETE = '/delete'

class File:
    '''Constant for file'''
    NAME= 'data.json'

class Message:
    '''Constant for message'''
    WELCOME = 'Welcome to tiki price tracking bot. \n For more info please enter ' + Command.HELP
    ADD = 'Please enter tiki\'s URL'
    HELP_ADD  = 'Enter ' + Command.ADD + ' to add product URL'
    HELP_LIST = 'Enter ' + Command.GET + ' to get URL list'
    HELP = '```1. 1) ' + HELP_ADD + ' \n 2) ' + HELP_LIST + '```'

    def get_message(self, name, price, image):
        '''Message gonna be sent back to user'''
        # name = name[0, int(.find('-'))]
        price = format(int(price), ",")
        return '*'+ name + '*' + '\n *' + price +'*'  + '\n' + image.replace(r'\.', '.')
