# Project Euler - 93
# Date: 14/07/2022

from itertools import permutations, combinations, combinations_with_replacement
from time import time

class Expression:
    pass

class Times(Expression):
    def __init__(self,l,r):
        self.l = l
        self.r = r

    def eval(self,env):
        return self.l.eval(env)*self.r.eval(env)

class Divide(Expression):
    def __init__(self,l,r):
        self.l = l
        self.r = r

    def eval(self,env):
        if self.l.eval(env)%self.r.eval(env) != 0:
            return self.l.eval(env)/self.r.eval(env)
        else:
            return self.l.eval(env)//self.r.eval(env)

class Plus(Expression):
    def __init__(self,l,r):
        self.l = l
        self.r = r

    def eval(self,env):
        return self.l.eval(env)+self.r.eval(env)

class Subtract(Expression):
    def __init__(self,l,r):
        self.l = l
        self.r = r

    def eval(self,env):
        return self.l.eval(env)-self.r.eval(env)
    
class Var(Expression):
    def __init__(self,name):
        self.name = name

    def eval(self,env):
        return env[self.name]

def find_consectutive_nums(sett):
    n = 1
    while(True):
        if n in sett:
            n+=1 
            continue
        else:
            return n-1
start = time()
operations = [Times,Divide,Plus,Subtract]
all_operations = list(combinations_with_replacement(operations,3))
ops = []
for op in all_operations:
    for asdf in list(permutations(op)):
        ops.append(asdf)
all_operations = list(set(ops))

digits = list(range(1,10))
all_digits = list(combinations(digits,4))

maximum = 0
for set_digits in all_digits:
    a,b,c,d = set_digits
    perms = list(permutations([a,b,c,d]))
    sett = set()
    for perm in perms:
        env = {"var1":perm[0],"var2":perm[1],"var3":perm[2],"var4":perm[3]}
        for set_ops in all_operations:
            op1,op2,op3 = set_ops
            es = []
            es.append(op1(Var("var1"),op2(Var("var2"), op3(Var("var3"),Var("var4")))))
            es.append(op1(op2(Var("var2"), op3(Var("var3"),Var("var4"))),Var("var1")))
            es.append(op1(Var("var1"),op2(op3(Var("var3"),Var("var4")), Var("var2"))))
            es.append(op1(op2(op3(Var("var3"),Var("var4")),Var("var2")),Var("var1")))
            es.append(op1(op2(Var("var1"),Var("var2")),op3(Var("var3"),Var("var4"))))
            for e in es:
                try:
                    temp = e.eval(env)
                    if temp<=0:
                        continue
                    else:
                        if type(temp) == int:
                            sett.add((temp))
                        elif type(temp) == float and temp.is_integer():
                            sett.add(int(temp))
                except:
                    continue
    curr_len = find_consectutive_nums(sett)
    if curr_len>maximum:
        maximum = curr_len
        x,y,z,w = a,b,c,d

print(x,y,z,w)
