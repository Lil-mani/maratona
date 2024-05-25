"""
 InOrder traversal -> printo se passei pelo menos duas vezes
 PreOrder traversal  -> cheguei printei 
 PostOrder traversal -> printo os filhos primeiro (isso considerando que fui até as folhas)
 LevelOrder traversal 

 complexidade de tempo -> O(N)
 complexidade de espaço -> O(1) não considerando o tamanho da memoria stack 
 se for considerar o tamanho da memoria stack O(log n) onde log n vai representar o tamanho da tree


 folhas -> Node.left == None or Node.right == None


"""

# Classe representa um Node individualmente 
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def Preorder(root):
    if root is None:
        return

    print(root.val,end=" ")
    Preorder(root.left)
    Preorder(root.right)

def InOrder(root):
    if root is None:
        return
    InOrder(root.left)
    print(root.val,end=" ")
    InOrder(root.right)
        
def PostOrder(root):
    if root is None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.val,end=" ")

def FindDepth(root):
    if root is None:
        return 0
    # Chegamos em uma folha 
    if root.left == None and root.right == None:
        return 1

    # Se não consigo ir para o lado esquerdo, sigo o lado direito 
    if root.left is None:
       return 1 + FindDepth(root.right)
    
    # Se eu não consigo ir para o lado direito, sigo para o lado esquerdo
    if root.right is None:
        return 1 + FindDepth(root.left)

    return  1 + min(FindDepth(root.left),FindDepth(root.right))
    

def sumTree(root):
    if root == None:
        return 0
    
    s = root.val

    s+= sumTree(root.left)
    s+= sumTree(root.right)

    return s

def sumLeafTree(root,s=0):
    if root != None:
        s= s*0 + root.val
        if result:= sumLeafTree(root.left) + sumLeafTree(root.right):
            return result
        
        return s
    
    return 0

  



#       1
#      / \
#     2   3
#    / \ /
#   4  5 10

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(10)

print(sumTree(root))
print(sumLeafTree(root))
# print("PreOrder: ")
# Preorder(root)
# print("\nInOrder: ")
# InOrder(root)
# print("\nPostOrder: ")
# PostOrder(root)

# n = FindDepth(root)
# print("\n Tamanho",n)