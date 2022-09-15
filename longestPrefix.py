strs = ["flower","flow","flight"]
output=[]
def long(strs):
    for item in strs:
        for index in range(len(item)):
            if item[index]==item[(index+1)]:
                output.append(item[index])
            return output

print(long(strs))

