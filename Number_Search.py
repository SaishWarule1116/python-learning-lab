nums = [5,3,6,7,4,5,7,8,2,1,0,9]
quires = [5,7,0,10,3,2]
prestore = {}
result = {}
# Prestore the frequency of each number in the list nums
def prestore_numbers(nums):
    
    for num in nums:
        if num in prestore:
            prestore[num]+=1
        else:
            prestore[num]=1
    return prestore

# Function to search for numbers in the prestore dictionary
def search_numbers(quires, prestore):
   
    for num in quires:
        if num<1 or num>10:
            result[num] = 0
        else:
            result[num] = prestore.get(num,0)
    return result

# Calling the functions and printing the result
prestore = prestore_numbers(nums)
result = search_numbers(quires, prestore)
print(f"Result: {result}")

# Used items() to print the result in a formatted way
for k,v in result.items():
    print(f"Number {k} occurs {v} times.")

# Keys()
print(f"Keys in prestore: {list(prestore.keys())}")
# Values()
print(f"Values in prestore: {list(prestore.values())}")
