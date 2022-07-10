# Project Euler - 17
# Date: 31/05/2022

def first_nineteen_digits_to_len(num):
    lst = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    return len(lst[num])

def tugur_to_len(num):
    lst = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    return len(lst[num])

def find_length(num):
    num = str(num)
    if len(num) == 1 or (len(num) == 2 and int(num)<20):
        return first_nineteen_digits_to_len(int(num))
    elif len(num) == 2 and int(num)>=20:
        return tugur_to_len(int(num[0])) + first_nineteen_digits_to_len(int(num[1]))
    elif len(num) == 3:
        if num[2] == '0' and num[1] == '0':
            return first_nineteen_digits_to_len(int(num[0])) + len('hundred')
        elif num[2] == '0' and num[1] != '0':
            return first_nineteen_digits_to_len(int(num[0])) + len('hundred') + len('and') + tugur_to_len(int(num[1]))
        elif num[1] == '1':
            return first_nineteen_digits_to_len(int(num[0])) + len('hundred') + len('and') + first_nineteen_digits_to_len(int(num[1:]))
        else:
            return first_nineteen_digits_to_len(int(num[0])) + len('hundred') + tugur_to_len(int(num[1])) + len('and') + first_nineteen_digits_to_len(int(num[2]))
    elif len(num) == 4:
        return len('onethousand')
    else:
        print(num)
        raise Exception('what da heck')




sum = 0
for i in range(1,1001):
   sum += find_length(i)
print(sum)