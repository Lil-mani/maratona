# Considering the code only for the MAX HEAP anyways
# for MIN HEAP you just need to check for the min node in heapify function

def insert_node(arr,new_data):
    arr.append(new_data)
    n = len(arr)
    
    # one node tree is always a heap
    if n>1:
        #traversing the internal nodes in reverse
        for i in  range(n//2 -1 ,-1, -1): 
            heapify(arr,i,n)
    # print(f"Max heap after inserting {new_data} :",arr)

def heapify(arr,ind,n):
    largest = ind

    # checking if there are left and right nodes 
    left = ind*2 + 1 if (ind*2 + 1)<n else 0 
    right = ind*2 + 2 if (ind*2 + 2)<n else 0
    
    # finding the largest from the parent and the child nodes
    if left and left <=n and arr[largest]<arr[left]:
        largest = left
    if right and right <=n and arr[largest]<arr[right]:
        largest = right
    
    # swap the elements if got found a largest value than the parent
    if ind != largest:
        temp = arr[ind]
        arr[ind] = arr[largest]
        arr[largest] = temp
        heapify(arr,largest,n)
        
arr = []

# inserting the nodes into the tree which is in array representation

insert_node(arr,22)
insert_node(arr,15)
insert_node(arr,7)
insert_node(arr,2)
insert_node(arr,1)
indGe = 3
res = 0
taken_amount = 0
for i in range(indGe):
    if len(arr) == 0:
        taken_amount = 0
        break
    root = arr.pop(0)
    taken_amount = sum(int(digito) for digito in str(root))
    new_root = root - taken_amount
    if new_root == 0:
        continue
    else:
        insert_node(arr,new_root)
print(taken_amount)
