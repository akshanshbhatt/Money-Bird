def emin(symbol):
    if symbol == 'AAPL':
        poi = '''"Tim Cook"'''
    elif symbol == 'GOOGL':
        poi = '''"Sundar Pichai'''
    elif symbol == 'MSFT':
        poi = '''"Satya Nadella"'''
    elif symbol == 'AMZN':
        poi = '''"Jeff Bezos" OR "Andy Jassy"'''
    elif symbol == 'FB':
        poi = '''"Mark Zuckerberg"'''
    elif symbol == 'TWTR':
        poi = '''"Jack Dorsey" OR "Parag Agarwal"'''
    elif symbol == 'CSCO':
        poi = '''"Larry Ellison"'''
    elif symbol == 'TSLA':
        poi = '''"Elon Musk"'''
    return poi

print(emin('AAPL'))
