import scipy.io as si
import re

def Arrange(filename,filepath):
    rs = []
    for line in filename.readlines()[2:]:
        line = re.sub(' +\t*','\t',line)  
        line = line.split('\t')
        rs.append([line[2],line[1],line[6]])
    rs = sorted(rs)
    return rs    

def TimeTransfer(filename,filepath):
    rs = Arrange(filename,filepath)
    newrs = []
    for i in rs:
        timesplit = i[1].split(':')
        hour = int(timesplit[0])*60*60*1000
        minute = int(timesplit[1])*60*1000
        second = int(timesplit[2].split('.')[0])*1000
        time = hour+minute+second+int(timesplit[2].split('.')[1])
        newrs.append([i[0],float(time),int(i[2])])
    return newrs

def WriteIntoDict(filename,filepath):
    rs = TimeTransfer(filename,filepath)
    mac = []
    for i in rs:
        if i[0] not in mac:
            mac.append(i[0])
    dictionary = []
    for i in mac:
        dictionary.append({i:[]})
    for i in range(len(dictionary)):
        for element in rs:
            if element[0] in dictionary[i]:
                dictionary[i][element[0]].append([element[1],element[2]]) 
    return dictionary

def WriteIntoMat(filename,filepath,prefix):
    dictionary = WriteIntoDict(filename,filepath)
    for dic in dictionary:
        for i in dic:
            i = i.replace(':','_')
            si.savemat(prefix+str(i)+'.mat',dic)
            
def main():
    fp = open(r'E:\code\Beacon\first_20141215T165105.txt','r')
    filepath = r'E:\code\Beacon\first_20141215T165105.txt'
    prefix = '2m_'
            
    WriteIntoMat(fp,filepath,prefix)    
    
if __name__ == '__main__':
    main()