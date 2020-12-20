<template>
    <div class="whole">
        <navBar />
        <main class="container">
            <div class="my-carousel" id="my-carousel" style="margin-top: 65px">
                <div class="container">
                    <div id="carousel_con">
                        <b-carousel
                            id="carousel"
                            v-model="slide"
                            :interval="4000"
                            controls
                            indicators
                            background="#ababab"
                            img-width="1024"
                            img-height="480"
                            style="text-shadow: 1px 1px 2px #333;"
                            @sliding-start="onSlideStart"
                            @sliding-end="onSlideEnd"
                        >
                            <template v-for="slide in slideData">
                                <b-carousel-slide
                                    :key="slide.id"
                                    :caption="slide.content"
                                    :img-src="slide.picture"
                                ></b-carousel-slide>
                            </template>
                        </b-carousel>
                    </div>
                </div>
            </div>

            <div id="show-recipes" class="show-recipes mt-3">
                <div class="container">
                    <div class="row title-row">
                        <div class="col section-title">
                            <h2>最新食谱</h2>
                        </div>
                    </div>
                    <div class="row">
                        <template v-for="recipe in recipes">
                            <div :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
                                <recipe-card :recipe="recipe"></recipe-card>
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

export default {
    head() {
        return { title: "首页 - 欢乐食光" };
    },
    components: { navBar, myFooter, carousel, },

    async asyncData({ $axios, params }) {
        try {
            let slideData = await $axios.$get(`/api/slides/`);
            let diaries = await $axios.$get(`/api/diaries/`);
            let recipes = await $axios.$get(`/api/recipes/`);
            let foods = await $axios.$get(`/api/foods/`);
            return { recipes, diaries, foods, slideData };
        } catch (e) {
            console.log(e);
            return { recipes: [], diaries: [], foods: [], slideData: [] };
        }
    },
    data() {
        return { recipes: [], diaries: [], foods: [], slide: 0, sliding: null, };
    },
    methods: {
        onSlideStart(slide) {
            this.sliding = true
        },
        onSlideEnd(slide) {
            this.sliding = false
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
  background: #ffc400;
  bottom: 0;
  left: calc(50% - 25px);
}

.section-title p {
  margin-bottom: 0;
  color: #919191;
  font-size: 14px;
}

</style>