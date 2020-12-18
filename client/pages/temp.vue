<template>
    <main class="login_form">
        <div id="app">
            <div id="login">
                <div id="description">
                    <h1>登录</h1>
                    <p>开始你的美食之旅吧！</p>
                </div>
                <div id="form">
                    <form @submit.prevent="doLogin">
                        <label for="email">Email</label>
                        <input type="text" id="email" v-model="email" placeholder="请输入邮箱" autocomplete="off">

                        <label for="password">Password</label>&nbsp;
                        <!-- <i class="fas" :class="[passwordIcon]" @click="hidePassword = !hidePassword"></i> -->
                        <input type="password" id="password" v-model="password" placeholder="请输入密码">

                        <button type="submit">确认</button>
                    </form>
                </div>
            </div>
        </div>
    </main>
</template>

<script>
    export default {
        data() {
            return {}
        }
    }
</script>

<style scoped>

.login_form {
	background-color: #fff;
	border-radius: 20px;
	margin: auto;
	position: absolute;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;

}

div#app {
  width: 100%;
  height: 100%;
}

div#app div#login {
  align-items: center;
  background-color: #e2e2e5;
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100%;
}

div#app div#login div#description {
  background-color: #ffffff;
  width: 300px;
  padding: 35px;
}

div#app div#login div#description h1,
div#app div#login div#description p {
  margin: 0;
}

div#app div#login div#description p {
  font-size: 0.8em;
  color: #95a5a6;
  margin-top: 10px;
}

div#app div#login div#form {
  background-color: #ff6f1c;
  border-radius: 5px;
  box-shadow: 0px 0px 30px 0px #666;
  color: #ecf0f1;
  width: 350px;
  padding: 35px;
}

div#app div#login div#form label,
div#app div#login div#form input {
  outline: none;
  width: 100%;
}

div#app div#login div#form label {
  color: #95a5a6;
  font-size: 0.8em;
}

div#app div#login div#form input {
  background-color: transparent;
  border: none;
  color: #ecf0f1;
  font-size: 1em;
  margin-bottom: 20px;
}

div#app div#login div#form ::placeholder {
  color: #ecf0f1;
  opacity: 1;
}

div#app div#login div#form button {
  background-color: #ffffff;
  cursor: pointer;
  border: none;
  padding: 10px;
  transition: background-color 0.2s ease-in-out;
  width: 100%;
}

div#app div#login div#form button:hover {
  background-color: #eeeeee;
}

@media screen and (max-width: 600px) {
  div#app div#login {
    align-items: unset;
    background-color: unset;
    display: unset;
    justify-content: unset;
  }

  div#app div#login div#description {
    margin: 0 auto;
    max-width: 350px;
    width: 100%;
  }

  div#app div#login div#form {
    border-radius: unset;
    box-shadow: unset;
    width: 100%;
  }

  div#app div#login div#form form {
    margin: 0 auto;
    max-width: 280px;
    width: 100%;
  }
}

</style>