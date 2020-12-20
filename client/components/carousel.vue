<template>
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
            <template v-for="slide in sampleData">
                <b-carousel-slide
                    :key="slide.id"
                    :caption="slide.content"
                    :img-src="slide.picture"
                ></b-carousel-slide>
            </template>

        </b-carousel>
    </div>
</template>

<script>
const sampleData = 
[
    {
        id: 1,
        content: "First slide",
        picture: "https://picsum.photos/1024/480/?image=52",
    },
    {
        id: 2,
        content: "Second slide",
        picture: "https://picsum.photos/1024/480/?image=54",
    },
    {
        id: 3,
        content: "Third slide",
        picture: "https://picsum.photos/1024/480/?image=58",
    },
    {
        id: 4,
        content: "Forth slide",
        picture: "https://picsum.photos/1024/480/?image=55",
    },
];

export default {
    data() {
        return {
            slide: 0,
            sliding: null,
            sampleData
        }
    },
    async asyncData({ $axios, params }) {
        try {
            let slideData = await $axios.$get(`/api/slides/`);
            return { slideData };
        } catch (e) {
            console.log(e);
            return { slideData: [] };
        }
    },
    methods: {
        onSlideStart(slide) {
            this.sliding = true
        },
        onSlideEnd(slide) {
            this.sliding = false
        }
    }
}
</script>

<style>
</style>