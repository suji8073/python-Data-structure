
def even_or_odd(a):
    # 짝수인지 홀수인지 판별하고 배열에 저장하여 출력하는 함수
    
    if len(a) == 0: # a 배열이 비었다면
       even.extend(odd) # 짝수 배열 뒤에 홀수 배열 더함
       return(print("After arranging:   ["+', '.join(even)+"]")) # 변경된 array 출력
    
    if (int(a[0]) % 2 ) == 1: # a[0]가 홀수이면
        odd.append(a[0]) # 홀수를 저장하는 배열인 odd에 a[0] 추가
        
        even_or_odd(a[1:]) #a[1]부터 문자열의 끝까지 뽑아내어 a에 저장

        
    else: # a[0]가 짝수이면
        even.append(a[0]) # 짝수를 저장하는 배열인 even에 a[0] 추가
        
        even_or_odd(a[1:]) #a[1]부터 문자열의 끝까지 뽑아내어 a에 저장
        


odd = [] # 홀수를 저장하는 배열 
even = [] # 짝수를 저장하는 배열


num = input("Before arranging:   ") # 사용자가 입력하는 문자열 저장하는 배열

num = num.strip('[]') #양쪽의 특정 문자 삭제
num = num.split(', ') # 콤마와 띄어쓰기 삭제

even_or_odd(num)


    
    
