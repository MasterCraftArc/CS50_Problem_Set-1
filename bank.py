greeting = input('Greeting: ')
def main (greeting) :
    if 'hello' in greeting or 'Hello' in greeting:
        print('$0')
    elif greeting.startswith('h' or 'H'):
        print('$20')
    else:
        print('$100')
main(greeting)