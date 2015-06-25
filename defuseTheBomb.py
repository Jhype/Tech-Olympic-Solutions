import sys
import itertools

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789abcdefghijklmnopqrstuvwxyz_$&#@ "

for length in range(0,20):

   for entry in itertools.product(alpha,repeat = length):
      password = ''.join(entry)
      print(password)

      if password == 'Hate':
         print('hit')
         sys.exit(0)