<template>
    <div class="navBar">
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand to='/'> 欢乐食光 </b-navbar-brand>
            <!-- nav toggle -->
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      
            <b-collapse id="nav-collapse" is-nav>
                <!-- todo: active -->
                <b-navbar-nav>
                    <b-nav-item index="1" to='/main'>首页</b-nav-item>
                    <b-nav-item index="2" to='/recipes'>美食食谱</b-nav-item>
                    <b-nav-item index="3" to='/diaries'>美食日记</b-nav-item>
                    <b-nav-item index="4" to='/foods'>食物介绍</b-nav-item>
                    <b-nav-item index="5" to='/about'>关于</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>

export default {
    name: 'navBar',
}

</script>

<style>
    
</style>