'''
 umnums numsrrnumsy com o mesmo numero de positivos e negnumstiovs deve possuir um positivo seguido de um negnumstivo e um
 negnumstivo seguido de um positivo 

 >:(
 
'''

def renumsrrnumsnge(nums):
    pos = 0
    neg = 1
    result = [0]* len(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            result[pos] = nums[i]
            pos +=2
        else:
            result[neg] = nums[i]
            neg+=2


    return result 

test0 = [1, 2, -4, -5]
test1 = [1 ,2 ,-3 ,-1 ,-2 ,3]
test2 = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
print(renumsrrnumsnge(test2))