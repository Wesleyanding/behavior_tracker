const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            teachers: []
        }
    },
    methods: {

        // TODO create a method to bring out the students
        fetchTeachers: function() {
            fetch('/teachers')
            .then(response => response.json())
            .then(data => {
                this.teachers = data.data
            })
        }

    },

    created: function() {
        fetch('/teachers')
        .then(response => response.json())
        .then(data => {
            // data is not showing data in console so it should be like below
            this.teachers = data
            // console.log(data)
        })
    }, 
    mounted: function () {

    }
}).mount('#app')