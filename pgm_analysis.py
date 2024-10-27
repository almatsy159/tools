import os 
import glob 
import re

import time
import datetime

import mysql.connector as mc
import setting as s


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbn

# must make a setting.py file containing value for db connection

# execute in the dir that will be analysed
# be careful there is a collab about this program too ... 
class DB:
    def __init__(self,user=s.LOGIN,pwd=s.PWD,host=s.HOST,db=s.DB):
        self.db = db
        self.user = user
        self.host = host
        self.connect(pwd)
        #self.struct = self.struct_db()
        #print(self.struct)
        
    def connect(self,pwd,user=None):
        if user == None:
            user = self.user
        self.conn = mc.connect(user=user,host=self.host,passwd=pwd,database=self.db)
    
    def commit(self):
        self.conn.commit()
    def make_req(self,req="select * from program;"):
        cursor = self.conn.cursor()
        cursor.execute(req)
        res = cursor.fetchall()
        # trt single many here 
        #self.commit()
        cursor.close()
        if res != []:
            print(req,"=>",res)
        else : 
            print(req)
        return res
    
    def struct_db(self):
        res =""
        i1 = f"USE {self.db}"
        self.make_req(i1)
        i2 = "SHOW TABLES"
        
        tables = self.make_req(i2)
        res = {}
        for t in tables:
            #print(t[0])
            res[t] = []
            i3 = f"SHOW COLUMNS from {t[0]};"
            cols = self.make_req(i3)
            res[t].append(cols)
            
        return res
            


            
            
        #process = []
        
        
    
    
        

def get_file_content(fname):
    #nb = 0
    with open(fname,"r") as f:
        content = []
        for l in f.readlines():
            content.append(l)
            #nb += 1
    #print(content)
    return content
    

def get_file(fname):
    with open(fname,"r") as f:
        content = f.readlines()
    
    return content

class Program:
    def __init__(self,name,path="./",ext="txt"):
        self.name = name
        self.blocs = []
class Cls:
    def __init__(self,name,beg):
        self.name = name
        self.beg = beg
        self.pattern = r""

class Bloc:
    def __init__(self,pgm,beg=0,range=0):
        self.pgm = pgm
        self.beg = beg
        self.end = beg + range
        
