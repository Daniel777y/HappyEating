<template>
    <!-- 图片轮播 -->
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
            <!-- 核心内容 -->
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

export default {
    data() {
        return {
            slide: 0,
            sliding: null,
            sampleData
        }
    },

    // 从后台获取数据
    async asyncData({ $axios, params }) {
        try {
            let slideData = await $axios.$get(`/api/slides/`);
            return { slideData };
        } catch (e) {
            console.log(e);
            return { slideData: [] };
        }
    },
    // 点击变化
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