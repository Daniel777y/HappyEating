<template>
    <!-- 食品详情展示页面 -->
    <div>
        <navBar />
        <main class="container my-5">
            <div class="row">
                <div class="col-12 text-center my-3">
                    <h2 class="mb-3 display-4 text-uppercase">{{ food.name }}</h2>
                </div>
                <div class="col-md-6">
                    <div class="recipe-details">
                        <h4>食品介绍</h4>
                        <p>{{ food.simple_intro }}</p>
                        <h4>食品类型</h4>
                        <p>{{ food.food_type }}</p>
                        <h4>营养成分</h4>
                        <table class="table table-bordered">
                            <tbody>
                                <tr>
                                    <td>卡路里</td>
                                    <td>{{ food.calorie }} 千焦(kJ)/100克(g)</td>
                                </tr>
                                <tr>
                                    <td>碳水化合物</td>
                                    <td>{{ food.carbohydrate }} 克(g)/100克(g)</td>
                                </tr>
                                <tr>
                                    <td>脂肪</td>
                                    <td>{{ food.fat }} 克(g)/100克(g)</td>
                                </tr>
                                <tr>
                                    <td>蛋白质</td>
                                    <td>{{ food.protein }} 克(g)/100克(g)</td>
                                </tr>
                                <tr>
                                    <td>纤维素</td>
                                    <td>{{ food.cellulose }} 毫克(mg)/100克(g)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="col-md-6 mb-4">
                    <img
                        class="img-fluid"
                        style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
                        :src="food.picture"
                        alt
                    >
                </div>
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
        return { title: "食物详情 - 欢乐食光" };
    },

    components: { navBar, myFooter, },

    data() {
        return {
            food: {
                name: "",
                simple_intro: "",
                food_type: "",
                calorie: "",
                carbohydrate: "",
                fat: "",
                protein: "",
                cellulose: "",
                picture: "",
            }
        };
    },

    async asyncData({ $axios, params }) {
        try {
            let food = await $axios.$get(`/api/foods/${params.id}`);
            return { food };
        } catch (e) {
            return { food: [] };
        }
    },
};
</script>

<style>
</style>