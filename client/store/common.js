const state = {
    access_token: '',
    refresh_token: '',
    username: '',
}

export default {
    state,

    setState(access_token, refresh_token, username) {
        this.access_token = access_token;
        this.refresh_token = refresh_token;
        this.username = username;
    },

    clearState() {
        this.access_token = '';
        this.refresh_token = '';
        this.username = '';
    }
}