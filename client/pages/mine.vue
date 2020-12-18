<template>
    <div>
        <navBar />
        <main class="container" style="margin-top: 65px">

        </main>
        <myFooter />
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";
import FoodCard from "~/components/FoodCard.vue";


export default {
    head() {
        return { title: "食物介绍 - 欢乐食光" };
    },
    components: { navBar, myFooter, FoodCard, },
    async asyncData({ $axios, params }) {
        try {
            let foods = await $axios.$get(`/api/foods/`);
            return { foods };
        } catch (e) {
            console.log(e);
            return { foods: [] };
        }
    },
    data() {
        return { foods: [] };
    },
};
</script>

<style>
</style>