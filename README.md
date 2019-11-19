# eVue - DRF

## 1. 기본 설정

1. Django

   1. 가상환경 설정

      1. ```
         $ python -V
         3.7.4
         $ python -m venv venv
         $ source venv/Scripts/activate
         (venv) $
         ```

      

   2. 패키지 설치

      1. 

         ```
         $ pip install django djangorestframework
         pip freeze > requirements.txt
         ```

   3. django 프로젝트 생성

      ```
      $ django-admin startproject ( 프로젝트명) .
      ```

      

2.  Vue

   1. VueCli 설치

      ```
      $ npm install -g @vue/cli
      ```

   2. Vue 프로젝트 생성

      ```
      $ vue create (프로젝트 이름)
      ```

3. 프로젝트 폴더 구조

```
todo-django-vue/
	.git/
	todo-django/
		vue/
		manage.py
		todo_django/
	todo-vue/
		node_moduels/
		public/
		src/
		package.json
```

## DRF 모델링

## vUE

Vue-router

```
eeeeeeeeeeeeee$ npm i vue-router
$ vue add router
	Still proceed? y
	User history mode for router(Requires proper server ...)
```



## 4. Todos axios 요청

```vue
mounted(){
    // axios 요청 호출
    this.getTodos
    },
  methods : {
    todoCreate(event){
      this.todos.push(event)
    },
    getTodos(){
     axios.get('http://127.0.0.1:8000/api/v1/todos/')       
    .then(response =>{
      console.log(response)   
      this.todos = response.data
    })
    } 
}
```

3. CORS 오류 발생

   * 해결하기 위해서는 DJANGO 서버에서 설정이 필요

4. `DJANGO-CORS-HEADERS` 패키지 사용

   * [Github 참고]()

   ```
   pip install django-cors-headers
   ```

   * `Installed_apps`, `MIDDLEWARE` 설정
   * `CORS_ORIGIN_ALLOW_ALL` : True시 모든 도메인 요청 가능
   * `CORS_ORIGIN_WHITELIST`: 위의 옵션을 fALSE로 하고 화이트리스트에 직접 도메인 등록
   * 기타 옵션들 확인 해보기

5. Vue에서 다시 요청 보내보기