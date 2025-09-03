def containsNearbyDuplicate(nums, k: int) -> bool:
    _k = {}
    for i, num in enumerate(nums):
        if num in _k and abs(_k[num] - i) <= k:
            return True
        _k[num] = i
    return False
    
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))