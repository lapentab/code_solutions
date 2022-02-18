#My solutions for https://leetcode.com/contest/biweekly-contest-71/


#https://leetcode.com/contest/biweekly-contest-71/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
def minimumOperations(nums): 
        arr= []
        for items in str(nums):
            arr.append((items))
        arr= sorted(arr)
        print( str(arr))
        num1=int("".join(arr[::2]))
        num2=int("".join(arr[1::2]))
        print(str(num1))
        print(str(num2))
        return num1+num2
    
    
#https://leetcode.com/contest/biweekly-contest-71/problems/partition-array-according-to-given-pivot/
# Memory usage beats 98% of python submissions
# Runtime beats 87% of python submissions
nums = [9,12,5,10,14,3,10]
pivot = 10
def pivotArray(nums, pivot):
   return [i for i in nums if i < pivot] + [i for i in nums if i==pivot] + [i for i in nums if i>pivot]

# https://leetcode.com/contest/biweekly-contest-71/problems/minimum-cost-to-set-cooking-time/
# Runtime beats 95% of python submissions              
def minCostSetTime(startAt, moveCost, pushCost, targetSeconds):  
    minute = targetSeconds//60
    seconds = targetSeconds%60
    modMin = minute-1
    modSec = seconds + 60
    secCost=0
    minCost=0
    modCost=0
    def getCost(s):
        cost = len(s)*pushCost
        s= str(startAt) + s
        cost+=sum([0 if s[i] == s[i+1] else 1 for i in range(0, len(s)-1)])*moveCost
        return cost
    print('minute ' + str(minute) + ' seconds ' + str(seconds) + " modmin " + str(modMin) + ' modSec ' + str(modSec))
    if modSec > 99 or modMin < 0:
        modCost = None
    else:
        modString = str(modMin) + str(modSec)
        modCost = getCost(modString)
        print("MS %s" % modString)
        
    if targetSeconds > 99:
        secCost = None
    else:
        secString = str(targetSeconds)
        secCost= getCost(secString)
        print ("SS %s" % secString)
    if minute>99:
        minCost = None
    else:
        minString = (str(minute) + "%02d" % seconds).lstrip('0')
        print(minString)
        minCost = getCost(minString)
    return min([items for items in [secCost, minCost, modCost] if items !=None])
    
