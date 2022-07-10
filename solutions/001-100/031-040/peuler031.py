# Project Euler - 31
# Date: 06/01/2022

counter = 1
for a in range(3):
    for b in range(5):
        if 100*a+50*b>200:
            break
        for c in range(11):
            if 100*a+50*b+20*c>200:
                break
            for d in range(21):
                if 100*a+50*b+20*c+10*d>200:
                    break
                for e in range(41):
                    if 100*a+50*b+20*c+10*d+5*e>200:
                        break
                    for f in range(101):
                        if 100*a+50*b+20*c+10*d+5*e+2*f<= 200:
                            counter += 1
print(counter)