
fp = open('1.txt', 'r')
fq = open('2.txt', 'w')
for line in fp.readlines():
    line = line.strip()

    if line.startswith('0'):
        print(line)
        fq.write(line + '\n')
    # if len(list(line)) > 7 :
    #     print(list(line))
    #     if list(line)[1] == '0' or list(line)[2] == '0':
    #         print(line)
    #         fq.write(line)


# with open('1.txt', 'r+') as f:
#     f.seek(3)
#     print(f.tell())

