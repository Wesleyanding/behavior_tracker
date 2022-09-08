const app = Vue.createApp({
    delimters: ['[[', ']]'],
    data() {
        return {
            teachers: []
        }
    },
    methods: {
        fetchTeachers: function() {
            fetch('/api/teacher')
            .then(response => response.json())
            .then(data => {
                this.teachers = data.data
            })
        }

    },

    created: function() {
        fetch('./api/teacher')
        .then(response => response.json())
        .then(data => {
            this.teachers = data.data
        })
    }, 
    mounted: function () {

    }
}).mount('#app')