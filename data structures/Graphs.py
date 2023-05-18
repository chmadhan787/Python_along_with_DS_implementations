#graphs contains nodes
#a graph may be directed or undirected graph or weighted graph
#in tree there will be only one path between the nodes but in case of graph there may be more than one path
#tree can be considered as  special type of graph
#real life examples of graph data structure are google maps,internet ,facebook, amazon
class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start,end in self.edges:
            if  start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict : ",self.graph_dict)

    def get_paths(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths

    def get_shortest_path(self,start,end,path = []):
        path = path+[start]
        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path :
                sp = self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path = sp

        return shortest_path

routes = [("Mumbai","Paris"),
          ("Mumbai","Dubai"),
          ("Paris","Dubai"),
          ("Paris","Newyork"),
          ("Dubai","Newyork"),
          ("Newyork","Toronto")]

route_graph = Graph(routes)
start = "Mumbai"
end = "Newyork"
print(f"Paths between {start} and {end} is : ",route_graph.get_paths(start,end))
print(f"Shortest Path between {start} and {end} is : ",route_graph.get_shortest_path(start,end))
