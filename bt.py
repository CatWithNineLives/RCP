 
    


class treeNode:


    def __init__(self,currNode,parent):
        self.left=None
        self.middle=None
        self.right=None
        self.parent=parent
        self.cnode=currNode
        self.rv=None

    def tree(self,rootNode):
        self.root=rootNode
        self.rtlpaths=None
        self.d={}
           #Forming dictionary with keys
        for key in range(1,13):
            self.d.setdefault(key,[])
            
    def get(self):
        return self.cnode
        
    def addnode(self,child):

        if self.left is None:
            self.left=child
            val=child.cnode
        elif self.middle is None:
            self.middle=child
            val=child.cnode
        
        elif self.right is None:
            self.right=child
            val=child.cnode

    def getchildren(self):
        
        children=[]
        childrenVal=[]
        if self.left is not None:
            child=self.left
            val=child.cnode
            children.append(child)
            childrenVal.append(val)
        if self.middle is not None:
            child=self.middle
            val=child.cnode
            children.append(child)
            childrenVal.append(val)
        if self.right is not None:
            child=self.right
            val=child.cnode
            children.append(child)
            childrenVal.append(val)
       
        return children

    def getparent(self):
        return self.parent

    def isleaf(self):
        if self.left is None and self.middle is None and self.right is None:
            return True
        else:
            return False

    def treePaths(self,root):
        if root is None: 
            return []
        if root.left is None and root.middle is None and root.right is None:
            return [str(root.cnode)]

        # subtree is always a list, though it might be empty 
        left_subtree   = self.treePaths(root.left)  
        middle_subtree = self.treePaths(root.middle)
        right_subtree  = self.treePaths(root.right)
        full_subtree   = left_subtree + middle_subtree + right_subtree  # the last part of comprehension

        list1 = []
        for leaf in full_subtree:  # middle part of the comprehension
            list1.append(str(root.cnode) + '->'+ leaf)  # the left part 
        return list1


    def counter(self,currNode,root):
        root.dictionary(currNode)
        children=currNode.getchildren()
        if not children:
            return
        l=0

        while l<3:
            
            currNode=children[l]
            currNode.counter(currNode,root)
            l+=1    
                
    def dictionary(self,currNode):
        
        #Insert currNode's value into dict
        for key in self.d:
            if key==currNode.cnode:
                self.d[key].append(currNode)
                return

    





##        keep following color one
##
##            if there is a repetition:
##                if root is repeated:
##                    close cycle, leave
##                if not root is repeated:
##                    replace color one with two goto parent
##        
                

  

















        
