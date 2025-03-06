def is_prime(num_To_Check):
    i=2
    bool_value=False
    while i<int(num_To_Check/2)+1:
        if num_To_Check%i==0:
            bool_value=True
            break
        else:
            bool_value=False
        i+=1
    return bool_value

result_Prime=is_prime(7)

if result_Prime==True:
    print("Not a Prime Number")
else:
    print("Prime Number")
