def overwrite(file):
    f = open(file, 'w')
    f.write('')
    f.close

def returngreater(var1, var2):
    if var1 >= var2:
        return var2
    else:
        return var1

def append(file, text):
    f = open(file, 'a')
    f.write(text)
    f.close

def readln(file):
    f = open(file, 'r')
    return f.read()
    f.close

def countlns(file):
    f = open(file, 'r')
    return len(f.readlines())

def convert2arr(file):
    f = open(file, 'r')
    array = []
    for line in f:
        array.append(line)
    f.close
    return array

def appendfile(file1, file2):
    f2 = convert2arr(file2)
    for i in range(0, countlns(file2)):
        append(file1, f2[i])

def ziplikeappend(file1, file2):
    f1copy = convert2arr(file1)
    f2copy = convert2arr(file2)
    overwrite(file1)
    maxindex = returngreater(len(f1copy), len(f2copy))
    for i in range(0, maxindex):
        append(file1, f1copy[i])
        append(file1, f2copy[i])

def appendopen(filename):
    f = open(filename, 'a')
    return f




if __name__ == "__main__":

    print("FOOOOOO")
