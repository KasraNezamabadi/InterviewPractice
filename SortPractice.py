import math


def MergeSort(inputList: [int]):
    # Stop condition for recursive call
    if len(inputList) == 1:
        return inputList

    # We need to divide the array into two halves and recursively call mergeSort for each.

    leftSublist = inputList[:math.floor(len(inputList) / 2)]
    rightSublist = inputList[math.floor(len(inputList) / 2):]
    sortedLeftSubarray = MergeSort(leftSublist)
    sortedRightSubarray = MergeSort(rightSublist)
    finalResult = Merge(sortedLeftSubarray, sortedRightSubarray)
    v = 9
    return finalResult


def Merge(listA: [int], listB: [int]):
    # Merge two sorted arrays and return the result

    indexA = 0  # index for listA
    indexB = 0  # index for listB

    mergedArray = []

    lower_bound = len(listA)
    if len(listB) < len(listA):
        lower_bound = len(listB)

    while indexA < lower_bound and indexB < lower_bound:
        itemA = listA[indexA]
        itemB = listB[indexB]

        if itemA > itemB:
            mergedArray.append(itemB)
            indexB = indexB + 1
        else:
            mergedArray.append(itemA)
            indexA = indexA + 1

    if indexA < len(listA):
        mergedArray.extend(listA[indexA:])

    if indexB < len(listB):
        mergedArray.extend(listB[indexB:])

    v = 9

    return mergedArray


def quick_sort(input_list: [int], low, high):
    if low < high:

        pivot_index = partition(input_list, low, high)

        quick_sort(input_list, low, pivot_index - 1)
        quick_sort(input_list, pivot_index + 1, high)


def partition(input_list: [int], low, high):

    pivot = input_list[high]  # last element as pivot
    index_before_pivot = low-1

    for i in range(low, high):

        if input_list[i] <= pivot:

            index_before_pivot = index_before_pivot + 1
            input_list[i], input_list[index_before_pivot] = input_list[index_before_pivot], input_list[i]

    pivot_index = index_before_pivot + 1
    input_list[pivot_index], input_list[high] = input_list[high], input_list[pivot_index]

    return pivot_index


inputList = [1, 4, 2, 7, 8, 5, 3]

#print(inputList[-1])

quick_sort(input_list=inputList, low=0, high=len(inputList)-1)

print('Result: ', inputList)

#print(Merge([7, 8], [3, 5]))
#print(MergeSort(inputList=inputList))





