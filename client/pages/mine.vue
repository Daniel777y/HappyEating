<template>
    <div>
        <navBar />
        <main class="container" style="margin-top: 65px">

            <div id="show-recipes" class="show-recipes mt-3">
                <div class="container">
                    <div class="row title-row">
                        <div class="col-12 text-right mb-4">
                            <div class="d-flex justify-content-between">
                                <h2>{{ username }}的食谱</h2>
                                <nuxt-link to="/recipes/add" class="btn btn-warning">添加食谱</nuxt-link>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <template v-for="recipe in myrecipes">
                            <div :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
                                <my-recipe-card :onDelete="deleteRecipe" :recipe="recipe"></my-recipe-card>
                            </div>
                        </template>
                    </div>
                </div>
            </div>

            <hr />

            <div id="show-diaries" class="show-diaries mt-3">
                <div class="container">
                    <div class="row title-row">
                        <div class="col-12 text-right mb-4">
                            <div class="d-flex justify-content-between">
                                <h2>{{ username }}的美食日记</h2>
                                <nuxt-link to="/diaries/add" class="btn btn-warning">写美食日记</nuxt-link>
                            </div>
                        </div>
                    </div>

                    <template v-for="diary in mydiaries">
                        <div :key="diary.id" class="row">
                            <my-diary-card :onDelete="deleteDiary" :diary="diary"></my-diary-card>
                        </div>
                    </template>
                </div>

            </div>

        </main>
        <myFooter />
    </div>
</template>

<script>

import axios from 'axios'
import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";
import myDiaryCard from "~/components/myDiaryCard.vue";
import myRecipeCard from "~/components/myRecipeCard.vue";


export default {
    head() {
        return { title: "我的主页 - 欢乐食光" };
    },

    data() {
        return { myrecipes: [], mydiaries: [], username: ''};
    },

    components: { navBar, myFooter, myRecipeCard, myDiaryCard },

    created() {
        try {
            this.username = localStorage.getItem('username');
        } catch (e) {
            console.log(e);
        }
        console.log(this.username);

        try {
            axios.get(`http://localhost:8000/api/recipes/`, {
                params: {
                    username: this.username
                }
            }).then(
                res => {
                    this.myrecipes = res.data;
                }
            );
            axios.get(`http://localhost:8000/api/diaries/`, {
                params: {
                    username: this.username
                }
            }).then(
                res => {
                    this.mydiaries = res.data;
                }
            );
        } catch (e) {
            console.log(e);
            this.myrecipes = [], this.mydiaries = [];
        }
    },

    methods: {
        async deleteRecipe(recipe_id) {
            try {
                if (confirm('确认要删除吗？')) {
                    await this.$axios.$delete(`/api/recipes/${recipe_id}/`);
                    let newRecipes = await this.$axios.$get("/api/recipes/");
                    this.myrecipes = newRecipes;
                }
            } catch (e) {
                console.log(e);
            }
        },

        async deleteDiary(diary_id) {
            try {
                if (confirm('确认要删除吗？')) {
                    await this.$axios.$delete(`/api/diaries/${diary_id}/`);
                    let newDairies = await this.$axios.$get("/api/diaries/");
                    this.mydiaries = newDairies;
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