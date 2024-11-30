import math as m
def MinMax(depth,currIndex,isMax,score,treeHeight):
    if depth==treeHeight:
        return score[currIndex]
    if(isMax):
        return max(MinMax(depth+1,currIndex*2,False,score,treeHeight),MinMax(depth+1,currIndex*2+1,False,score,treeHeight))
    else:
        return min(MinMax(depth+1,currIndex*2,True,score,treeHeight),MinMax(depth+1,currIndex*2+1,True,score,treeHeight))

score=[1,2,4,5,6,7,8,9]
treeHeight=int(m.log(len(score),2))
print(MinMax(0,0,False,score,treeHeight))