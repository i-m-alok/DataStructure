#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    # code here
    queue=[]
    result=[]
    for i in range(N+1):
        if(i>=K):
            if(len(queue)):
                result.append(queue[0])
                if(queue[0]==A[i-K]):
                    queue.pop(0)
            else:
                result.append(0)
        if(i<N and A[i]<0):
            queue.append(A[i])
    return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends