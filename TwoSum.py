nums=[2,7,11,15,3,6]
target=9

def solution(numbers):
    output=[]
    def make_pairs(val):
        combination=[]
        for i in range(len(val)-1):
            for j in range(i+1,len(val)):
                combination.append((i,j))
        return combination

    for a,b in make_pairs(nums):
        if nums[a]+nums[b]==target:
            output.append([a,b])
    return output
    
print(solution(nums))
    
