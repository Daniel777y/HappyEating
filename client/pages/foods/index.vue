<template>
    <div>
        <navBar />
        <body>
            <div>
                食物介绍
            </div>
        </body>
        <myFooter />
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";

export default {
    head() {
        return { title: "食物介绍 - 欢乐食光" };
    },
    components: {
        navBar,
        myFooter,
    },
};
</script>

<style>
</style>