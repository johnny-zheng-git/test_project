#### 使用方法
- NEAV目录执行python run.py
- postman        
```
注册：http://127.0.0.1:8080/user/registration
post
{
	"username":"admin",
	"password":"123456"
}
登录：http://127.0.0.1:8080/user/login
post
带有access_token
验证：http://127.0.0.1:8080/user/secret
get
带有access_token
```
