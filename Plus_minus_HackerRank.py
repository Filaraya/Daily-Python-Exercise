"""
Given an array of integers, calculate the ratios of its
elements that are positive, negative, and zero.
Print the decimal value of each fraction on a
new line 6 with  places after the decimal.
"""
def plusMinus(arr):
    """The ratios of its elements that are
    positive, negative, and zero."""
    arr_pos = []
    arr_neg = []
    arr_zero = []
    for i in arr:
        if i == 0:
            arr_zero.append(i)   
        elif i > 0:
            arr_pos.append(i)
        else:
            arr_neg.append(i)
    ratio_pos = len(arr_pos)/len(arr)#proportion of positive values
    ratio_neg = len(arr_neg)/len(arr)#proportion of negative values
    ratio_zero = len(arr_zero)/len(arr)#proportion of zero values
    
    pos = format(ratio_pos,'0.6f')
    neg = format(ratio_neg,'0.6f')
    zer = format(ratio_zero,'0.6f')
    print (pos)
    print (neg)
    print (zer)

if __name__ == '__main__':
    n = int(input("Enter the length of array: ").strip())

    arr = list(map(int, input("Please, the values of arraya using space: ").rstrip().split()))
    print("The ratios of positive, negative and zero values in the array are:")
    plusMinus(arr)
