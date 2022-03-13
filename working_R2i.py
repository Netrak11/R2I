import sys
def convert_r2i(s):
    rome = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    slug = 0
    for i in range(len(s)):
        if i+1 != len(s) and rome[s[i]]<rome[s[i+1]]:
            slug -= rome[s[i]]    
        else:
            slug += rome[s[i]]
    return slug

def convert_i2r(inum):
  num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
  rome = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
  i = 12
  rome_num = ''
  while inum != 0:
    if num[i] <= inum:
      rome_num += rome[i]
      inum -= num[i] 
    else:
      i -= 1 
  print(rome_num)

def runBatchMode(arg):
  a = 0
  file1 = open(arg, "r")
  file_out = open("Output.txt", "a")
  for n in file1:
    n = n.strip()
    if n.isdigit():
      a+=int(n)
      file_out.write(int(convert_i2r(a)))
      file_out.write("\n")
      a = 0
    elif (isRoman(n) == True):
      file_out.write(str(convert_r2i(n)))
      file_out.write("\n")
    else:
      print("No")

def isRoman(tar):
 rome = {'I','V','X','L','C','D','M'}
 if type(tar) == int:
   return False 
 elif tar.isnumeric():
  return False
 for i in range(len(tar)):
   if tar[i] not in rome:
     return False
 return True

def runCmdLineMode(arg):
    if (isRoman(arg)== True):
      print(convert_r2i(str(arg)))
    elif type(arg) == int:
      print(convert_i2r(int(arg)))
    elif arg.isnumeric():
      print(convert_i2r(int(arg)))
    else:
      print("NOPE")

def runInteractiveMode():
  while(1):
    v1 = input("Give me a value: ")
    if v1 == "quit":
      return
    if (isRoman(v1)== True):
      print(convert_r2i(v1))
    elif v1.isnumeric():
      print(convert_i2r(int(v1)))
    else:
      print("Error")

def setMode():  
 if len(sys.argv) == 1:
   return runInteractiveMode()
 if len(sys.argv) == 2:
   return runCmdLineMode(sys.argv[1])
 if ".txt" in (str(sys.argv[1])):
   return runBatchMode(sys.argv[1])

setMode()



