class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        component_map = {}  
        min_cost_map = {}  
        component_id = 0

        visited = set()
        
        for node in range(n):
            if node not in visited:
                queue = deque([node])
                visited.add(node)
                component_map[node] = component_id
                nodes = [node] 
                min_and = -1 

                while queue:
                    curr = queue.popleft()
                    for neighbor, weight in graph[curr]:
                        if min_and == -1:
                            min_and = weight
                        else:
                            min_and &= weight 

                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                            component_map[neighbor] = component_id
                            nodes.append(neighbor)
                
                min_cost_map[component_id] = min_and
                component_id += 1

        result = []
        for s, t in query:
            if s in component_map and t in component_map and component_map[s] == component_map[t]:
                result.append(min_cost_map[component_map[s]])
            else:
                result.append(-1)

        return result
