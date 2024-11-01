# 'gif' = 'image/gif'
# 'jpeg' = 'image/jpeg'
# 'jpg' = 'image/jpeg'
# 'png' = 'image/png'
# 'pdf' = 'application/pdf'
# 'txt' = 'text/plain'
# 'zip' = 'application/zip'

# else = 'application/octet-stream'

x = input('File Name: ').lower().strip()

lx = x.split('.')

try:
    if lx[-1] == 'gif':
        print('image/gif')

    elif lx[-1] == 'jpeg' or lx[-1] == 'jpg':
        print('image/jpeg')

    elif lx[-1] == 'png':
        print('image/png')

    elif lx[-1] == 'pdf':
        print('application/pdf')

    elif lx[-1] == 'txt':
        print('text/plain')

    elif lx[-1] == 'zip':
        print('application/zip')

    else:
        print('application/octet-stream')

except:
    IndexError
    print('application/octet-stream')
