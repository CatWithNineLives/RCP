from tf import *
from itertools import chain
###concatenating cycles to paths
def sP(r,gr):
    flag=0
    synchronising=[]
    synchronisingP=[]
    for key in gr:
        if key==r: #synchronising word for r
           c=gr[key][key] #list of cycles of key
           for i in range(0,len(c)):
               cycle=c[i] #taking cycles of key one by one
               for j in range(1,9):
                   if j!=key: #since we're only considering paths here
                        p=gr[j][key] #list of all paths from j to key
                        for m in range(0,len(p)):
                            path=p[m] #taking paths one by one
                            pc=path+cycle
##                            print(m,"th path for",i,"th cycle",pc)
                            flag=syncP(pc)
                            if flag==1:
                                seq=color(pc)
##                                if seq not in synchronising: #prevent repetition of synchronising paths 
                                synchronising.append(seq)
                                synchronisingP.append(pc)

##                                          synchronising.append(seq)
##                                          print(pc,"Synchronising path found")
                                break
                            else: #path not synchronising
                                #adding cycle twice   
                                pc=path+cycle+cycle
##                                print(pc)
                                flag=syncP(pc)
                                if flag==1:
                                    seq=color(pc)
##                                    if seq not in synchronising: 
                                    synchronising.append(seq)
                                    synchronisingP.append(pc)
##                                          synchronising.append(seq)
##                                          print(pc,"Synchronising path found")  
                                    break

                                    
    print("Synchronising paths for",r)
    for z in range(0,len(synchronising)):
         print(synchronising[z],"\n")
    print("shortest synchronising path",min(synchronising,key=len))


#checking whether the concatenated path+cycle is synchronising
def syncP(pc):
    fv=pc[len(pc)-1]
    synchronisingP=[]
    setseq=[]
    adj=[
     [0,0,0,0,0,0,0,0,0],
     [0,0,1,0,0,2,0,0,0],
     [0,0,0,1,0,0,0,0,2],
     [0,1,0,0,2,0,0,0,0],
     [0,2,0,0,0,0,0,1,0],
     [0,0,0,0,1,0,0,2,0],
     [0,0,1,2,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,2],
     [0,0,0,0,0,2,1,0,0]
     ]
    seq=color(pc)
    flag=1
    #checking whether all vertices (except r) following the same color sequence reach r
    for i in range(1,9): #origin vertex
      if i!=fv:
        v=i
        counter=0
        pathF=[]
        pathF.append(v)
        while counter<len(seq):
                      for m in range(1,9):#column number
                             if seq[counter]=='R':
                                if adj[v][m]==1:
                                  pathF.append(m)
                                  v=m
                                  counter+=1
                                  break
                             elif seq[counter]=='B':
                                if adj[v][m]==2:
                                  pathF.append(m)
                                  v=m
                                  counter+=1
                                  break
        if pathF[len(pathF)-1]!=fv:
            flag=0 #not asynchronising path
##            print(flag,"=>",pathF)
            break
##        else:
##            print(flag,"=>",pathF)
        synchronisingP.append(pathF)
##    if flag==1:
##        print(synchronisingP)
##        print(seq)
    return flag

#assign colors to the path from adj
def color(pc):
    adj=[
     [0,0,0,0,0,0,0,0,0],
     [0,0,1,0,0,2,0,0,0],
     [0,0,0,1,0,0,0,0,2],
     [0,1,0,0,2,0,0,0,0],
     [0,2,0,0,0,0,0,1,0],
     [0,0,0,0,1,0,0,2,0],
     [0,0,1,2,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,2],
     [0,0,0,0,0,2,1,0,0]
     ]
    seq=[]
    for m in range(0,len(pc)-1):
        v1=pc[m]
        v2=pc[m+1]
        if adj[int(v1)][int(v2)]==1:
            seq+='R'
        elif adj[int(v1)][int(v2)]==2:
            seq+='B'
    return seq
    

def main():
    print("Take input of AGW graph as adjacency matrix")
##    print("Tree Formation")
    gr=graph()
    for i in range(1,9):
        rootName=i
##        print("Printing root-leaf paths for tree",rootName)
        rootNode=treeFormation(rootName)
        r=rootNode
##        print("Tree Paths")
        l=rootNode.treePaths(rootNode)
        r.rtlpaths=l
##        print(r.rtlpaths)
        r.counter(r,r)  
        cycles(r,gr)
        paths(r,gr)
##    pprint.pprint(gr)
    for j in range(1,9):
        sP(j,gr)
		
if __name__=="__main__":
    main()
