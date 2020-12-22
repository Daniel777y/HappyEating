<template>
    <!-- 日记卡片模块 -->
    <b-card class="diary-card w-100" :img-src="diary.picture" img-right>
        <div>
            <div class="post-preview">
                <nuxt-link :to="`/diaries/${diary.id}/`">
                    <h2 class="post-title">
                        {{ diary.title }}
                    </h2>
                    <h3 class="post-subtitle">
                        {{ diary.introduction }}
                    </h3>
                </nuxt-link>
                <p class="post-meta">
                    {{ dateFormat(diary.create_time) }}
                </p>
            </div>
        </div>
    </b-card>
</template>

<script>

export default {
    props: ["diary"],
    methods : {

        // 将后台传入的时间格式化
        dateFormat:function(time) {
            var date = new Date(time);
            var year = date.getFullYear();
            var month = date.getMonth()+1<10 ? "0"+(date.getMonth()+1) : date.getMonth()+1;
            var day = date.getDate()<10 ? "0"+date.getDate() : date.getDate();
            var hours = date.getHours()<10 ? "0"+date.getHours() : date.getHours();
            var minutes = date.getMinutes()<10 ? "0"+date.getMinutes() : date.getMinutes();
            var seconds = date.getSeconds()<10 ? "0"+date.getSeconds() : date.getSeconds();
            // 拼接
            return year+"-"+month+"-"+day+" "+hours+":"+minutes+":"+seconds;
        }
    }
};
</script>

<style scoped>
.diary-card {
    border: 0;
    padding: 20px 20px 20px 20px;
    position: relative;
    height: 20rem;
    width: 100%;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
}

.diary-card img {
    width: 30rem;
}

.card-body {
    z-index: 10;
    background: rgba(255, 255, 255, 0.9);
    padding: 15px 30px;
    box-shadow: 0px 2px 15px rgba(0, 0, 0, 0.1);
    transition: 0.3s;
    transition: ease-in-out 0.4s;
    border-radius: 5px;
}

.card-title {
    font-weight: 700;
    text-align: center;
    margin-bottom: 15px;
}

.card-title a {
    color: #150517;
}

.card-text {
    color: #5e5e5e;
}

.read-more a {
    color: #777777;
    text-transform: uppercase;
    font-weight: 600;
    font-size: 12px;
    transition: 0.4s;
}

.read-more a:hover {
    text-decoration: underline;
}

.card:hover .card-body {
    background: #ffc400;
}

.card:hover .read-more a, .show-diaries .card:hover .card-title, .show-diaries .card:hover .card-title a, .show-diaries .card:hover .card-text {
    color: #fff;
}

.post-preview > a {
    color: #555555;
}

.post-preview > a:focus, .post-preview > a:hover {
    text-decoration: none;
    color: #ffffff;
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
    color: #ffffff;
}

@media only screen and (min-width: 768px) {
    .post-preview > a > .post-title {
        font-size: 36px;
    }
}
</style>