<template>
    <div>
        <navBar />
        <main>
            <div>
                hhhhhhh
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
        return { title: "编辑日记 - 欢乐食光" };
    },
    components: { navBar, myFooter, },
};
</script>

<style>
</style>