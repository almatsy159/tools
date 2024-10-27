import sys
import os


# with this as 
def trt(arg):
    """
    with open(arg[0],"r") as f:
        res:list = f.readlines()
    """
    res = None
    file = arg[0]
    #pytoncode(file)
    try :
        res = read(file)
    except FileNotFoundError as err:
        print("is not a file !")
        try :
            res = os.system(f"curl {file}")
        except :
            res = "err"
            print("neither a link")
    else :
        print(res)
    finally :
        print("trt end")
    
    return res

def read(file):
    with open(file,"r") as f:
        res:list = f.readlines()
    return res
    
def pytoncode(file):
    res = exec(file)
    return res

def main(argv):
    #input_file = sys.argv
    #input_file = input()
    res:list = []
    if argv[1:] != []:
        print(f"hey arg here {argv[1:]}")
        res:str = trt(argv[1:])
    else:
        print( "No arg here =(")
    #input_file = input(sys.stdin)
    #with open(sys.stdin,"r") as f:
    #    input_file = f.readlines()
    
        
    name,args = argv[0],argv[1:]
    return {"name":name,"args":args,"res":res}


if __name__ == "__main__":
    res:dict = main(sys.argv)
    #print(sys.stdin)
    print(res)