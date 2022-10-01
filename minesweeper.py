import random

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
location = []
pos_num = {}
bomb = []
size = int(input('size???: '))
sheet = {}
score = []
check = []


#######################################################
def near_bomb():
    for i in bomb:

        for k in range(size):
            for j in range(1, size + 1):
                pos = list[k] + str(j)
                # center
                if i[0] == list[k] and (i[1] == str(j + 1) or i[1] == str(j - 1)) and (pos not in bomb):
                    pos_num[pos] += 1
                # right
                elif i[0] == list[k - 1] and (i[1] == str(j + 1) or i[1] == str(j - 1) or i[1] == str(j)) and (
                        pos not in bomb):
                    pos_num[pos] += 1

                elif i[0] == list[k + 1] and (i[1] == str(j + 1) or i[1] == str(j - 1) or i[1] == str(j)) and (
                        pos not in bomb):
                    pos_num[pos] += 1

    ##############################################################


def find_near(i):
    near = []
    for k in range(size):
        if pos_num[i] > 0:
            sheet[i] = pos_num[i]
            break
        for j in range(1, size + 1):
            pos = list[k] + str(j)

            # center
            if (i == list[k] + str(j + 1)) or (i == list[k] + str(j - 1) or i == list[k] + str(j)) and (
                    pos not in bomb):
                sheet[pos] = (pos_num[pos])

                if pos not in score:
                    score.append(pos)
            # right
            elif (i == list[k - 1] + str(j + 1) or i == list[k - 1] + str(j - 1) or i == list[k - 1] + str(j)) and (
                    pos not in bomb):
                sheet[pos] = (pos_num[pos])

                if pos not in score:
                    score.append(pos)
                    # left
            elif (i == list[k + 1] + str(j + 1) or i == list[k + 1] + str(j - 1) or i == list[k + 1] + str(j)) and (
                    pos not in bomb):
                sheet[pos] = (pos_num[pos])

                if pos not in score:
                    score.append(pos)
    for f in score:
        if pos_num[f] == 0 and f not in check:
            check.append(f)
            command = find_near(f)



def checker(x):
    if x[0] == '1':
        sheet[x[2:4]] = 'F'

    elif x[0] == '2':
        sheet[x[2:4]] = '- '


################startttttt##########################
for i in range(size):
    for k in range(1, size + 1):
        pos = list[i] + str(k)
        sheet[pos] = '- '
        pos_num[pos] = 0
        location.append(pos)

for pp in range(size+1):
    print(pp, end ='| ')
    for j in range(size):
         if pp == 0:
            print(list[j], end= '  ')
         else:
            pos = list[j] + str(pp)
            print(sheet[pos] , end = '  ')
    print()

########################################
########################################
print(f'we have {size} bombs')
A = input('guess:').upper()
# make bomb
a = 0
random.shuffle(location)
while len(bomb) < size:
    if A != location[a]:
        mine = location[a]
        bomb.append(mine)
        pos_num[mine] = '*'
    a += 1
command = near_bomb()

print('มีระเบิด', size, 'ลูก')

####################################



while (A not in bomb) or (score != (size * size) - len(bomb)):
    if A in bomb:
        for i in bomb:
            sheet[i] = 'bomb'

        print('OH NO YOU JUST TOUCH THE BOMB TTT')

        break
    if A[0].isdigit():
        checker(A)
    else:
        find_near(A)

    for pp in range(size + 1):
        print(pp, end='| ')
        for j in range(size):
            if pp == 0:
                print(list[j], end='  ')
            else:
                pos = list[j] + str(pp)
                print(sheet[pos], end='  ')
        print()

    A = input('guess:').upper()

if (score == (size * size) - len(bomb)):
    print('YOU WIN CONGRAT!!')
    for i in bomb:
        sheet[i] = 'bomb'

for pp in range(size+1):
    print(pp, end ='| ')
    for j in range(size):
         if pp == 0:
            print(list[j], end= '  ')
         else:
            pos = list[j] + str(pp)
            print(sheet[pos] , end = '  ')
    print()

##################################