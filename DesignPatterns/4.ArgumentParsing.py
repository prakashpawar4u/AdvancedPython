"""def myFunction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE'])
    print(kwargs['KEYTWO'])

myFunction('hey', True, 19, 'wow', KEYONE=1, KEYTWO=7)

"""

from email import message
import sys

#usage: 4.ArgumentParsing.py FILENAME

# print(sys.argv[0])            
# print(sys.argv[1])
# print(sys.argv)

# filename = sys.argv[1]
# message = sys.argv[2]

# with open(filename, 'w+') as f:
#     f.write(message)
#     f.close()

import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

print(f"OPTS : {opts}")
print(f"ARGS : {args}")

# for opt, arg in opts:
#     if opt == '-f':
#         filename = arg
#     if opt == '-m':
#         message = arg

    # print(message)
    # print(filename)
