<template>
    <div>
        <navBar />
        <main class="container">
            <div id="myCarousel">
                <carousel />
            </div>
            <div id="topRecipes">
            </div>
            <div id="topDiaries">
            <hr/>
            </div>
            <div id="topFoods">
            </div>
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
    components: {
        navBar,
        myFooter,
        carousel,
    },
};

</script>

<style>
#myCarousel {
    position: relative;
    top: 80px;
    margin: auto;
}
#topRecipes {
    position: relative;
    top: 80px;
    margin: auto;
}
#topDiaries {
    position: relative;
    top: 80px;
    margin: auto;
}
#topFoods {
    position: relative;
    top: 80px;
    margin: auto;
    text-align: center;
    bottom: 300px;
}
</style>