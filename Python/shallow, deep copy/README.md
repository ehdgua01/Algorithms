# 얕은 복사와 깊은 복사

## Immutable, mutable 객체
| class | type
| :--- | :---
| list | mutable
| set | mutable
| dict | mutable
| custom class | mutable(almost)
| bool | immutable
| int | immutable
| float | immutable
| tuple | immutable
| str | immutable
| frozenset | immutable


## 얕은 복사
mutable한 객체를 변수에 할당  
mutable한 객체인 변수 A를 변수 B에 대입하면 값이 아닌 주소를 대입하기 때문에,  
변수 A의 값이 변경되면 변수 B의 값도 변경됨

```
a = [1, 2, 3]
b = a
a.append(4)

# result
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
```

### 주의 사항
리스트 슬라이싱을 통하여 새로운 리스트 객체를 할당할 수 있지만 리스트 안의 변수들이 mutable한 객체인 경우 조심.  
독립적인 변수 할당을 위해서는 Python 표준 라이브러리인 copy의 deepcopy를 이용하여야 함.

```
arr1 = [[1], [2], [3]]
arr2 = arr1[:]

arr1[0].append(4)

# result
arr1 = [[1, 4], [2], [3]]
arr2 = [[1, 4], [2], [3]]
```

## 깊은 복사
immutable한 객체를 변수에 할당
immutable한 객체인 변수 A를 변수 B에 대입하면 같은 얕은 복사와 같이 메모리 주소를 바라보지만,  
변수 B에 새로운 값을 할당하면 메모리 재할당이 이루어져 변수 A와 다른 주소를 가지게 됨.

```
a = 'string'
b = a
b = 'string2'

# result
a = 'string'
b = 'string2'
```
