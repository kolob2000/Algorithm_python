count = 0
for i in range(32, 128):
    if count % 10 != 0 or count == 0:
        print(f'{i}  {chr(i)}      ', end=' \t')
    else:
        print('\n')
        print(f'{i}  {chr(i)}       ', end=' \t')
    count += 1
