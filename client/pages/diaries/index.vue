<template>
    <div>
        <navBar />
        <main class="container" style="margin-top: 65px">
            <div class="row">
                <div class="col-12 text-right mb-4">
                    <div class="d-flex justify-content-between">
                        <h3>美食日记</h3>
                    </div>
                </div>
            </div>
            <template v-for="diary in diaries">
                <div :key="diary.id" class="row">
                    <diary-card :diary="diary"></diary-card>
                </div>
            </template>
        </main>
        <myFooter />
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";
import DiaryCard from "~/components/DiaryCard.vue"

const diaryData = [
    {
        "id": 1,
        "title": "This is title",
        "introduction": "This is introductiion.",
        "create_time": "2020-12-14T22:18:47.547616",
        "picture": "/images/food-1.jpeg",
    },

    {
        "id": 1,
        "title": "This is title",
        "introduction": "This is introductiion.",
        "create_time": "2020-12-14T22:18:47.547616",
        "picture": "/images/food-1.jpeg",
    },

    {
        "id": 1,
        "title": "This is title",
        "introduction": "This is introductiion.",
        "create_time": "2020-12-14T22:18:47.547616",
        "picture": "/images/food-1.jpeg",
    }
]

export default {
    head() {
        return { title: "美食日记 - 欢乐食光" };
    },
    components: { navBar, myFooter, DiaryCard },
    async asyncData({ $axios, params }) {
        try {
            let diaries = await $axios.$get(`/api/diaries/`);
            return { diaries };
        } catch (e) {
            console.log(e);
            return { diaries: [] };
        }
    },
    data() {
        return { diaries: [] };
    },
};
</script>

<style>
</style>