class PyProgReport:
    id = 0
    def __init__(self,fname,db=None):
        # modProg1 union modProg2
        
        self.id_report = self.id
        PyProgReport.id += 1
        self.fname = fname
        self.nb_mod = 0
        self.nb_cls = 0
        self.stat = os.stat(fname)
        self.content = self.get_content()
        self.file = self.get_file()
        self.nb_line = len(self.content)
        self.modules = self.get_mod()
        self.cls= self.get_cls()
        self.get_name_and_ext()
        self.fs = []
        self.get_prop()
        print(self)
        #print(time.localtime(self.st_ctime))
        #self.values = self.fname,self.st_ctime
        
        # uncoment to create (should be if not exist) 
        #self.insert()
    
    def __str__(self):
        res = f"{self.id} {self.name} :\nclass : {str(self.cls)}\nlines : {self.nb_line}"
        return res
    def umode(self,other):
        res = {}
        for ms in self.modules:
            for mo in other.modules:
                if ms == mo :
                    res[self] = ms
        return res
    def get_prop(self):
        #for i in self.stat:
        #    print(i)
        self.st_mode= self.stat[0]
        self.st_ino = self.stat[1]
        self.st_dev = self.stat[2]
        self.st_nlink = self.stat[3]
        self.st_uid = self.stat[4]
        self.st_gid = self.stat[5]
        self.st_size = self.stat[6]
        self.st_atime = self.stat[7]
        self.st_mtime = self.stat[8]
        self.st_ctime = self.stat[9]
        self.get_name_and_ext()
        
        return self.stat
        #print(a)
    def get_content(self):
        return get_file_content(self.fname)
        
    def get_file(self):
        #my_str = ""
        #for i in get_file(self.fname):
            #my_str+= str(i)
        #return my_str
        return get_file(self.fname)
    
    def insert(self):
        
        req = f"insert into program values ('{self.fname}',{self.st_ctime});"
        res = self.db.make_req(req)
        self.db.commit()
        print("req : ",req,"\nres : ",res)
        self.insert_prop()
        
    def insert_prop(self):
        for c in self.get_comment
        
    
    def insert_comment(self,comment=""):
        req = f"insert into comment values ('{self.fname}',{comment})"
        res = self.db.make_req(req)
        self.db.commit()
        print("req : ",req,"\nres : ",res)
        
    def get_name_and_ext(self):
        pattern = r"(\w*)\.(\w*)"
        pattern = re.compile(pattern)
        res = re.search(pattern,self.fname)
        #print(res[0],res[1],res[2])
        self.name = res[1]
        self.ext = res[2]  
    
    def get_cls(self):
        # class name !!
        
        
        matchs = []
        #pattern = re.compile(r"class \w*")
        pattern = re.compile(r"class (\w*) ?(\( ?\w*\))?:")
        for l in self.content:
            #print(l)
            cl = pattern.findall(l)
            #cl = re.search(pattern,l)
            #print(type(cl))
            if cl !=[]:
                #if cl != None:
                
                #matchs.append(cl.group(1))
                #print("cl[0][0]:",cl[0][0])
                matchs.append(cl[0][0])
                #print(self.get_class_name(cl[0]))
            self.nb_cls = len(cl)
        #print(matchs)
        return matchs
        
    def get_class_name(self,my_str):
        pattern = re.compile(f"class (\w*)")
        y = re.search(pattern,my_str)
        #print("y :",y)
        
    def get_mode_name(self,my_str):
        pattern = re.compile(f"import (\w*)")
        
    def get_mod(self):
        matchs = []
        pattern = re.compile(r"import (\w*)")


        for l in self.content:
            cl = pattern.findall(l)
            
            if cl !=[]:
                matchs.append(cl)
                print(f"{fname} cl: {cl}")
                """
                #self.nb += 1
                for r in cl:
                    if len(r)> 1:
                        if r[2] != "":
                            #print(r[2])
                            matchs.append(r[2])
                        else:
                            #print("r:",r)
                            matchs.append(r[0])
                """
                """
                print(cl[0])
                #print(cl[0][2])
                if cl[0][2] == '':
                #print(cl)
                    print("other")
                    matchs.append(cl[0][0])
                else:
                    print("this case")
                    matchs.append(cl[0][2])
            """
            #else:
            #    print(self.fname)
            
        print("match",matchs)
        if len(matchs) == 1:
            pass
        else:
            #print(len(matchs))
            pass
        #if nb> self.
        self.nb_mod = len(matchs)
        return matchs

    def get_alias(self,my_str):
        matchs = []
        pattern = re.compile(r"")
        for l in self.content:
            cl = pattern.findall(l)
            #print(type(cl))
            if cl !=[]:
                
                matchs.append(cl)
        #print(matchs)
        
    def get_pattern(self,my_str):
        matchs = []
        pattern = re.compile(my_str)
        for l in self.content:
            cl = pattern.findall(l)
            #print(type(cl))
            if cl !=[]:
                matchs.append(cl)
        
        #print(matchs)
        return matchs
        
    def search(self,my_str,pattern):
        pattern = re.compile(pattern)
        res = re.search(pattern,my_str)
        #print(res)
        return res
    
    def get_in_class(self,cname):
        #pattern = rf"class {cname}( \w*)?( *)?:\\n( *)(\w *)*"
        #pattern = rf"(class {cname}:)\\n(( *\w|\W)*\\n)*"
        pattern_cls = rf"(class {cname} ?(\(\w*\)))"
        pattern_cls = re.compile(pattern_cls)
        #print(self.get_file())
        # get line
        matches = {}
        for i,f in enumerate(self.get_file()):
            m = re.match(pattern_cls,f)
            #print(m)
            if m != None:
                matches[i] = f
                
        print("match",matches)
        cls_dict = matches
        
        #print(self.nb_line)
        
        pattern_indent = r"^( )*\w*"
        pattern_indent = re.compile(pattern_indent)
        flag = 0
        beg = 0
        end = 0
        for l,f in matches.items():
            beg = l
            end = beg
            if flag == True:
                #x =re.match(pattern_indent,f)
                #print(x)
                for lb in self.content[beg+1:self.nb_line-beg]:
                    x = re.match(pattern_indent,lb)
                    #print("matches : ",x)
                    if x != []:
                        end +=1
                    else :
                        flag=False
                #flag = False
            print("beg : ",beg,"; end : ",end)
                    
            if l in cls_dict.keys():
                flag = True
                #for i in range(l,self.nb_line):
                #if re.match(pattern_ident)
                print("l : ",l,"f : ",f)
                #print(f"line {i}",re.match(pattern_cls,f))
            
            #if re.match(pattern,f):
            #print(f)
            #print(re.findall(pattern,f))
        #for f in self.get_file():
        #matches= re.match(pattern,f)
        #matches = re.match(pattern,self.get_file())
        #print(matches)
    
    def get_comment(self):
        comments = {}
        pattern = re.compile(r"(#)|(\"\"\")")
        count = 0
        for l in self.content:
            if re.match(pattern,l) != None:
                #if re.match(pattern,l).groupdict() != {}:
                #print(re.match(pattern,l).group())
                comments[count] = l
                count += 1
        return comments
        
        
    
    
        

def get_first(t1,t2):

    for i in range(len(t1)):
        if t1[i] > t2[i]:
            return t2
        elif t1[i] < t2[i]:
            return t1


