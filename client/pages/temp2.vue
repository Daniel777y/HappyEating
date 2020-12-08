<template>
    <div>
        <navBar />
            <body>
                <div class="mt-5">
                    <div class="container">
                        <div class="row">
                            <div class="col-lg-8 col-md-10 mx-auto">
                                <hr>
                                <div class="post-preview">
                                <a href="post.html">
                                    <h2 class="post-title">
                                    Science has not yet mastered prophecy
                                    </h2>
                                    <h3 class="post-subtitle">
                                    We predict too much for the next year and yet far too little for the next ten.
                                    </h3>
                                </a>
                                <p class="post-meta">
                                    on August 24, 2019</p>
                                </div>
                                <hr>
                            </div>
                        </div>
                    </div>
                </div>
            </body>
        <myFooter />
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";
import FoodCard from '~/components/FoodCard.vue';
import RecipeCard from "~/components/RecipeCard.vue";

const sampleData = 
[
    {
        id: 1,
        name: "日记1",
        introduction: "日记摘要1",
        picture: "/images/food-1.jpeg",
    },
];

export default {

    head() {
        return { title: "临时2 - 欢乐食光" };
    },
    asyncData(context) {
        let data = sampleData;
        return {
            foods: data
        };
    },
    data() {
        return { foods: [] };
    },
    components: {
        navBar,
        myFooter,
        RecipeCard,
        FoodCard,
    },
    props: ["food"],
};
</script>

<style scoped>
.post-preview > a {
  color: #555555;
}

.post-preview > a:focus, .post-preview > a:hover {
  text-decoration: none;
  color: #00aeff;
}

.post-preview > a > .post-title {
  font-size: 30px;
  margin-top: 30px;
  margin-bottom: 10px;
}

.post-preview > a > .post-subtitle {
  font-weight: 300;
  margin: 0 0 10px;
}

.post-preview > .post-meta {
  font-size: 18px;
  font-style: italic;
  margin-top: 0;
  color: #555555;
}

.post-preview > .post-meta > a {
  text-decoration: none;
  color: #555555;
}

.post-preview > .post-meta > a:focus, .post-preview > .post-meta > a:hover {
  text-decoration: underline;
  color: #00aeff;
}

@media only screen and (min-width: 768px) {
  .post-preview > a > .post-title {
    font-size: 36px;
  }
}

</style>