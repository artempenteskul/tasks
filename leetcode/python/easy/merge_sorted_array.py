# task number - 88


from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    last = n + m - 1

    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1

        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1

    # algo should be in-place nums1 sequence
    print(nums1)


if __name__ == '__main__':
    merge(nums1=[2, 2, 3, 0, 0, 0], m=3, nums2=[1, 5, 6], n=3)  # [1, 2, 2, 3, 5, 6]
    merge(nums1=[1], m=1, nums2=[], n=0)  # [1]
    merge(nums1=[0], m=0, nums2=[1], n=1)  # [1]
