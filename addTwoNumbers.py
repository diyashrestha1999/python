l1=[5,4,3]
l2=[5,6,4]

def addTwoNumber(val1,val2):
    output=[]
    temp=[]
    for i in range(len(val1)):
        for j in range(len(val2)):
            output.append(val1[i]+val2[j])
        return output
    def remainder(output):
        for index in output:
            if index>0:
                temp.append(index)
        return temp
    remainder(output)

print(addTwoNumber(l1,l2))

        


            


