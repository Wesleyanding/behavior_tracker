const app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            teachers: [],
            students: [],
            selectedStudent: null,
            currentStudent: [],
            behaviors: [],
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
            student_id = document.querySelector('#student_id').value
            fetch(`/studentinfo/${student_id}`)
            .then(response => response.json())
            .then(data => {
                this.behaviors = data.data
                console.log(data)
            })
        }
    },

    created: function() {
        fetch('/teachers')
        .then(response => response.json())
        .then(data => {
            // data is not showing data in console so it should be like below
            this.teachers = data
            console.log(data)
        }),
        this.studentInfo()
    }, 
    mounted: function () {
        this.viewStudents()
    }
}).mount('#app')