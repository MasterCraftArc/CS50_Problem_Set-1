thought = input('what is the Answer to the Great Question of life, the universe, and everything?: ')
def main(thought):
    if '42' in thought:
        print('Yes')
    elif 'forty-two'in thought:
        print ('Yes')
    elif 'forty two'in thought:
        print ('Yes')
    else:
        print('No') 
main(thought)