def astar(graph,start,end):
    open_list=[(0,start)]
    closed_list=set()
    
    while open_list:
        f,current_node=min(open_list)
        open_list.remove((f,current_node))
        
        if current_node == end:
           return reconstruct_path(graph,start,end,closed_list)
        
        closed_list.add(current_node)
        
        for neighbour,cost in graph[current_node]:
            if neighbour in closed_list:
                continue
            g=f+cost 
            h=heuristic(neighbour,end)
            f=g+h 
            open_list.append((f,neighbour))
    return None


def reconstruct_path(graph, start, end, closed_list):
    path = [end]
    curr_node = end
    while curr_node != start:
        found_prev = False
        for node in graph:
            if curr_node != node:
                for neighbour, _ in graph[node]:
                    if neighbour == curr_node and node in closed_list:
                        path.append(node)
                        curr_node = node
                        found_prev = True
                        break
            if found_prev:
                break
    return path[::-1]


                
def heuristic(node,end):
    return 0


graph={
    'A':[('B',1),('C',3)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D':[('C',2),('B',4)]
}
start='A'
end='D'
g=astar(graph,start,end)
print(g)