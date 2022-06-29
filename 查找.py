## 顺序查找
# def linear_search(li, val):
#     for ind, v in enumerate(li): #枚举li中的index与值
#         if v == val:
#             print(ind)
#         else:
#             # return None
#             print("result is not found")
#     pass
#
#
# for i, j in enumerate([1, 2, 1, 5, 1]):
#     print(i, j)
#
# linear_search([1, 2, 3, 5, 6, 8], 4)
# linear_search([1, 2, 3, 5, 6, 8], 5)


# # 折半查找,binary_search
# def binary_search(li, val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if li[mid] == val:
#             print(mid)
#             return mid
#         elif li[mid] < val:
#             left = mid + 1
#             pass
#         elif li[mid] > val:
#             right = mid - 1
#             pass
#         else:
#             print('result is not found')
#             pass
#     else:
#         return None
#
#
# binary_search([1, 3, 8, 41, 56, 98, 555, 1000], 555)

