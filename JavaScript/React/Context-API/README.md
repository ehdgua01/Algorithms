# Context API

2018년 3월말에 React 16.3이 릴리즈되면서 새로워진 Context API!

기존에도 Context API는 존재했지만 사용성이 불편해 많이 사용되고 있지 못한 상태였는데  
이번 업데이트를 통하여 편리성을 높여 특정 상황에서만 사용하는 기능이 아니라 일반적인 상황에서도 사용할 수 있도록 편리성을 높였다고 한다.

Context API는 Provider와 Consumer라는 컴포넌트를 통하여 모든 레벨의 컴포넌트가 사용할 수 있는 데이터를 제공한다.  
ex) 사용자 로그인 정보, 부모 데이터 관리 함수, 테마 설정 등  
이러한 기능들은 Redux, MobX 등 유명하고 성능이 좋은 라이브러리들이 존재하는데 Context API를 쓰는 이유는 앞서 말한 라이브러리에 비해서 사용하기가 정말 간단하기 때문에 굳이 라이브러리를 써야할 상황이 아니라면 Context API를 사용하는 것도 나쁘지 않은 선택이다.

## 어떤 용도로 사용하는가

- 전역 상태 관리

  단방향 데이터 플로우의 특성상 React에서는 top-down(부모-자식)으로 데이터 전달이 되는데  
   에를 들면,  
   A -> B -> C 순으로 가야할 데이터가 존재할 때 Context를 사용하게 되면
  데이터를 생성하고 C 에서 해당 데이터를 불러와서 사용하는 게 가능하게 된다.

  ```
  class A extends React.Component {
      render() {
         return <B theme="dark" />;
      }
  }

  function B(props) {
      return (
          <div>
             <C theme={props.theme} />
          </div>
     );
  }

  function C(props) {
      return <Button theme={props.theme} />;
  }
  ```

  ```
  const ThemeContext = React.createContext('light');

   class A extends React.Component {
       render() {
           return (
               <ThemeContext.Provider value="dark">
                   <B />
               </ThemeContext.Provider>
           );
       }
   }

   function B(props) {
       return (
           <div>
               <C />
           </div>
       );
   }

   function C(props) {
       return (
           <ThemeContext.Consumer>
               {theme => <Button {...props} theme={theme} />}
           </ThemeContext.Consumer>
       );
   }
  ```

## 정리

---

React에 입문하고 나서 컴포넌트 개념과 부모-자식를 통한 데이터 전달 등을 접하였을 때는 재밌고 더 알아보고 싶은 욕심이 충만했는데, Redux 같은 전역 상태 관리 라이브러리를 배우기 시작할 때 React를 배우고자하는 욕심이 줄어드는 것을 경험했다. 이유는 Flux 라는 개념과 store를 생성하고 action, reducer를 정의하고 dispatch를 통해 action을 실행시키고, 순수 함수(외부 또는 인자로 들어온 값을 함수 내에서 변경하지 않고 항상 같은 결과를 출력하는 함수)라는 다소 생소한 개념들을 배워야했기 때문이다. 물론 어려워도 배우려고 노력하니 많은 것들을 알 수 있었지만, 처음으로 돌아가서 바로 Redux를 접하는 건 지금 생각해도 그렇게 쉽지 않을 거 같다는 생각이 든다.

이번에 Context API를 배우면서 느낀 점은 React를 입문하는 사람들이 Context API를 먼저 접하는 것이 전역 상태 관리나 React를 이해하는 데 더 쉽고 몸소 깨달을 수 있을 거 같다는 생각이 들었고, 간단한 어플리케이션을 만들 때도 많은 작업이 필요한 라이브러리들 대신에 Context API로 쉽고 빠르게 만들어 보는 것도 좋을 거 같다는 생각이 들었다.

## 참고

- https://velopert.com/3606

- http://webframeworks.kr/tutorials/react/react-dataflow/

- https://medium.com/@Dongmin_Jang/reactjs-context-api-korean-%ED%95%9C%EA%B8%80-%EC%9E%91%EC%84%B1%EC%A4%91-79edaf18efff
