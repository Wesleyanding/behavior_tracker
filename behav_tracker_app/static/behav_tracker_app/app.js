const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            teachers: [],
            students: [],
            selectedStudent: null,
            currentStudent: []
        }
    },
    methods: {
        fetchStudents: function() {
            fetch(`/student/${this.selectedStudent}`)
            .then(response => response.json())
            .then(data => {
                this.students = data.data
                this.openForm()
            })
        },
        openForm: function() {
            document.getElementById('myForm').style.display = 'block'
        },
        viewStudents: function () {
            fetch('/viewStudents')
            .then(response => response.json())
            .then(data => {
                this.students = data
            })
        },
        // finish student info
        studentInfo: function () {
            fetch('/')
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
        this.viewStudents()
    }
}).mount('#app')