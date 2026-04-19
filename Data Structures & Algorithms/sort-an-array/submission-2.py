class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # in-place merge sort
        # splitter -> give mid, left, right and recursive operation
        # combiner -> init 3 pointers(i,j,k -> L,0,0), pick lesser -> add, increment, fill in empty

        def mergeSort(array, left, right) : 
            if left >= right : 
                return
            
            mid = (left + right) // 2
            mergeSort(array, left, mid)
            mergeSort(array, mid + 1, right)
            merge(array, left, mid, right)
        
        def merge(array, left, mid, right) : 
            leftarray, rightarray = array[left : mid+1], array[mid+1 : right+1]
            i, j, k = left, 0, 0

            while j < len(leftarray) and k < len(rightarray) : 
                if leftarray[j] <= rightarray[k] : 
                    array[i] = leftarray[j]
                    j+=1
                else : 
                    array[i] = rightarray[k]
                    k+=1
                i+=1
            
            while j < len(leftarray) : 
                array[i] = leftarray[j]
                j+=1
                i+=1
            
            while k < len(rightarray) : 
                array[i] = rightarray[k] 
                k+=1
                i+=1
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums

