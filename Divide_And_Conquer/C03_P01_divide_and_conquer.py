import csv

class System:
    def __init__(self):
        self.sensors_list = list()
        self.sensor_mapping_list = list()
        self.master_node_list = list()
        self.dict = {}
        self.counter = 0
        self.overload_master = ''
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.DictReader(data_file)
        for row in reader:
            node_id = row['Node ID']
            type = row['Type']
            master_node_id = row['Master Node ID']
            
            if type == 'Master':
                self.master_node_list.append(int(master_node_id))
            elif type == "Sensor":
                self.sensors_list.append(int(node_id))
                self.sensor_mapping_list.append(int(master_node_id))
                
        
    def SensorAssignedCount(self, mapping_list, l, r, OverloadSensor):
        count = 0
        for i in range(l, r+1):
            if (mapping_list[i] == OverloadSensor): 
                count +=  1
        return count
    
    def OverloadNodeHelper(self,l, r):

        #Calculating middle index of the array
        mid = (l + r)//2

        #base case
        if l == mid:
            master_node = self.sensor_mapping_list[l]
            self.dict[master_node] = self.dict.get(master_node,0) + 1
            #Conquering
            if self.dict[master_node] >= self.counter:
                self.counter,self.overload_master = self.dict[master_node],master_node
            return 
        
        #Dividing
        left = self.OverloadNodeHelper(l,mid)
        right = self.OverloadNodeHelper(mid,r)

        if self.counter >= len(self.sensor_mapping_list)//2:
            return self.overload_master
        else:
            return 

        #pass
        
    def getOverloadedNode(self):
        return self.OverloadNodeHelper(0, len(self.sensor_mapping_list)) #Removed -1 for convenience
    
    def getPotentialOverloadNode(self):

        for master in self.sensor_mapping_list:
            if len(self.sensor_mapping_list) // 2 > self.sensor_mapping_list.count(master) >= len(self.sensor_mapping_list)//3:
                return master
        return -1

        #pass
    
if __name__ == "__main__":
    test_system1 = System()
    
    test_system1.config_system('app_data1.csv')
    
    print("Overloded Master Node : ", test_system1.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system1.getPotentialOverloadNode())

    test_system2 = System()
    
    test_system2.config_system('app_data2.csv')
    
    print("Overloded Master Node : ", test_system2.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system2.getPotentialOverloadNode())

    test_system3 = System()

    test_system3.config_system('app_data3.csv')
    
    print("Overloded Master Node : ", test_system3.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system3.getPotentialOverloadNode())

    test_system4 = System()

    test_system4.config_system('app_data4.csv')
    
    print("Overloded Master Node : ", test_system4.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system4.getPotentialOverloadNode())
