<template>
    <div>
        <navBar />
        <main class="container">
            <div class="my-carousel mt-5" id="my-carousel">
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

            <div id="show-diaries" class="show-diaries">
                <div class="row title-row">
                    <div class="col section-title">
                        <h2>最新美食日记</h2>
                    </div>
                    <div class="col show-more">
                        <p>show more</p>
                    </div>

                    <div class="row">
                        <div class="col-md-6 d-flex align-items-stretch">
                            <div class="card" style='background-image: url("https://cdn.acwing.com/media/user/profile/photo/5400_lg_6904153088.jpg");'>
                                <div class="card-body">
                                    <h5 class="card-title"><a href="">Our Mission</a></h5>
                                    <p class="card-text">Lorem ipsum dolor sit amet, consectetur elit, sed do eiusmod tempor ut labore et dolore magna aliqua.</p>
                                    <div class="read-more"><a href="#"><i class="icofont-arrow-right"></i> Read More</a></div>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-6 d-flex align-items-stretch mt-4 mt-md-0">
                            <div class="card" style='background-image: url("https://cdn.acwing.com/media/user/profile/photo/5400_lg_6904153088.jpg");'>
                                <div class="card-body">
                                    <h5 class="card-title"><a href="">Our Plan</a></h5>
                                    <p class="card-text">Sed ut perspiciatis unde omnis iste natus error sit voluptatem doloremque laudantium, totam rem.</p>
                                    <div class="read-more"><a href="#"><i class="icofont-arrow-right"></i> Read More</a></div>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-6 d-flex align-items-stretch mt-4">
                            <div class="card" style='background-image: url("https://cdn.acwing.com/media/user/profile/photo/5400_lg_6904153088.jpg");'>
                                <div class="card-body">
                                    <h5 class="card-title"><a href="">Our Vision</a></h5>
                                    <p class="card-text">Nemo enim ipsam voluptatem quia voluptas sit aut odit aut fugit, sed quia magni dolores.</p>
                                    <div class="read-more"><a href="#"><i class="icofont-arrow-right"></i> Read More</a></div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 d-flex align-items-stretch mt-4">
                            <div class="card" style='background-image: url("https://cdn.acwing.com/media/user/profile/photo/5400_lg_6904153088.jpg");'>
                                <div class="card-body">
                                    <h5 class="card-title"><a href="">Our Care</a></h5>
                                    <p class="card-text">Nostrum eum sed et autem dolorum perspiciatis. Magni porro quisquam laudantium voluptatem.</p>
                                    <div class="read-more"><a href="#"><i class="icofont-arrow-right"></i> Read More</a></div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <hr />

            <div id="show-foods" class="show-foods">
                <div class="row title-row">
                    <div class="col section-title">
                        <h2>食物知多少</h2>
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

            <div class="dist-footer mb-5"></div>

        </main>
        <myFooter />
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";
import carousel from '~/components/carousel.vue';
import RecipeCard from "~/components/RecipeCard.vue";

export default {
    head() {
        return { title: "首页 - 欢乐食光" };
    },
    components: {
        navBar,
        myFooter,
        carousel,
        RecipeCard,
    },

    async asyncData({ $axios, params }) {
        try {
            let recipes = await $axios.$get(`/recipes/`);
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

.show-diaries .card {
  border: 0;
  padding: 160px 20px 20px 20px;
  position: relative;
  width: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
}

.show-diaries .card-body {
  z-index: 10;
  background: rgba(255, 255, 255, 0.9);
  padding: 15px 30px;
  box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.1);
  transition: 0.3s;
  transition: ease-in-out 0.4s;
  border-radius: 5px;
}

.show-diaries .card-title {
  font-weight: 700;
  text-align: center;
  margin-bottom: 15px;
}

.show-diaries .card-title a {
  color: #150517;
}

.show-diaries .card-text {
  color: #5e5e5e;
}

.show-diaries .read-more a {
  color: #777777;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 12px;
  transition: 0.4s;
}

.show-diaries .read-more a:hover {
  text-decoration: underline;
}

.show-diaries .card:hover .card-body {
  background: #ff7f5d;
}

.show-diaries .card:hover .read-more a, .show-diaries .card:hover .card-title, .show-diaries .card:hover .card-title a, .show-diaries .card:hover .card-text {
  color: #fff;
}

</style>