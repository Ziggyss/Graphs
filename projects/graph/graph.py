"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
       
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        
        # check that v1 and v2 exist in the vertices dictionary
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 to the vertices at v1
            self.vertices[v1].add(v2)
        # otherwise
        else:
            # raise an exception and give an error 
            raise IndexError("That vertex does not exist")  

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        def get_neighbours(self, vertex_id):
            return self.vertices[vertex_id]  

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        # Tom's solution had visited=None as a parameter
        # then:
        
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create the visited set - need to do this outside the recursive function
        if visited is None:
            visited = set()
            # (Above code is for quirk of Python as explained in lecture)
        
        # Print the starting_vertex
        print(starting_vertex)
        # Add the starting_vertex to the visited set
        visited.add(starting_vertex)
        # Loop through the adjacent vertices
        for v in self.vertices[starting_vertex]:
            # check to see if the vertex has been visited
            if v not in visited:
                # then, if not recur, passing in v as the starting_vertex and the visited set
                self.dft_recursive(v, visited)



    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue and enqueue a PATH to the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first PATH eg: [a, b, c, r, g]
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # check if the last vertex has been visited before
            if last_vertex not in visited:
                # Check if it's the target
                if last_vertex == destination_vertex:
                    # if so, return path
                    return path
                # Mark it as visited...
                visited.add(last_vertex)
                # Then add a path to its neighbours to the back of the queue

                # This is the part I don't quite understand - below:

                for next_vert in self.vertices[last_vertex]:
                    # Copy the contents of the current path into a new path and append the next vertex
                    next_path = list(path)
                    next_path.append(next_vert)
                    # Append the neigbour to the back of the queue
                    q.enqueue(next_path)
        # return None
        return None            

              
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
       

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push a PATH to the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty
        while s.size() > 0:
            # pop the first PATH eg: [a, b, c, r, g]
            path = s.pop()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # check if the last vertex has been visited before
            if last_vertex not in visited:
                # Check if it's the target
                if last_vertex == destination_vertex:
                    # if so, return path
                    return path
                # Mark it as visited...
                visited.add(last_vertex)
                # Then add a path to its neighbours to the back of the queue
                # This is the part I don't quite understand

                for v in self.vertices[last_vertex]:
                    # Copy the contents of the current path into a new path and append the next vertex
                    next_path = list(path)
                    next_path.append(v)
                    # Append the neigbour to the back of the queue
                    s.push(next_path)
        return None            

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # if visited is None:
        #     visited = set()

        # # base case
        # if starting_vertex == destination_vertex:
            # return path



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
