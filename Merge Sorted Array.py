m=int(input())
n=int(input())
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))


def merge(nums1,nums2,m,n):
    for i in range(m,len(nums1)):
        nums1[i]=nums2[i-m]

    nums1.sort()

    print(nums1)



merge(nums1,nums2,m,n)
