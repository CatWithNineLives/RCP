from bt import *
from collections import defaultdict
import pprint

def treeFormation(rootName):

 
    adj=[ 
     [0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,3,0,2,0,0,0,1,0,0,0,0],
     [0,1,0,2,0,3,0,0,0,0,0,0,0],
     [0,0,3,0,1,0,2,0,0,0,0,0,0],
     [0,0,0,1,0,0,0,3,0,0,0,0,2],
     [0,0,1,0,0,0,1,0,0,3,0,0,0],
     [0,0,0,1,0,3,0,2,0,0,0,0,0],
     [0,0,0,0,2,0,1,0,0,0,0,0,3],
     [0,1,0,0,0,0,0,0,0,2,3,0,0],
     [0,0,0,0,0,1,0,0,3,0,0,2,0],
     [0,1,0,0,0,0,0,0,2,0,0,3,0],
     [0,0,0,0,0,0,0,0,0,1,3,0,2],
     [0,0,0,0,0,1,0,0,0,0,3,2,0],
     ]


 #Formation of trees
    currNode=treeNode(rootName,None)
    r=currNode
    r.tree(currNode)
    r.rv=rootName
    flag=[0]*13
    counter=0
    while(sum(flag)!=36):
        counter+=1
        cn=currNode.get()
        if flag[cn]<3:

            for j in range(1,13):
                if adj[cn][j]==flag[cn]+1:
                   flag[cn]+=1

                   if flag[j]==0:
                      child=treeNode(j,currNode)
                      currNode.addnode(child)
                      temp=currNode.getchildren()
                      print("children",temp,"of",cn,currNode)
                      currNode=temp[len(temp)-1]    
                      
                   else :
                      child=treeNode(j,currNode)
                      currNode.addnode(child)
                   break
        else:
            currNode=currNode.getparent() #returns the parent object,
    return r #returns the root

def cycles(r,gr):
    count=[0]*13
    path=[]
    index=[]
    stack=[]
    i=r.cnode
    #determine the first straight path
    currNode=r #receive root from main
    path.append(currNode.cnode)
    index.append(currNode)
    while(len(set(path))==len(path)): #there is no repetition in the path isRep(path)):
          stack=push(stack,1)
          ch=[]
          ch=currNode.getchildren()
          currNode=ch[0] #make currNode, first child to the left
          path.append(currNode.cnode)  #adding on to the path
          index.append(currNode)
          if currNode.isleaf():
            currNode=skipNode(r,currNode)



    if path[0]==path[len(path)-1]:
          count[i]=count[i]+1
          j=r.cnode
          cp(r,gr,j,path)
          
    #determining remaining paths
    flag1=0
    while True:
          while stack[len(stack)-1]==3:
              stack.pop()
              path.pop()
              index.pop()
          
              if len(stack)==0:
                 flag1=1   
                 break
          if flag1==1:
              break
          val=stack.pop()
          stack=push(stack,val+1)
          #if the current node is a leaf node =>jump to the node with same value parent node
          ob=index[len(index)-2]
          
          if ob.isleaf():
                ob=skipNode(r,ob)

          temp=ob.getchildren()
          path[len(path)-1]=temp[val].get() 
          index[len(index)-1]=temp[val]
          currNode=temp[val]
          while(len(set(path))==len(path)): #there is no repetition in the path isRep(path)):
               if currNode.isleaf():
                  currNode=skipNode(r,currNode)
               
               stack=push(stack,1)
               l=currNode.getchildren()
               currNode=l[0]
               path.append(currNode.cnode) #adding on to the path
               index.append(currNode)


##        #if obtained path is required solution B        
          if path[0]==path[len(path)-1]:
             count[i]+=1
             j=r.cnode
             cp(r,gr,j,path)
             
          
 #Determine no loop paths from node 1->2,3,...n & 2->1,3,4,..n & 3->1,2,4,.. n-1
## for i in range(1,2):
def paths(r,gr): 
 for j in range(1,13):
                if r.cnode!=j:
                   stack=[] #python equivalent here
                   path=[]
                   index=[]
                   currNode=r
                   #determine the first straight path C
                   path.append(currNode.cnode)
                   index.append(currNode)
                   while(len(set(path))==len(path) and path[len(path)-1]!=j): #there is no repetition in the path isRep(path)):
                        stack=push(stack,1)
                        ch=currNode.getchildren()
                        currNode=ch[0]
                        path.append(currNode.cnode) #adding on to the path
                        index.append(currNode)
                        if currNode.isleaf():
                            currNode=skipNode(r,currNode)

                   if path[len(path)-1]==j:
                             cp(r,gr,j,path)

                   #Determining remaining paths
                   while True:
                     flag1=0
                     while stack[len(stack)-1]==3:
                                 stack.pop()
                                 path.pop()
                                 index.pop()
          
                                 if len(stack)==0:
                                     flag1=1   
                                     break

                     if flag1==1:
                         break

                     val=stack.pop()
                     stack=push(stack,val+1)
                     #if the current node is a leaf node =>jump to the node with same value parent node
                     ob=index[len(index)-2]
                     if ob.isleaf():
                         ob=skipNode(r,ob)

                     temp=ob.getchildren()
                     path[len(path)-1]=temp[val].cnode
                     index[len(index)-1]=temp[val]
                     currNode=temp[val]
                       
                     while len(set(path))==len(path) and path[len(path)-1]!=j: #there is no repetition in the path isRep(path) && path(length(path))!=j):
          
                        if currNode.isleaf():
                                currNode=skipNode(r,currNode)
                        stack=push(stack,1)        
                        ch=[]
                        ch=currNode.getchildren()
                        currNode=ch[0]
                        path.append(currNode.cnode) #adding on to the path
                        index.append(currNode)
                

                     if path[len(path)-1]==j:
                          cp(r,gr,j,path)
def graph():
    gr=defaultdict(list)
    for key in range(1,13):
        gr[key]={}
        for k in range(1,13):
            gr[key][k]=[]
    return gr

def cp(r,gr,j,path):
    flag=0
    for key in gr:
        if key==r.cnode:
            for k in gr[key]:
                if k==j:
                    gr[key][k].append(path.copy())
                    flag=1
                    break
            if flag==1:
                break


def skipNode(r,Node):#function to skip to same value parent node
    flag=0
    for key in r.d:
        if key==Node.cnode:
            list1=r.d[key]
            l=len(list1)
            for i in (0,l):
              if not list1[i].isleaf(): 
                Node=list1[i]
                flag=1
                break
        if flag==1:
            break
    return Node                                  
                        
                                          
                                    
def push(stack,k):
    stack.append(k)
    return stack


    

    
