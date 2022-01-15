
"""
minimum swaps method 1
Swap to correct place, repeating current index
[4, 3, 5, 2, 1] 4 and 2
[2, 3, 5, 4, 1] 2 and 3
[3, 2, 5, 4, 1] 3 and 5
[5, 2, 3, 4, 1] 5 and 1
[1, 2, 3, 4, 5] 1 good
[1, 2, 3, 4, 5] 2 good
[1, 2, 3, 4, 5] 3 good
[1, 2, 3, 4, 5] 4 good
[1, 2, 3, 4, 5] 5 good

minimum swaps method 2
Swap with correct value, no repeating
[4, 3, 5, 2, 1] 4 and 1
[1, 3, 5, 2, 4] 3 and 2
[1, 2, 5, 3, 4] 5 and 3
[1, 2, 3, 5, 4] 5 and 4
[1, 2, 3, 4, 5] 5 good
"""

def main():
    arr = [4, 3, 5, 2, 1]
    assert 4 == minimumSwaps_meth1(arr)
    arr = [4, 3, 5, 2, 1]
    assert 4 == minimumSwaps_meth2(arr)
    arr = [4, 3, 5, 2, 1]
    assert 4 == minimumSwaps_meth2_v2(arr)

def minimumSwaps_meth1(arr):
    print("Method 1:")
    """
    int minimumSwaps(vector<int> arr) {
    
    int i,c=0,n=arr.size();
    for(i=0;i<n;i++)
    {
        if(arr[i]==(i+1))
            continue;
        
        swap(arr[i],arr[arr[i]-1]);
        c++;
        i--;
    }
    return c;

    }
    """
    c = 0
    i = 0
    iter = 0
    while i < len(arr):
        iter += 1
        print(arr, end=" ")
        if(arr[i] != i+1):
            print(f"swapping {arr[i]} and {arr[arr[i]-1]}")
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
            c += 1
            i -= 1
        else:
            print(f"{arr[i]} good")
        i += 1
    print(f"{c} swaps with {iter} iterations")
    return c


def minimumSwaps_meth2(arr):
    print("Method 2")
    ref_arr = sorted(arr)
    index_dict = {v: i for i,v in enumerate(arr)}
    swaps = 0
    iter = 0
    
    for i,v in enumerate(arr):
        iter += 1
        correct_value = ref_arr[i]
        print(arr, end=" ")
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            print(f"swapping {arr[i]} and {arr[to_swap_ix]}")
            arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix]
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1
        else:
            print(f"{arr[i]} good")
    print(f"{swaps} swaps with {iter} iterations")
    return swaps

def minimumSwaps_meth2_v2(arr):
    sa = sorted(arr)
    idxs = {v: i for i,v in enumerate(arr)}
    c = 0
    
    for i,v in enumerate(arr):
        corr_val = sa[i]
        if v != corr_val:
            swp_idx = idxs[corr_val]
            swap(arr, i, swp_idx)
            idxs[v] = swp_idx
            idxs[corr_val] = i
            c += 1
    return c

def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

if __name__ == "__main__":
    main()