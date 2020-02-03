def top_n(items, n):
    """return the top n in an array, descending order.
    args:
    items(array): list or array-type object containing numerical values
    n (int): number of top items to return

    return:
    array: top n items, in descending order

    examples:
    >>>top_n([8,3,2,7,4],3)[8,7,3]"""

for i in range(n)
    for j in range(len(items)-1,i):

        if items[j] > items[j+1]:
            items[j], items[j+1] = items[j+1], items[j]

top_n = items[-n:]

return top_n[::-1]
