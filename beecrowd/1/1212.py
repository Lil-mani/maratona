def count_carry(a, b):
 
    # Initialize the value of 
    # carry to 0 
    carry = 0; 
 
    # Counts the number of carry
    # operations 
    count = 0; 
 
    # Initialize len_a and len_b
    # with the sizes of strings 
    len_a = len(a);
    len_b = len(b); 
 
    while (len_a != 0 or len_b != 0):
 
        # Assigning the ascii value
        # of the character 
        x = 0;
        y = 0; 
        if (len_a > 0): 
            x = int(a[len_a - 1]) + int('0'); 
            len_a -= 1; 
         
        if (len_b > 0):
            y = int(b[len_b - 1]) + int('0'); 
            len_b -= 1; 
 
        # Add both numbers/digits 
        sum = x + y + carry; 
 
        # If sum > 0, increment count 
        # and set carry to 1 
        if (sum >= 10):
            carry = 1; 
            count += 1; 
 
        # Else, set carry to 0 
        else:
            carry = 0; 
 
    return count; 
res = []
while True:
    try:
        v1,v2 = input().split()
        if v1 == "0" and v2 == "0":
            break
        carryCounter = count_carry(v1,v2)
        if carryCounter == 0:
            res.append("No carry operation.")
        elif carryCounter == 1:
            res.append("1 carry operation.")
        else:
            res.append(str(carryCounter)+" carry operations.")

    
    except EOFError:
        break

for i in res:
    print(i)