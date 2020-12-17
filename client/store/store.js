import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex);

export const store = new Vuex.Store({
    state: {
        //token: localStorage.getItem('access_token') || null,
        //refresh_token: localStorage.getItem('refresh_token') || null,
        user_name: null,
    },
})