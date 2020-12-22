<template>
    <!-- 食谱卡片 -->
    <div class="card recipe-card">
        <img :src="recipe.picture" class="card-img-top" />
        <div class="card-body">
            <h5 class="card-title">{{ recipe.name }}</h5>
            <p class="card-text">
                <strong>成分:</strong>
                {{ recipe.ingredients }}
            </p>
            <div class="action-buttons">
                <nuxt-link :to="`/recipes/${recipe.id}/`" class="btn btn-sm btn-success">查看</nuxt-link>
                <!-- <nuxt-link :to="`/recipes/${recipe.id}/edit/`" class="btn btn-sm btn-primary">编辑</nuxt-link>
                <button @click="onDelete(recipe.id)" class="btn btn-sm btn-danger">删除</button> -->
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ["recipe", "onDelete"]
};
</script>

<style scoped>
.card {
  /* width: 250px; */
  /* display: inline-block; */
  margin: 1rem;
  border-radius: 5px;
  box-shadow: 0 -1px 1px 0 rgba(0, 0, 0, 0.05), 0 1px 2px 0 rgba(0, 0, 0, 0.2);
  transition: all 0.2s ease;
  background: #fff;
  position: relative;
  overflow: hidden;
}

.card-img-top {
  height: 12rem;
  width: 100%;
}

.recipe-card {
  border: none;
  box-shadow: 0 1rem 1.5rem rgba(0, 0, 0, 0.6);
  border-radius: 5px;
}
</style>