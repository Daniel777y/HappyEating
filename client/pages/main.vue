<template>
    <div>
        <navBar />
        <main class="container">
            <div class="my-carousel" id="my-carousel" style="margin-top: 65px">
                <div class="container">
                    <carousel />
                </div>
            </div>

            <div id="show-recipes" class="show-recipes mt-3">
                <div class="container">
                    <div class="row title-row">
                        <div class="col section-title">
                            <h2>最新食谱</h2>
                        </div>
                        <div class="col show-more">
                            <p>show more</p>
                        </div>
                    </div>
                    <div class="row">
                        <template v-for="recipe in recipes">
                            <div :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
                                <recipe-card :onDelete="deleteRecipe" :recipe="recipe"></recipe-card>
                            </div>
                        </template>
                    </div>
                </div>
            </div>

            <hr />

            <div id="show-diaries" class="show-diaries mt-3">
                <div class="container">
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

            </div>

            <hr />

            <div id="show-foods" class="show-foods mt-3">
                <div class="container">
                    <div class="row title-row">
                        <div class="col section-title">
                            <h2>食物知多少</h2>
                        </div>
                        <div class="col show-more">
                            <p>show more</p>
                        </div>
                    </div>
                    <div class="row">
                        <template v-for="food in foods">
                            <div :key="food.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
                                <food-card :food="food"> </food-card>
                            </div>
                        </template>
                    </div>
                </div>
            </div>

            <div class="dist-footer mb-5"></div>

        </main>
        <myFooter />
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";
import carousel from '~/components/carousel.vue';

const diaryData = [
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
        return { title: "首页 - 欢乐食光" };
    },
    components: {
        navBar,
        myFooter,
        carousel,
    },

    async asyncData({ $axios, params }) {
        try {
            let diaries = diaryData
            let recipes = await $axios.$get(`/recipes/`);
            let foods = foodData
            return { recipes, diaries, foods };
        } catch (e) {
            console.log(e);
            return { recipes: [], diaries: [], foods: [] };
        }
    },
    data() {
        return { recipes: [], diaries: [], foods: [] };
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


<style scoped>

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