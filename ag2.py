#Determining all cycles

 count=[0]*8
 for i in range(1,2):
    print("For i=%d" %i)
    stack=[] #python equivalent here
    #determine the first straight path
    currNode=r #receive root from main
    path=currNode.cnode
    index=currNode
    while(len(set(path)==len(path)) #there is no repetition in the path isRep(path)):
          stack=push(stack,1)
          children=currNode.getchildren(currNode)
          currNode=children[0] #make currNode, first child to the left
          path.append(currNode.cnode)  #adding on to the path
          index.append(currNode)
          #if the current node is a leaf node =>jump to the node with same value parent node
          if currNode.isleaf():
                #refer to the dictionary here
                for key in r.d:
                    if key==currNode.cnode:
                          list1=r.d[key]
                          l=len(list1)
                          for i in l:
                              if not list1[i].isleaf(): 
                                  currNode=list1[i]
                                  break







    if path[0]==path[length(path)-1]:
          print(path)
          count[i]=count[i]+1

    #determining remaining paths
    while True:
          while stack[l]==2:
              stack.pop()
              path.pop()
              index.pop()
          if len(stack[0]):
             break

          val=stack.pop()
          stack=push(stack,val+1)
          #if the current node is a leaf node =>jump to the node with same value parent node
          i=index[len(index)-2]
            print(i)
          if i.isleaf():
                #refer to the dictionary here
                for key in r.d:
                    if key==i.cnode:
                          list1=r.d[key]
                          l=len(list1)
                          print(list1[i].isleaf())
                          for i in range(0,l):
                              if not list1[i].isleaf(): 
                                  temp2=list1[i]
                                  break
          else:
             temp2=index[len(index)-2]

          temp=temp2.getchildren()
          path[length(path)-1]=temp[val+2].get() 
          index[length(index)-1]=temp[val+2]
          currNode=temp[val+2]
                       
          while(len(set(path))==len(path)): #there is no repetition in the path isRep(path)):
               flag=0
               if currNode.isleaf():
                    #refer to the dictionary here
                for key in r.d:
                    if key==i.cnode:
                          list1=r.d[key]
                          l=len(list1)
                          for i in l:
                              if not list1[i].isleaf(): 
                                  temp2=list1[i]
                                    flag=1
                                  break
                      if flag==1:
                         break

               
                stack=push(stack,1)
                l=currNode.getchildren()
                currNode=l[1]
                path.append(currNode.cnode) #adding on to the path
                index.append(currNode)
                



##        #if obtained path is required solution B        
          if path[0]==path[len(path)-1]:
             print(path)
             count[i]+=1


 #Determine no loop paths from node 1->2,3,...n & 2->1,3,4,..n & 3->1,2,4,.. n-1
 for i in range(1,2):
        for j in range(1,9):
                if i!=j:
                   print('For i=%d to j=%d',%(i,j))
                   stack=[] #python equivalent here
                   path=[]
                   index=[]
                   #determine the first straight path C
                   currNode=r
                   path.append(currNode.cnode)
                   index.append(currNode)
                   while(len(set(path))==len(path) and path[len(path)-1]!=j: #there is no repetition in the path isRep(path)):
                        stack=push(stack,1)
                        l=currNode.getchildren()
                        currNode=l[0]
                        path.append(currNode.cnode) #adding on to the path
                        index.append(currNode)
                        if currNode.isleaf():
                                flag=0
                                #refer to the dictionary here
                                for key in r.d:
                                    if key==currNode.cnode:
                                          list1=r.d[key]
                                          l=len(list1)
                                          for i in (0,l):
                                              if not list1[i].isleaf(): 
                                                  currNode=list1[i]
                                                  flag=1
                                                  break
                                    if flag==1:
                                        break

                        if path[len(path)-1]==j:
                             print("path from",i,j,path)

                #Determining remaining paths
                while True:
                     ## print("#6")
                     while stack[len(stack)-1]==2:
##                               print("#8")
                                 stack.pop()
                                 path.pop()
                                 index.pop()
          
                                 if len(stack)==0:
                                     flag1=1   
                                     break

                                 if flag1==1:
                                     break

                     val=pop(stack)
                     stack=push(stack,val+1)
                     #if the current node is a leaf node =>jump to the node with same value parent node
                     ob=index[length(index)-2]
                     if currNode.isleaf():
                                flag=0
                                #refer to the dictionary here
                                for key in r.d:
                                    if key==currNode.cnode:
                                          list1=r.d[key]
                                          l=len(list1)
                                          for i in (0,l):
                                              if not list1[i].isleaf(): 
                                                  currNode=list1[i]
                                                  flag=1
                                                  break
                                    if flag==1:
                                        break

                     else:
                         temp2=ob

                     temp=temp2.getchildren()
                     path[length(path)-1]=temp[val].cnode
                     index[length(index)-1]=temp[val]
                     currNode=temp[val]
                       
                     while len(set(path))==len(path) and path[len(path)-1]!=j:: #there is no repetition in the path isRep(path) && path(length(path))!=j):
          
                        if  currNode.isleaf():
                            #refer to the dictionary here
                                for key in r.d:
                                    if key==currNode.cnode:
                                          temp=r.d[key]
                                          l=len(temp)
                                          for i in l:
                                              if not temp[i].isleaf(): 
                                                  temp2=temp[i]
                                                  break
                        l=currNode.getchildren()
                        currNode=currNode[0]
                        path.append(currNode.cnode) #adding on to the path
                        index.append(currNode)
                

                     if path[len(path)-1]==j:
                          print("path from",i,j,path)










                           
                
