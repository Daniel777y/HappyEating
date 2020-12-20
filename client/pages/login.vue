<template>
    <div>
        <navBar />
        <main class="login_form">
            <div id="app">
                <div id="login">
                    <div id="description">
                        <h1>登录</h1>
                        <p>开启你的美食之旅</p>
                    </div>
                    <div id="form">
                        <label for="username">用户名：</label>
                        <input type="text" id="username" v-model="loginForm.username" placeholder="请输入用户名" autocomplete="off">

                        <label for="password">密码：</label>&nbsp;
                        <!-- <i class="fas" :class="[passwordIcon]" @click="hidePassword = !hidePassword"></i> -->
                        <input type="password" id="password" v-model="loginForm.password" placeholder="请输入密码">

                        <button @click="login">确认</button>
                    </div>
                </div>
            </div>
        </main>
        <myFooter />
    </div>
</template>
 
<script>
import axios from 'axios'
//import common from '~/components/common'
import common from '~/store/common'
import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";

export default {
    data () {
        return {
            loginForm: {
                username: '',
                password: ''
            },
            uname: '',
        };
    },
    components: {
        navBar,
        myFooter,
    },
    
    methods: {
        login () {
            let _this = this;
            if (this.loginForm.username === '' || this.loginForm.password === '') {
                alert('账号或密码不能为空！');
            } else {
                axios.post(`http://localhost:8000/api/token/`, _this.loginForm).then(res => {
                    console.log(res);

                    localStorage.setItem('access_token', res.data.access);
                    localStorage.setItem('refresh_token', res.data.refresh);
                    localStorage.setItem('username', res.data.username);

                    // common.state.username = res.data.username;
                    // common.state.access_token = res.data.access;
                    // common.state.refresh_token = res.data.refresh;

                    common.setState(res.data.access, res.data.refresh, res.data.username);

                    this.uname = localStorage.getItem('username');
                    console.log(this.uname);
                    // console.log(common.state.username);

                    alert('登录成功！');
                    this.$router.push('/main');
                }).catch(error => {
                    console.log(error);
                    let code = error.response.status;
                    if (code == 401) {
                        alert('用户名与密码不匹配！')
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

.login_form {
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