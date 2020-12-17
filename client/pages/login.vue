<template>
  <div>
    <input type="text" v-model="loginForm.username" placeholder="用户名"/>
    <input type="text" v-model="loginForm.password" placeholder="密码"/>
    <button @click="login">登录</button>
  </div>
</template>
 
<script>
import axios from 'axios'


export default {
    data () {
        return {
            loginForm: {
                username: '',
                password: ''
            }
        };
    },
    
    methods: {
        login () {
            let _this = this;
            if (this.loginForm.username === '' || this.loginForm.password === '') {
                alert('账号或密码不能为空');
            } else {
                axios.post(`http://localhost:8000/api/token/`, _this.loginForm).then(res => {
                    console.log(res);
                    localStorage.setItem('access_token', res.data.access);
                    localStorage.setItem('refresh_token', res.data.refresh);
                })
                    .catch(error => {
                    console.log(error);
                })
            }
        }
    }
};
</script>