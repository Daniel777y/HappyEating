<template>
    <div>
        <navBar />
        <body>
            主界面
        </body>
        <myFooter />
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter";
import MyFooter from '../components/myFooter.vue';

export default {
    head() {
        return { title: "首页 - 欢乐食光" };
    },
    components: {
        navBar,
        myFooter
    },
};
</script>

<style>
</style>