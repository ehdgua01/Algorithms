## 코루틴이란,
```
- caller가 함수를 call하고, callee(함수)가 caller에게 값을 return하면서 종료하는 것에 더해 return하는 대신 suspend(혹은 yield)하면 caller가 나중에 resume하여 중단된 지점부터 실행을 이어갈 수 있다.
- Generator와 비슷하지만 generator와 목적(거대한 iterator 객체를 만드는 것)이 다르다. 외부와의 상호 작용이 목적
```

## 서브루틴이란,
```
- 메인 루틴에 종속되어있는 루틴으로 메인루틴에서 서브루틴에 이벤트/작업(반복되는 작업)을 맡긴다.
```

### 제네레이터 기반 코루틴
```
- 제네레이터를 확장시켜 만들 수 있다.
- 제네레이터에서 생산한 데이터를 소비하는 코드에서 send 함수를 사용하여 yield 표현식(a = yield)에 값을 보낼 수 있는 코루틴
```

### 네이티브 코루틴(비동기 코루틴)
```
- async, await 구문을 사용하는 코루틴
async - 비동기 코루틴를 표현하는 키워드
await - 비동기 코루틴의 결과를 기다리는 키워드
```

## 제네레이터란,
```
- 제네레이터 안에서 데이터를 생산한다.
- 일반 함수와는 다르게 suspend/resume이 가능하여 진입점이 많은 함수이다.
- iterator를 생성하는 함수이다.
- 큰 메모리를 필요로 하는 곳에서 효과적이다.
- Lazy evaluation 즉 계산 결과 값이 필요할 때까지 계산을 늦추는 효과를 볼 수 있다.
```

## iterable과 iterator의 차이
```
iterable
- iterable 의 의미는 member를 하나씩 차례로 반환 가능한 객체를 말한다. 
- iterable 의 예로는 sequence type인 list, str, tuple 이 대표적이다.

iterator
- next() 메소드로 데이터를 순차적으로 호출 가능한 객체이다. 만약 next() 로 다음 데이터를 불러 올수  없을 경우 (가장 마지막 데이터인 경우) StopIteration exception을 발생시킨다.
```