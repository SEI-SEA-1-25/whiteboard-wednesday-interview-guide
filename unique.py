def order(arr):
    list = []
  
    for i in range(len(arr)):
        if(arr[i] == arr[i - 1]): 
           i += 1
        else:
            list.append(arr[i])


    return print(list)
 
