<template>
    <!-- 食品总页 -->
    <div>
        <navBar />
        <main class="container" style="margin-top: 65px">
            <div class="row">
                <div class="col-12 text-right mb-4">
                    <div class="d-flex justify-content-between">
                        <h3>食物知多少</h3>
                    </div>
                </div>
                <template v-for="food in foods">
                    <div :key="food.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
                        <food-card :food="food"> </food-card>
                    </div>
                </template>
            </div>
        </main>
        <myFooter />
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";
import FoodCard from "~/components/FoodCard.vue";

const foodData = 
[
    {
        id: 1,
        name: "日记1",
        introduction: "日记摘要1",
        picture: "/images/food-1.jpeg",
    },
    {
        id: 1,
        name: "日记1",
        introduction: "日记摘要1",
        picture: "/images/food-1.jpeg",
    },
    {
        id: 1,
        name: "日记1",
        introduction: "日记摘要1",
        picture: "/images/food-1.jpeg",
    },
    {
        id: 1,
        name: "日记1",
        introduction: "日记摘要1",
        picture: "/images/food-1.jpeg",
    },
];

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