# AsyncIO
```
비동기 프로그래밍을 위한 모듈이며 CPU 작업과 I/O를 병렬로 처리하게 해줍니다.
```

## 이벤트 루프 ?
```
이벤트 루프는 작업들을 하나씩 실행시키는 역할을 합니다.  
메인 스레드에서 실행된 작업이 특정한 데이터를 요청하고 응답을 기다려야 한다면(I/O 작업),  
이 작업은 이벤트 루프에 통제권을 넘겨줍니다. 통제권을 받은 이벤트 루프는 다음 작업을 실행하게 됩니다.  
그리고 응답을 받은 순서대로 멈췄던 부분부터 다시 통제권을 가지고 작업을 마무리합니다.

메인 스레드 -> Task(여러 코루틴) -> 첫 코루틴 실행 -> 응답을 기다려야하는 작업 ->  
이벤트 루프에 해당 작업을 맡기고 -> 다음 코루틴 실행 -> 응답이 마무리된 코루틴부터 작업을 다시 시작함
```

## AsyncIO는 스레딩에서의 문제점을 어떻게 해결하였는가
```
- CPU 컨텍스트 스위칭: asyncio 는 비동기이며 이벤트 루프를 사용한다.  
  이는 I/O를 대기하는 동안 애플리케이션이 컨텍스트 스위치를 관리할 수 있도록 한다. CPU 스위칭이 없다!

- 경쟁 조건(Race Conditions): asyncio 는 한 번에 오직 하나의 코루틴만 실행하며 정의된 지점에서만  
  스위칭이 일어나기 때문에, 코드는 경쟁 조건으로부터 안전하다.

- 데드락/라이브 잠금(Dead-Locks/Live-Locks): 경쟁 조건에 대해 걱정할 필요가 없기 때문에,   
  잠금을 사용할 필요가 없다. 이는 데드락으로부터 매우 안전하게 만들어준다.  
  만약 두 개의 코루틴이 서로를 깨워야(wake) 할 필요가 있을 경우엔 여전히 데드락이 발생할 가능성이 있지만,  
  이런 일을 해야할 경우는 매우 드물 것이다.

- 기아 상태(Resource Starvation): 모든 코루틴이 하나의 스레드에서 실행되고,  
  추가적인 소켓이나 메모리를 필요로하지 않기때문에, 되려 리소스가 부족하기가 힘들 것이다.  
  그러나 Asyncio 는 기본적인 스레드 풀인 “executor pool”을 하나 가지고 있다.  
  만약 매우 많은 일들을 하나의 “executor pool”에서 실행한다면, 여전히 리소스 부족에 대한 문제가 발생할 수 있다.  
  하지만, 매우 많은 실행 프로그램을 사용하는것은 안티 패턴이며, 아마 이런 일을 자주 하지는 않을 것이다.
```

## 코루틴이란,
```
- caller가 함수를 call하고, callee(함수)가 caller에게 값을 return하면서  
  종료하는 것에 더해 return하는 대신 suspend(혹은 yield)하면 caller가 나중에 resume하여  
  중단된 지점부터 실행을 이어갈 수 있다.
- Generator와 비슷하지만 generator와 목적(거대한 iterator 객체를 만드는 것)이 다르다.  
  외부와의 상호 작용이 목적
```

## 서브루틴이란,
```
- 메인 루틴에 종속되어있는 루틴으로 메인루틴에서 서브루틴에 이벤트/작업(반복되는 작업)을 맡긴다.
```

### 제네레이터 기반 코루틴
```
- 제네레이터를 확장시켜 만들 수 있다.
- 제네레이터에서 생산한 데이터를 소비하는 코드에서 send 함수를 사용하여  
  yield 표현식(a = yield)에 값을 보낼 수 있는 코루틴
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
- next() 메소드로 데이터를 순차적으로 호출 가능한 객체이다.  
  만약 next() 로 다음 데이터를 불러 올수  없을 경우 (가장 마지막 데이터인 경우)  
  StopIteration exception을 발생시킨다.
```