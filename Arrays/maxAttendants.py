# Solution in O(n) complexity time
# We create an array with 1s for start timestamps and -1s for end timstamps. 
# We loop through the array keeping track of the max accumulated number.
def maxAttendants(startTimeStamps,endTimeStamps):
    maxTimeStamp = max(max(startTimeStamps),max(endTimeStamps))
    res = (maxTimeStamp + 2) * [0] 
    current,index,ts = 0,0,-1
    for i in range(0,len(startTimeStamps)):
        res[startTimeStamps[i]] = res[startTimeStamps[i]] + 1
        res[endTimeStamps[i]+1] = res[endTimeStamps[i]+1] - 1     
    for i in range(0, maxTimeStamp + 1): 
        current = current + res[i]
        if ts < current :
            ts = current
            index = i
    return index

start=[13,28,29,14,40,17,3]
end=[107,95,111,105,70,127,74]

start2=[1, 2, 10, 5, 5]
end2=[4, 5, 12, 9, 12]
                    
print(maxAttendants(start,end))