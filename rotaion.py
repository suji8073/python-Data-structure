class ArrayQueue:

    DEFAULT_CAPACITY = 10 #최대 배열 사이즈
    
    def __init__(self): # 빈 큐 생성
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY #고정된 용량을 가진 목록 인스턴스에 대한 참조
        self._size = 0 # 큐에 저장된 요소의 개수
        self._front = 0 # 큐에 저장된 첫번째 요소의 인덱스
        
    def __len__(self):# 큐의 요소의 개수
        return self._size

    def is_empty(self): # 큐가 비어있는지 확인하는
        return self._size == 0
    
    def first(self): # 첫번째 요소 리턴
        if self.is_empty():# 빈 배열이라면
            raise Empty("Queue is empty")
        return self._data[self._front]
    
    def enqueue(self, e): # 큐 뒤에 요소 추가
        if self._size == len(self._data):# 새로운 요소를 넣을 자리가 없을 경우 사이즈 늘려줌
            self._resize(2*len(self.data))
        avail = (self._front + self._size) % len(self._data) # 배열의 맨 끝을 찾아 요소를 저장할 위치 알아냄
        self._data[avail] = e # 찾아낸 인덱스에 요소 저장
        self._size += 1 # 요소가 저장된 크기 하나 늘려줌


    def _resize(self,cap):# 큐 크기 조정 메서드
        old = self._data # 새로운 리스트
        self._data = [None] * cap # 기존의 리스트의 사이즈를 cap만큼 늘려주고 초기화
        walk = self._front # 첫번째 위치 저장
        for k in range(self._size): # 초기화한 배열에 다시 복사
            self._data[k] = old[walk]
            walk = (1+walk)% len(old)
        self._front = 0 # 다시 0으로 초기화
        
    def rotate(self):
        # Q.enqueue(Q.dequeue())와 같은 동작을 수행하는 메서드
        
        if self.is_empty(): # 빈 배열이라면
            raise Empty("Queue is empty")
        
        answer = self._data[self._front] # 첫번째 요소 값
        self._data[self._front] = None # 첫번째 요소 값에 None 할당
        self._front = (self._front+1) % len(self._data) # 인덱스 두번째 요소 값으로 옮김
        self._size -= 1 # 배열의 크기 하나 줄임

        avail = (self._front + self._size) % len(self._data) # 배열의 맨 끝을 찾아 요소를 저장할 위치 알아냄
        self._data[avail] = answer # 위의 첫번째 요소를 찾아낸 인덱스에 저장
        self._size += 1 # 배열의 사이즈 다시 하나 늘림

    def print(self):
        # 큐에 저장된 요소들의 값 출력하는 메서드
        
        location = self._front # 첫번째 요소 위치
        print("After Rotaion:    [", end ="")
        
        for i in range(self._size-1): # 큐에 저장된 배열의 크기-1 만큼 반복
            element = self._data[location] # 첫번째 요소 위치에 있는 요소값 저장
            print(element,end = ', ') # 요소 출력
            location += 1 # 첫번째 요소 위치 하나 늘림
            
        element = self._data[location] # 큐에 저장된 배열의 마지막 요소값 저장
        print(element+"]") # 출력

   
Q = [] # 빈 배열
que = ArrayQueue()

s = input("Before Rotation:    ") # 사용자가 입력하는 문자열 저장

s = s.strip('[]') # 양쪽의 특정 문자 삭제
s = s.split(', ') # 콤마와 띄어쓰기 삭제

Q = list(s) # 문자열 하나하나를 리스트에 저장

for i in range(len(Q)): #Q의 크기 만큼 반복
    que.enqueue(Q[i]) # Q의 요소값을 차례대로 que에 저장

que.rotate() # Q.enqueue(Q.dequeue())와 같은 동작을 수행하는 메서드

que.print() # 큐에 저장된 요소들의 값 출력하는 메서드

    
