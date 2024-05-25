class Item:
    def __init__(self,value,weight):
        self.value = value 
        self.weight = weight

def fractionalKnapscak(w,array,n):
    array.sort(key= lambda x: (x.value/x.weight))
    array.reverse()
    print(array[0].value,array[0].weight)
    print(array[1].value,array[1].weight)
    print(array[2].value,array[2].weight)

    currW = 0
    finalVal = 0.0

    for i in range(n):
        if (currW + array[i].weight)  <= w:
            finalVal += array[i].value
            currW+= array[i].weight 
        else: 
            remain = w - currW
            finalVal += (array[i].value * remain)/ array[i].weight 
            break 

    return finalVal



n =  5
w = 50 

array = []

i1 = Item(100,20)
i2 = Item(60,10)
i3 = Item(120,30)
array.append(i1)
array.append(i2)
array.append(i3)
print(array)
print(fractionalKnapscak(w,array,n))