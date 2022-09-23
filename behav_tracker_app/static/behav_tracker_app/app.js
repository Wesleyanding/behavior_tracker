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
        closeForm: function() {
            document.getElementById('myForm').style.display = 'none'
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
            if(document.querySelector('#student_id')){
                student_id = document.querySelector('#student_id').value
                fetch(`/studentinfo/${student_id}`)
                .then(response => response.json())
                .then(data => {
                    this.behaviors = data
                })}
        }
    },

    created: function() {
        fetch('/teachers')
        .then(response => response.json())
        .then(data => {
            // data is not showing data in console so it should be like below
            this.teachers = data
        })
            var elems = document.querySelectorAll('select');
            var instances = M.FormSelect.init(elems, {dropdownOptions:{}});
          
    }, 
    mounted: function () {
        this.viewStudents(),
        this.studentInfo()
    }
}).mount('#app')