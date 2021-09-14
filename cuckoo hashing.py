class CuckooHashing: 
    def __init__(self, size): # 
        self.M = size
        self.h = [[None, None] for x in range(size+1)]  # h-table
        self.d = [[None, None] for x in range(size+1)]  # d-table

    def hash(self, key):        # h-hash function, h(key)
        return key % self.M      
    
    def hash2(self, key):       # d-hash function, d(key)
        return (key*key % 17) *11 % self.M  
    
    def put(self, key, data): # item (key,data) 삽입위한 method 
        #### 구현하시오.
    
        a = self.hash(key)
        b=self.hash2(key)
        if self.h[a][0] == key:
            self.h[a][1] = data
        elif self.d[b][0] ==key:
            self.d[b][1] =data
        
        if self.h[a][0] == None: # h[h]가 비어있는지 확인
            self.h[a] = [key, data]
            print("i = ", a)
            print("h-table: [ ", a, "]   [", key, ", ", data, "]")
        else:
            a_prkey = self.h[a][0]
            a_prdata = self.h[a][1]
            self.h[a]=[key, data]
            print(" [ ", a_prkey, " , ", a_prdata, " ] : h[ ", a, " ] ", self.h[a], ": h[ ", a, " ] ")
            a2 = self.hash2(a_prkey)
            if self.d[a2][0] == None: # d[d]가 비어있는지 확인
                self.d[a2] = [a_prkey, a_prdata]
                print("d-table: [ ", a2, " ] ", self.d[a2])
            else:
                a2_prkey = self.d[a2][0]
                a2_prdata = self.d[a2][1]
                self.d[a2] = [a_prkey, a_prdata]
                print(" [ ", a2_prkey, " , ", a2_prdata, " ] : d[ ", a2, " ] ", self.d[a2], ": d[ ", a2, " ] ")
                self.put(a2_prkey, a2_prdata)

                                      
    def get(self, key): # key 값에 해당하는 value 값을 return
        #### 구현하시오.
        a=self.hash(key)
        a2=self.hash2(key)
        if self.h[a][0] == key:
            value = self.h[a][1]
        elif self.d[a2][0] == key:
            value = self.d[a2][1]

        return value

        

    def delete(self, key): # key를 가지는 item 삭제 
        #### 구현하시오.
        a=self.hash(key)
        a2=self.hash2(key)
        if self.h[a][0] == key:
            self.h[a] = [None, None]
        elif self.d[a2][0] == key:
            self.h[a2] = [None, None]
    
        
       

    def print_table(self):
        print('********* Print Tables ************')
        print('h-table:')
            #### h-table 출력 : 구현하시오
        for i in range (0, (len(self.h)-1)):
            print(i, end ="")
        for i in range (0, (len(self.h)-1)):
            print(self.h[i][0], end="")
        
        print('d-table:')
            #### d-table 출력 : 구현하시오
        for i in range (0, (len(self.d)-1)):
            print(i, end ="")
        for i in range (0, (len(self.d)-1)):
            print(self.d[i][0], end="")
       
 

if __name__ == '__main__':
    t = CuckooHashing(13)
    t.put(25, 'grape')      # 25:  12,   0
    t.put(43, 'apple')      # 43:   4,   0
    t.put(13, 'banana')     # 13:   0,   7
    t.put(26, 'cherry')     # 26:   0,   0
    t.put(39, 'mango')      # 39:   0,  10
    t.put(71, 'lime')       # 71:   9,   8
    t.put(50, 'orange')     # 50:  11,  11
    t.put(64, 'watermelon') # 64:  12,   7
    print()
    print('--- Get data using keys:')
    print('key 50 data = ', t.get(50))
    print('key 64 data = ', t.get(64))
    print()
    t.print_table() 
    print()
    print('-----  after deleting key 50 : ---------------')
    t.delete(50)
    t.print_table() 
    print()
    print('key 64 data = ', t.get(64))
    print('-----  after adding key 91 with data berry:---------------')
    t.put(91, 'berry')
    t.print_table()
    print()
    print('-----  after changing data with key 91 from berry to kiwi:---------------')
    t.put(91, 'kiwi')       # 91:  0,   9
    print('key 91 data = ', t.get(91))    
    t.print_table()
    
