import csv

class System:
    steps = [   
        [-1,0], # Top Step
        [0,1],  # Right Step
        [1,0], # Bottom Step
        [0,-1] # Left Step
    ]
    
    def __init__(self):
        self.star_city = list()
        self.star_city_rows = 0
        self.star_city_cols = 0
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.reader(data_file)
        self.star_city=list()
        for row in reader:
            self.star_city.append(row)
        self.star_city_rows=len(self.star_city)
        self.star_city_cols=len(self.star_city[0])

    def check_limits(self,row_num, col_num):
        if 0 <= row_num < self.star_city_rows and 0 <= col_num < self.star_city_cols:
            return True
        return False

    def get_neighbours(self,row,col):
        neighbours=[]
        #loop through top, right, bottom and left adjacent nodes to get the neighbor
        # only if the altitude of adjacent node is lower or equal to the current node 
        # and is not already present in neighbors list
        for i in System.steps:
            if self.check_limits(row+i[0], col+i[1]):
                if self.star_city[row+i[0]][col+i[1]] <= self.star_city[row][col] and (row+i[0],col+i[1]) not in neighbours:
                    neighbours.append((row+i[0],col+i[1]))
        return neighbours

    def find_route(self,source,destination):

        self.source_node = source
        self.destination_node = destination
        self.vertexQ = []
        self.visited_nodes = []
        self.found_destination = False
        self.parent = dict()

   
        #add 1st node in visited and que lists

        self.vertexQ.append(self.source_node)
        self.visited_nodes.append(self.source_node)
        self.parent[self.source_node] = None #Source node doesn't have any parent so make it NONE
        
        #traverse all the nodes from queue till the queue is not empty
        # and destination is not found

        while len(self.vertexQ) != 0 and not self.found_destination:
        
            #remove current node from queue
            
            current_node = self.vertexQ.pop(0)
            
            #check if current node has neighbours
            
            if len(self.get_neighbours(current_node[0],current_node[1])) != 0:
                #temporary list which will have all neighbour nodes of current node 
                # which are added in visited list

                neighbours_list = self.get_neighbours(current_node[0],current_node[1])
                
                #get each neighbor of current node

                for neighbour in neighbours_list:
                
                    #if neighbor is not visited then mark it visited by adding in visited 
                    # and also add it in queue

                    if neighbour not in self.visited_nodes:
                        self.visited_nodes.append(neighbour)
                        self.vertexQ.append(neighbour)
                        self.parent[neighbour] = current_node  # Neighbour as key and parent node as value in dictionary
                    
                        # if neighbour is the destination node 
                        # then extract all the nodes from visited till the current node 
                        # and break the loop

                        if neighbour == self.destination_node:
                            self.found_destination = True
                            break
                    
                        #if neighbour already in visited list, 
                        # so no need  to keep the current node and 
                        # the neighbours (already added in visited) of current node
                        # in the visited list and queue list
                        
                        
            
                # if current node has no neighbour then no need to keep it in visited list  
            else:
                self.visited_nodes.remove(current_node)    

        # If length of queue is zero and destination isn't found. It means there is no path..
        if len(self.vertexQ) == 0 and not self.found_destination:
            return 0

        # If destination found. Retrive path from parent dictionary and return 
        if self.found_destination:
            path = []
            path.append(self.destination_node)
            while self.parent[self.destination_node] != None:
                path.append(self.parent[self.destination_node])
                self.destination_node = self.parent[self.destination_node]
            path.reverse()  # Reverse because we retrive path from destination node
            return path

    def Bluevalley_to_Smallville_route(self):
        Bluevally = [(0,0),(1,0),(2,0),(3,0),(4,0)] #Starting nodes of BlueVally
        smallville = [(0,4),(1,4),(2,4),(3,4),(4,4)] #Starting nodes of Smallville
        route = []
        for source in Bluevally:
            for destination in smallville:
                if self.find_route(source,destination) == 0:
                    #print(f'{(source,destination)} + no')
                    pass
                else:
                    route.append( self.find_route(source,destination))

                    #print(f'{(source,destination)} + yes') # We can find available source and destination where path available
                    
        #Printing the path if route is not empty
        if len(route) != 0:
            path =   min(route,key = len) # Return minimum length path
            print('\n\nTo reach city Smallville from city Blue Valley the nodes traversed are-')
            print('Blue Valley ----> ',end = '')
            for node in path:
                print(f"({node[0]},{node[1]}) ----> ",end = '')
            print('SmalleVille\n')

        else:
            print('\n\nThere is No path from city Blue Valley to city Smallville\n')

# Some changes happened here. please consider it

if __name__ == "__main__":
    test_system1 = System()
    
    #Getting data in 2D matrix
    test_system1.config_system('city_data.csv')
    
    #Finding path between Source node to Destination node
    
    #'_' was removed based on return. 
    
    route = test_system1.find_route((3,0),(4,2))  

    '''Checking for path availability. 
       if path doesn't found it returns 0 so, if it is'nt 0 we ready to print path'''
    if route != 0:
        print(f"\n\nTo reach Node (4,2) from Node (3,0) the nodes traversed are-")
        for node in route[:-1]:
            print(f"({node[0]},{node[1]}) ---->", end=" ")
        print((4,2))
    else:
        print('\n\nPath Not Found!!')
    
    #Finding path between Bluevalley to Smallville   
    test_system1.Bluevalley_to_Smallville_route()
    

   
    
