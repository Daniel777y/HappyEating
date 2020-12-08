<template>
    <div>
        <navBar />
        <main class="container mt-5">
            
            <div id="show-diaries" class="show-diaries">
                <div class="row title-row">
                    <div class="col section-title">
                        <h2>最新美食日记</h2>
                    </div>
                    <div class="col show-more">
                        <p>show more</p>
                    </div>
                </div>
                <template v-for="diary in diaries">
                    <div :key="diary.id" class="row">
                        <diary-card :diary="diary"></diary-card>
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
import carousel from '~/components/carousel.vue';
import RecipeCard from "~/components/RecipeCard.vue";
import DiaryCard from "~/components/DiaryCard.vue";

const diarydata = [
    {
        id: 1,
        title: "This is title",
        introduction: "This is introductiion.",
        dateAndTime: "2020 12 7",
        picture: "/images/food-1.jpeg",
    },

    {
        id: 1,
        title: "This is title",
        introduction: "This is introductiion.",
        dateAndTime: "2020 12 7",
        picture: "/images/food-1.jpeg",
    },

    {
        id: 1,
        title: "This is title",
        introduction: "This is introductiion.",
        dateAndTime: "2020 12 7",
        picture: "/images/food-1.jpeg",
    }
]

export default {
    head() {
        return { title: "首页 - 欢乐食光" };
    },
    components: {
        navBar,
        myFooter,
        carousel,
        RecipeCard,
        DiaryCard,
    },

    async asyncData({ $axios, params }) {
        try {
            let diaries = diarydata
            return { diaries };
        } catch (e) {
            return { diaries: [] };
        }
    },
    data() {
        return { diaries: [] };
    },
    methods: {
        async deleteRecipe(recipe_id) {
            try {
                if (confirm('确认要删除吗？')) {
                    await this.$axios.$delete(`/recipes/${recipe_id}/`);
                    let newRecipes = await this.$axios.$get("/recipes/");
                    this.recipes = newRecipes;
                }
            } catch (e) {
                console.log(e);
            }
        }
    }
};

</script>


<style>

.show-recipes {
    padding-top: 15px;
}

.section-title {
    text-align: left;
    height: 60px;
    padding-bottom: 5px;
}

.section-title h2 {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 20px;
    padding-bottom: 20px;
    position: relative;
}

.section-title h2::after {
    content: '';
    display: block;
    width: 50px;
    height: 3px;
    background: #ff7f5d;
    bottom: 0;
    left: calc(50% - 25px);
}

.section-title p {
    margin-bottom: 0;
    color: #919191;
    font-size: 14px;
}

</style>