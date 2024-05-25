# this function is to find the internal nodes of the tree and 
# return them in a list

def inter_nodes(root,i_nodes):
    que = [root]
    while que:
        node = que.pop(0)
        if node.left or node.right:
            i_nodes.append(node)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    return i_nodes

# this is function is called from the build heap function.
# it will check for the nodes satifying the heap property and 
# tries to swap them with the parent if needed 
def heapify(start_node):
    large = start_node.data
    left = start_node.left
    right = start_node.right
    
    # if the node consists of bothe children
    if left and right:
        if left.data > right.data and left.data > large:
            temp = start_node.data
            start_node.data = start_node.left.data
            start_node.left.data = temp
            heapify(start_node.left)
            return
        elif right.data > left.data and right.data > large:
            temp = start_node.data
            start_node.data = start_node.right.data
            start_node.right.data = temp
            heapify(start_node.right)
            return
        else:
            return
    
    # if it has only eiether of the children
    if left:
        if left.data > large:
            temp = start_node.data
            start_node.data = start_node.left.data
            start_node.left.data = temp
            heapify(start_node.left)
            return
    if right:
        if right.data > large:
            temp = start_node.data
            start_node.data = start_node.right.data
            start_node.right.data = temp
            heapify(start_node.right)
            return

# this function will loop through the intrenal nodes in reverse order
def build_heap(i_nodes):
    for i in range(len(i_nodes)-1,-1,-1):
        heapify(i_nodes[i])
    return