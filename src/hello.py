
# Python3 program for the above approach
 
# Returns true if arr1[0..N-1] and
# arr2[0..M-1] contain same elements.
 
 

def is_arr_equal(arr1, arr2):



    if len(arr1) != len(arr2):

        return False
 


    count = {}



    for i in arr1:

        if i in count:

               

            count[i] += 1

        else:


            count[i] = 1
 



    for i in arr2:


        if i not in count or count[i] == 0:

            return False

        else:

                # If element is found, decrement

                # its value in the dictionary

            count[i] -= 1

   

    return True
 
 
# Driver Code

if __name__ == "__main__":
    n = int(input())

    arr1 = list(map(int,input().strip().split()))

    arr2 = list(map(int,input().strip().split()))
 

    if is_arr_equal(arr1, arr2):

        print('1')

    else:

        print("0")
 
