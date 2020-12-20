<template>
    <div>
        <navBar />
        <main class="container" style="margin-top: 65px">
            <div class="row">
                <div class="col-12 text-right mb-4">
                    <div class="d-flex justify-content-between">
                        <h3>美食食谱</h3>
                    </div>
                </div>
                <template v-for="recipe in recipes">
                    <div :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
                        <recipe-card :onDelete="deleteRecipe" :recipe="recipe"></recipe-card>
                    </div>
                </template>
            </div>
        </main>
        <myFooter />
    </div>
</template>
  
<script>
import RecipeCard from "~/components/RecipeCard.vue";
import myFooter from "~/components/myFooter.vue";
import navBar from "~/components/navbar.vue";

export default {
    head() {
        return { title: "食谱列表 - 欢乐食光" };
    },
    components: { RecipeCard, navBar, myFooter },

    async asyncData({ $axios, params }) {
        try {
            let recipes = await $axios.$get(`/api/recipes/`);
            return { recipes };
        } catch (e) {
            return { recipes: [] };
        }
    },
    data() {
        return { recipes: [] };
    },
    methods: {
        async deleteRecipe(recipe_id) {
            try {
                if (confirm('确认要删除吗？')) {
                    await this.$axios.$delete(`/recipes/${recipe_id}/`);
                    let newRecipes = await this.$axios.$get("/recipes/");
                    this.recipes = newRecipes;
                    location.reload()
                    this.$router.go(0)
                }
            } catch (e) {
                console.log(e);
            }
        }
    }
};
</script>
  
<style scoped>
</style>