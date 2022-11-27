def quicksort(List):
    if(len(List)<=1):
        return List
    center=len(List)//2
    list1=list([i for i in List if i<List[center]])
    list2=list([i for i in List if i==List[center]])
    list3=list([i for i in List if i>List[center]])
    l1=quicksort(list1)
    l3=quicksort(list3)
    return l1+list2+l3
print(quicksort([1,1,2,12,13,15,2,8,9,1,11,25,105,242,241,12,16]))
