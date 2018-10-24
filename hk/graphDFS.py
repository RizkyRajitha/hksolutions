def ddfs(startnode, graph,f):
    vvisited[startnode] = 1    
    for item in graph[startnode]:
        if vvisited[item] == 0:
            print(item)
            f.append(1)    
            ddfs(item, graph,f)
            print(f"ret from dfs -- - {f}")
    return f
        
def pl(graph,clib,croad,n):

    jk = 0
    alone = 0
    cost = 0
    f = []
    
    if  clib<=croad or clib ==0:
        return clib*n
    
    else:
        for startnode in nodes:
            if vvisited[startnode]==0:

                if graph[startnode]==[]:
                    #print("alone")
                    alone+=1  
                j = ddfs(startnode, graph,f=[])

                if j !=None:  
                    print(f" nodes of one cluster    {len(j)}")
                    cost = cost + clib + len(j)*croad
                    print(f"cost ---- {cost}")
    
    print(alone)
    #if alone >0:
        #cost = cost + clib*(alone)
    print(f"cost ---- {cost}")
    print(vvisited)
                




if __name__ =="__main__":
    n = 10
    vvisited = [0] * (n+1)
    #graph = [[1,2],[3,4],[5],[1],[1],[2],[7],[6]]
    city = { 1: [2,3], 2: [1], 3: [1] ,4:[5,6], 5: [4],6:[4],7:[], 8: [], 9: [],10:[]}# 6: [7], 7: [6] , 8:[]}#, 8: [7], 9: [],10:[]}
    nodes = [ 1, 2, 3,4,5,6,7,8,9,10]
    clib = 10
    croad = 2
    pl(city,clib,croad,n)
    
    

    #print(f"final cost k -- {k}")