if __name__ == "__main__":
    # test without arg
    #db = DB()
    #res0 = db.make_req()
    
    # test with os
    #print(help(os))

    #for i in os.environ:
    #    print(i)

    #print(os.error)
    #print(os.ctermid())
    #print(os.environ)
    #print(os.environb)
    #print(os.getenv())
    #os.chdir()
    # file to write result on 
    # . py ?.txt... not treated yet
    report_file = "report.txt"

    dir_name = os.getcwd()
    #print(os.fchdir())


    prog_in_dir = glob.glob(f'{dir_name}/*.py')

    #prog_in_dir = ["map.py"]
    #print(prog_in_dir)
    content = ""

    # getting all prog in dir content
    for fname in prog_in_dir:
        #print(fname)
        with open(fname,"r") as f:
            content = f.read()
        
    #print(content)
    

    # create db to store pgm and carac of pgm
    db = DB(db="program")
    
    #db.make_req(f"insert into program values ('test0',CURRENT_DATE())")
    #db.commit()
    # default "./"
    # import path !
    
    # get prog from dir and making a report of it
    print(db.struct_db(),"\n END")
    progs = {}
    
    for fname in prog_in_dir:
        
        progs[fname] = PyProgReport(fname,db)


    db.make_req()
    #### /!\ !!!
    #db.make_req("delete from program;")
    #db.commit()
    #db.make_req()
    #print(progs)

    res = {}
    res_class = {}
    res_mod = {} 
    res_crea = {}
    pfx = "######################################"
    sfx = pfx
    
    for name,prog in progs.items():
        print(pfx,name,sfx)
        res[name] = {"cls":[],"mod":[],"crea":int,"nb_m":int,"nb_c":int}
        
        c = prog.get_cls()
        if c != []:
            res_class[name] = c
            #for ci in c:
            res[name]["cls"] = c
            
        m = prog.get_mod()
        if m != [] :
            res_mod[name] = m
            #for mi in m:
            res[name]["mod"]= m
        cmt = prog.get_comment()
        
        res_crea[name] =  prog.st_ctime
        res[name]["crea"] = prog.st_ctime
        res[name]["nb_m"] = len(res[name]["mod"])
        res[name]["nb_c"] = prog.nb_cls
        res[name]["nb_m"] = prog.nb_mod
        
        #for cls in c:
        #    bloc = prog.get_in_class(cls)
        

    print('res : ',res)
    #for name,content in res.items():
    #    print(f"{name} :\n\t{content}")


    lst_mod = []
    lst_mod2 = []
    pgm = {"name":{"cls":[],"mod":[]}}
    for c in res_class:
        #print(f"{i} : {res_class[i]}")
        #pgm["cls"].append(i) 
        pass
    for m in res_mod:
        #print(f"{i} : {res_mod[i]}")
        for j in res_mod[i] :
            if j not in lst_mod2: 
            
                lst_mod2.append(j)
        if res_mod[i] not in lst_mod:
        # tri instead of happend => check equality after transform : [mod2,mod1] => [mod1,mod2] => "mod1+mod2" != "mod2+mod1" !!!
            lst_mod.append(res_mod[i])
    
    #for com in comments
        

### get value for each program   
"""
#print("lst_mod :",lst_mod)
modules = {}

#print("lst_mod2 :",lst_mod2)
for i,j in enumerate(lst_mod2):
    modules[i] = j
    
# mod in prog
mip = {}
for i,m in modules.items():
    mip[m[0]] = 0
    for name,prog in progs.items():
        if m in prog.modules :
            mip[m[0]] += 1

print(modules)
print(mip)
            
        
"""

#print(res)


# Tests for prog report
"""
test = PyProgReport("perso.py")
y0 = test.get_mod()
y1 = test.get_cls()
print(y0)
print(y1)
"""
#print(help(os.stat))
"""
sum = 0
for i,j in mip.items():
    sum += 1
    plt.scatter(i,j)
"""
#sans_mod = len(progs)-j
#plt.scatter("None",sans_mod)
#plt.scatter("Total",len(progs))
    #tmp = {j:mip[i]}

# to plot 
#b = 1
#e = 10
#x = [xi for xi in range(b,e)]
#y = [(yi**2) for yi in x]
#def get_y(lst):
#    for i in lst:

# test with 2n+1 pyramid
def square(n=1):
    #res = 0
    res = 1
    to_add = 1
    #last = 0
    while i < range(n-1):
        to_add =  to_add + 2
        res += to_add
        
        # 
        # 2*i b,e = 5,13 => [13, 21, 31, 43, 57, 73, 91, 111]
        # 2*i+1 b,e = 5,13 => [17, 26, 37, 50, 65, 82, 101, 122]
        i+=1
    return res


### PLOT 
"""
z = [square(zi) for zi in x]
print(x)
print(y)
print(z)
#plt.show()
plt.figure(figsize=(12,8))
plt.title("prog analysis")
plt.plot(x,y,label = "y(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.plot(x,z,label="z(x)")
plt.show()
"""