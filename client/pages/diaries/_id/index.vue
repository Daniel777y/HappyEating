<template>
    <!-- 某篇日记展示 -->
    <div>
        <navBar />
        <main class="container my-5">
            <div class="row">
                <div class="col-12 text-center my-3">
                    <h2 class="mb-3 display-4 text-uppercase">{{ diary.title }}</h2>
                </div>
            </div>
            <div class="row">
                <v-card-text v-html="diary.article_content" class="markdown-body">
                </v-card-text>
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
        return { title: "美食日记 - 欢乐食光" };
    },

    components: { navBar, myFooter, },

    data() {
        return {
            diary: {
                title: "",
                introduction: "",
                picture: "",
                article_content: "",
            },
        }
    },

    async asyncData({ $axios, params }) {
        try {
            let diary = await $axios.$get(`/api/diaries/${params.id}`);
            console.log(diary);
            return { diary };
        } catch (e) {
            return { diary: [] };
        }
    },
};
</script>

<style>
</style>