<template>
    <div>
        <navBar />
        <main>
            <div>
                关于页面
            </div>
        </main>
        <myFooter />
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";

export default {
    head() {
        return { title: "关于 - 欢乐食光" };
    },
    components: { navBar, myFooter, },
};
</script>

<style>
</style>