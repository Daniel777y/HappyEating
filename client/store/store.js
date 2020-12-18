import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex);

const state = {
    access_token: null,
    refresh_token: null,
    username: null,
}

export default new Vuex.Store({
    state,
});
