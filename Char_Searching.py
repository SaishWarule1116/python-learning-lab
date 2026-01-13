# Given a string s and a list of characters q,# this code pre-stores the frequency of each character in s
# and then searches for the frequency of each character in q using the pre-stored data.
s = "azyxcyyzaaaaa"
q = ["x", "y", "z", "a", "b", "c"]

# Prestore the frequency of each character in the string s
def char_prestore(s):
    prestore={}
    for char in s:
        index = ord(char)-97
        prestore[index] = prestore.get(index,0)+1
    return prestore 

# Function to search for characters in the prestore dictionary
def char_searching(q,prestore):
    result = {}
    for char in q:
        index = ord(char)-97
        result[char] = prestore.get(index,0)
    return result

prestore = char_prestore(s)
result = char_searching(q,prestore)
print(result)