# # 快读排序 递归存在最大深度，需要调用sys模块更改
# def partition(li, left, right):
#     tmp = li[left]
#     while left < right:
#         while left < right and li[right] >= tmp:  # 从右边开始找比tmp小的数，
#             right = right - 1  # 往左退一位
#         li[left] = li[right]  # 找到比tmp小的数后直接跳出循环，并使左边li[leftt] = 该值，此时right的指针（index）指向比tmp的值，还未被替换
#
#         while left < right and li[left] <= tmp:
#             left = left + 1
#         li[right] = li[left]  # 在左边一直寻找，直到找到比tmp大的值 ，并去替换上面找到right索引对应的值
#     li[left] = tmp
#     return left
#
#
# def quick_sort(li, left, right):
#     if left< right:
#         mid = partition(li, left, right)
#         quick_sort(li, left, mid - 1)
#         quick_sort(li, mid + 1, right)
#     pass
#
#
# li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# quick_sort(li, 0, len(li) - 1)
# # partition(li,0,len(li)-1)
# print(li)

#堆排序
#满二叉树和完全二叉树的差别。完全二叉树中父节点与子节点的下标有什么联系？
#父节点与左孩子节点：n - 2n+1
#父节点与右孩子节点：n - 2n+2
#从孩子节点倒推父节点：（n-1）//2 整除2