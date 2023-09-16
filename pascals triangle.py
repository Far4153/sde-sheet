numRows=int(input())
def generate(numRows: int) :
        first_list=[1]
        result=[]
        finalarray=[first_list]

        for r in range(numRows-1):
            first_list=[0]+first_list
            first_list.append(0)
            # print(first_list)
            i=0
            j=i+1
            while(i!=len(first_list)-1):
                  
                  res=first_list[i]+first_list[j]
                #   print(res)

                  result.append(res)
                  
                  
                  i+=1
                  j=i+1

            first_list=result
            # print(first_list)

            finalarray.append(result)
            result=[]

        return finalarray

print(generate(numRows))
        

