from random import randint

class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.value=None
        self.parent=None

class BinarySearchTree:
    def __init__(self):
        self.root=Node()

    def add(self,value):
        if self.root.value is None:   #проверяем есть ли корень
            self.root.value=value
            return
        self.add_data(self.root,value)

    def add_data(self,cn,value):               # cn текуший нод
        if cn.value>value:          #проверяем направо или налево идти
            if cn.left is None:
                cn.left=Node()
                cn.left.value=value
                cn.left.parent=cn
            else:
                self.add_data(cn.left,value)
        else:
            if cn.right is None:
                cn.right=Node()
                cn.right.value=value
                cn.right.parent=cn
            else:
                self.add_data(cn.right,value)
#-------- Поиск -------------------------------------
    def find(self,value):
        if self.root.value is None:
            return False
        if self.root.value==value:
            return True
        
        node=self.find_node(self.root,value)
        if node is None:
            return False
        return True

    def find_node(self,cn,value):
        if cn is None:
            return False
        if cn.value==value:
            return cn        
        if cn.value>value:
            res=self.find_node(cn.left,value)
            return res
        else:
            res=self.find_node(cn.right,value)
            return res
            

                
#-------- Удаление root ----------------------------------------            
    def delete(self,value):
        if (self.root.left is None and
            self.root.right is None and
            self.root.value==value):
            self.root.value=None
            return
    
        if (self.root.left is not None and
            self.root.right is None and
            self.root.value==value):
            self.root=self.root.left
            self.root.parent=None
            return
        
        if (self.root.left is None and
            self.root.right is not None and
            self.root.value==value):
            self.root=self.root.right
            self.root.parent=None
            return

        node=self.find_node(self.root,value)
        if node is None:
            raise Exception("Нет такого узла")
        self.delete_data(node)
#------- Удаление узла -------------------
    def delete_data(self,node):
        if (node.left is None and node.right is None):   # нет детей
            if node.parent.left==node:
                node.parent.left=None
            else:
                node.parent.right=None
            return
        if (node.left is not None and node.right is None):   # есть левый ребенок
            if node.parent.left==node:
                node.parent.left=node.left
            else:
                node.parent.right=node.left
            return
        if (node.left is None and node.right is not None):   # есть правый ребенок
            if node.parent.left==node:
                node.parent.left=node.right
            else:
                node.parent.right=node.right
            return
        if (node.left is not None and node.right is not None):   # два ребенка
            min_node_of_right=self.find_min_node(node.right)
            min_node_of_right.left=node.left

# ====================================================
#  ----------------- Здесь задание -------------------
            if node.parent==None:
                self.root=self.root.left
                self.root.parent=None
                return                
            else:
# ------------------ Конец задания -------------------
# ====================================================
                if node.parent.left==node:              
                    node.parent.left=min_node_of_right
                else:
                    node.parent.right=min_node_of_right
                return
        raise Exception("Не могу удалить узел")
# ----------- Поиск минмального элемента --------------
    def find_min(self):
        node=self.find_min_node(self.root)
        return node.value
    
    def find_min_node(self,cn):
        if cn.left is None:
            return cn
        node=self.find_min_node(cn.left)
        return node
                
#------ Обход дерева -------------------------------------
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.value)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
#====================================
n=10
hash_tel=[]
for i in range(n):
     hash_tel.append(randint(1,100))

hash_tel.sort()


print("\nОтсортированный список")   
print(hash_tel,"\n")

bst=BinarySearchTree()

for i in range(n):
     bst.add(hash_tel[i])

print("\nОбход дерева")     
print(bst.PreorderTraversal(bst.root))


print("\nКакой элемент нужно удалить?")
bst.delete(int(input()))


print("\nОбход дерева")     
print(bst.PreorderTraversal(bst.root))

