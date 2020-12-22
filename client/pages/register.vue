<template>
    <!-- 注册页面 -->
    <div>
        <navBar />
        <main class="signup_form">
            <div id="app">
                <div id="login">
                    <div id="description">
                        <h1>注册</h1>
                        <p>获取新账号，开启美食之门</p>
                    </div>
                    <div id="form">
                        <label for="username">用户名：</label>
                        <input type="text" id="username" v-model="registerForm.username" placeholder="请输入用户名" autocomplete="off">
                        <label for="email">邮箱：</label>
                        <input type="text" id="email" v-model="registerForm.email" placeholder="请输入邮箱" autocomplete="off">
                        <label for="password">密码：</label>
                        <input type="password" id="password" v-model="registerForm.password" placeholder="请输入密码">
                        <label for="password2">确认密码：</label>
                        <input type="password" id="password2" v-model="registerForm.password2" placeholder="请再次输入密码">
                        <button @click="register">注册</button>
                    </div>
                </div>
            </div>
        </main>
        <myFooter />
    </div>
</template>
 
<script>

import axios from 'axios'
import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";


export default {
    data () {
        return {
            registerForm: {
                username: '',
                email: '',
                password: '',
                password2: ''
            }
        };
    },

    components: {
        navBar,
        myFooter,
    },
 
    methods: {
        register () {
            let _this = this;
            let reg1 = /^[a-zA-Z][a-zA-Z0-9_-]{5,19}$/;
            let reg2 = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;

            if (this.registerForm.username === '' || this.registerForm.email === '' || this.registerForm.password === '' || this.registerForm.password2 === '') {
                alert('所有都是必填项！');
            } else if(!reg1.test(this.registerForm.username)) {
                alert('用户名应以字母开头，且只包含字母、数字、下划线，长度为6到19位！');
            } else if(!reg2.test(this.registerForm.email)) {
                alert('邮箱格式不正确！');
            } else if (this.registerForm.password !== this.registerForm.password2) {
                alert('两次密码输入不一致！');
            } else {
                axios.post(`http://localhost:8000/account/api/register`, _this.registerForm).then(res => {
                    alert('注册成功！');
                    this.$router.push('/login');
                })
                .catch(error => {
                    let code = error.response.status;
                    if (code == 400) {
                        alert('用户名或邮箱已被占用！');
                        location.reload()
                        this.$router.go(0)
                    }
                })
            }
        }
    }
};
</script>

<style scoped>

.signup_form {
	background-color: #fff;
	border-radius: 20px;
	margin: auto;
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
}

div#app {
  width: 100%;
  height: 100%;
}

div#app div#login {
  align-items: center;
  background-color: #e2e2e5;
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100%;
}

div#app div#login div#description {
  background-color: #ffffff;
  width: 300px;
  padding: 35px;
}

div#app div#login div#description h1,
div#app div#login div#description p {
  margin: 0;
}

div#app div#login div#description p {
  font-size: 0.8em;
  color: #95a5a6;
  margin-top: 10px;
}

div#app div#login div#form {
  background-color: #ffc400;
  border-radius: 5px;
  box-shadow: 0px 0px 30px 0px #666;
  color: #ecf0f1;
  width: 350px;
  padding: 35px;
}

div#app div#login div#form label,
div#app div#login div#form input {
  outline: none;
  width: 100%;
}

div#app div#login div#form label {
  color: #d4d4d4;
  font-size: 0.8em;
}

div#app div#login div#form input {
  background-color: transparent;
  border: none;
  color: #ecf0f1;
  font-size: 1em;
  margin-bottom: 20px;
}

div#app div#login div#form ::placeholder {
  color: #ecf0f1;
  opacity: 1;
}

div#app div#login div#form button {
  background-color: #ffffff;
  cursor: pointer;
  border: none;
  padding: 10px;
  transition: background-color 0.2s ease-in-out;
  width: 100%;
}

div#app div#login div#form button:hover {
  background-color: #eeeeee;
}

@media screen and (max-width: 600px) {
  div#app div#login {
    align-items: unset;
    background-color: unset;
    display: unset;
    justify-content: unset;
  }

  div#app div#login div#description {
    margin: 0 auto;
    max-width: 350px;
    width: 100%;
  }

  div#app div#login div#form {
    border-radius: unset;
    box-shadow: unset;
    width: 100%;
  }

  div#app div#login div#form form {
    margin: 0 auto;
    max-width: 280px;
    width: 100%;
  }
}

</style>