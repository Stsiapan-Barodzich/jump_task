def solution(nums: list)-> bool:

    max_jump_element = 0
    for i, jump in enumerate(nums):
        if max_jump_element < i: # Если мы не можем допрыгнуть до i-ого элемента
            return False
        max_jump_element = max(max_jump_element, jump + i) # Ищем максимальный элемент до которого можем допрыгнуть
    return True


nums = list(map(int, input().split()))
print(solution(nums))
