<template>
  <div>
    <input type="text" v-model="registerForm.username" placeholder="用户名"/>
    <input type="text" v-model="registerForm.email" placeholder="邮箱"/>
    <input type="text" v-model="registerForm.password" placeholder="密码"/>
    <input type="text" v-model="registerForm.password2" placeholder="确认密码"/>
    <button @click="register">注册</button>
  </div>
</template>
 
<script>

import axios from 'axios'


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
 
  methods: {
    register () {
        let _this = this;
        if (this.registerForm.username === '' || this.registerForm.email === '' || this.registerForm.password === '' || this.registerForm.password2 === '') {
            alert('所有都是必填项');
        } else {
            axios.post(`http://localhost:8000/account/api/register`, _this.registerForm).then(res => {
                console.log(res);
            })
            .catch(error => {
                console.log(error);
            })
        }
    }
  }
};
</script>