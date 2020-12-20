<template>
    <div>
        <navBar />
        <main class="container">
            <form @submit.prevent="submitRecipe">
                <div class="form-group">
                    <label for>标题</label>
                    <input type="text" class="form-control" v-model="diary.title">
                </div>
                <div class="form-group">
                    <label for>一句话介绍一下你的日记吧</label>
                    <input v-model="diary.introduction" type="text" class="form-control">
                </div>
                <div class="form-group">
                    <label for>封面</label>
                    <input type="file" name="file" @change="onFileChange">
                </div>
                <div class="mavonEditor">
                    <no-ssr>
                        <mavon-editor class="mavonEditor" :toolbars="markdownOption" @change="mdChange" />
                    </no-ssr>
                </div>
                <button type="submit" class="btn btn-primary">提交</button>
            </form>
        </main>
    </div>
</template>

<script>

import navBar from "~/components/navbar.vue";
import myFooter from "~/components/myFooter.vue";
import MyFooter from '../../components/myFooter.vue';

export default {
    head() {
        return { title: "添加日记 - 欢乐食光" };
    },

    components: { navBar, myFooter, },

    data() {
        return {
            markdownOption:{
                bold: true, // 粗体
                italic: true, // 斜体
                header: true, // 标题
                underline: true, // 下划线
                strikethrough: true, // 中划线
                mark: true, // 标记
                superscript: true, // 上角标
                subscript: true, // 下角标
                quote: true, // 引用
                ol: true, // 有序列表
                ul: true, // 无序列表
                link: true, // 连接
                imagelink: true, // 图片连接
                code: true, // code
                table: true, // 表格
                fullscreen: false, // 全屏编辑
                readmodel: false, // 沉浸式阅读
                htmlcode: true, // 展现html源码
                help: true, // 帮助
                undo: true, // 上一步
                redo: true, // 下一步
                trash: true, // 清空
                save: true, // 保存（触发events中的save事件）
                navigation: true, // 导航目录
                alignleft: true, // 左对齐
                aligncenter: true, // 居中
                alignright: true, // 右对齐
                subfield: true, // 单双栏模式
                preview: true, // 预览
            },
            diary: {
                title: "",
                introduction: "",
                picture: "",
                article_content: "",
            },
            preview: "",
            owner: "",
        }
    },
    mounted() {
        this.owner = localStorage.getItem('username');
    },
    methods: {
        mdChange(value, render) {
            this.html = render;
            this.diary.article_content = render;
        },
        onFileChange(e) {
            let files = e.target.files || e.dataTransfer.files;
            if (!files.length) {
                return;
            }
            this.diary.picture = files[0];
            this.createImage(files[0]);
        },
        createImage(file) {
            let reader = new FileReader();
            let vm = this;
            reader.onload = e => {
                vm.preview = e.target.result;
            };
            reader.readAsDataURL(file);
        },
        async submitRecipe() {
            const config = {
                headers: { "content-type": "multipart/form-data" }
            };
            this.diary.owner = this.owner;
            console.log(this.diary);
            let formData = new FormData();
            for (let data in this.diary) {
                console.log(data);
                formData.append(data, this.diary[data]);
            }
            console.log(formData);
            try {
                let response = await this.$axios.$post("/api/diaries/", formData, config);
                this.$router.push("/diaries/");
            } catch (e) {
                let code = e.response.status;
                if (code == 400) {
                    alert('请将信息填写完整！')
                }
                console.log(e.response);
            }
        }
    }
};
</script>

<style scoped>
.container {
    margin-top: 65px;
    margin-bottom: 65px;
}
.mavonEditor {
    margin-bottom: 20px;
    height: 600px;
}
</style>