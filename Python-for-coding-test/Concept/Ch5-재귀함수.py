# 재귀함수란 자기 자신을 다시 호출하는 함수를 의미한다.
# 단순한 형태의 재귀 함수 예제
  # '재귀 함수를 호출합니다.'라는 문자열을 무한히 출력합니다.
  # 어느 정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력됩니다.
  
# def recursive_function():
#     print('재귀함수를 호출합니다.')
#     recursive_function()

# recursive_function()

# 재귀함수의 종료 조건
# 재귀함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야 한다.

# 종료 조건을 포함한 재귀함수 예제

def recursive_function2(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1,'번째 재귀함수를 호출합니다.')
    recursive_function2(i+1)
    print(i, '번째 재귀함수를 종료합니다.')
    
recursive_function2(1)