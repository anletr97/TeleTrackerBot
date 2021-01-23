class Command:
    START = '/start'
    ADD = '/add'
    GET = '/list'
    HELP = '/help'
    DELETE = '/delete'
    pass

class Url:
    TIKI = 'https://tiki\.vn/'
    EXAMPLE_URL = TIKI + 'dien-thoai-iphone-12-pro-max-128gb-hang-chinh-hang-p70771651\.html'
    pass

class Message:
    WELCOME = 'Welcome to tiki price tracking bot. \n For more info please enter ' + Command.HELP
    ADD = 'Please enter tiki\'s URL'
    HELP_ADD  = 'Enter ' + Command.ADD + ' to add product URL'
    HELP_LIST = 'Enter ' + Command.GET + ' to get URL list'
    
    HELP = '```1. 1) ' + HELP_ADD + ' \n 2) ' + HELP_LIST + '```'