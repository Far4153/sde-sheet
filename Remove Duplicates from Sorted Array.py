nums=[1,1,1,2,2]

def removeDuplicates(arr) -> int:
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    k = len(st)
    j = 0
    for x in st:
        arr[j] = x
        j += 1
    return k

         
