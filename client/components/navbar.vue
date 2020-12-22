<template>
    <!-- 导航栏样式 -->
    <div class="navBar fixed-top">
        <b-navbar toggleable="lg" type="dark" variant="warning">
            <b-navbar-brand to='/'> 欢乐食光 </b-navbar-brand>
            <!-- nav toggle -->
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      
            <b-collapse id="nav-collapse" is-nav>
                <!-- todo: active -->
                <b-navbar-nav class="navbar-nav mr-auto">
                    <b-nav-item index="1" to='/main'>首页</b-nav-item>
                    <b-nav-item index="2" to='/recipes'>美食食谱</b-nav-item>
                    <b-nav-item index="3" to='/diaries'>美食日记</b-nav-item>
                    <b-nav-item index="4" to='/foods'>食物介绍</b-nav-item>
                </b-navbar-nav>
                <b-navbar-nav>
                    <b-nav-item v-if="username" @click="gotomine">你好，{{ username }}</b-nav-item>
                    <b-nav-item v-else @click="register">注册</b-nav-item>
                    <b-nav-item v-if="username" @click="logout">登出</b-nav-item>
                    <b-nav-item v-else @click="login">登录</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
import axios from 'axios'
import common from '~/components/common'

export default {
    name: 'navBar',
    data () {
        return {
            username: '',
        };
    },
    mounted() {
        if (localStorage.username) {
            this.username = localStorage.username;
        }
    },
    methods: {
        gotomine() {
            this.$router.push('/mine');
        },
        login() {
            this.$router.push('/login');
        },
        register() {
            this.$router.push('/register');
        },
        logout() {
            alert('您已登出！');
            localStorage.clear();
            this.$router.push('/');
        },
    },
}

</script>

<style>
    
</style>