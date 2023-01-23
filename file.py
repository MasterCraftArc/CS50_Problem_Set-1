file = input('please enter a file type: ')

if '.gif' in file:
    print('image/gif')
elif '.jpg' in file or '.jpeg' in file:
    print('image/jpeg')
elif '.png' in file:
    print ('image/png')
elif '.pdf' in file:
    print('file/pdf')