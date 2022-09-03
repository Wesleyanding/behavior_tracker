
# Student Behavior Tracker

## Project Overview
Teachers have long used hard copy methods for documenting student behaviors that affect student learning. This leads to difficulty in understanding the data and takes time most teachers could spend on other tasks. This tracker will greatly speed up the process of tracking a documenting problem behaviors. This aims to aid in the discussion around what and where bad behaviors occur as well as provide documentation for further interventions.


## Functionality
- Quickly track student behaviors and interventions
    - Quick access to students (potentially cards with photos)
    - Tracks behaviors that affect academics
    - Tracks behaviors that may harm others or self
    - Tracks where that behavior occurred (gym, classroom, cafeteria, recess)
    - Tracks interventions that were performed 
    - additional comments
- Secure login 
    - potentially a parent access for their student
- Potentially a connection with various Student Information Systems (SIS) for easier access to rosters etc. 

#### Libraries:
- Django
- JavaScript

## Data Model

#### Teacher
    - Name
    - Classes (ManytoManyField)
    - Students (ForeignKey)
    - Admin

#### Student
    - Id
    - Name
    - Grade
    - Classes (ManytoMany)
    - Photo (potentially)
    - contact information
    - Behaviors (ForeignKey)

#### Behaviors
    - Date and time
    - behavior
    - interventions
    - Location

## Schedule
- Week 1 - Start working on backend 
    - [ ] Create models
        - [ ] Teacher
        - [ ] Student
        - [ ] Behaviors
    - [ ] Look into connecting with SIS
- Week 2 - Start working on frontend
    - [ ] Login page
    - [ ] Logout page
    - [ ] Teacher page
        - [ ] Classes
        - [ ] Students
    - [ ] Student page
        - [ ] Behaviors
    - [ ] Create dummy data
    - [ ] Create a student page
    - [ ] Create a teacher page
- Week 3 - Work on styling
    - [ ] Create overall theme
        - [ ] Mobile focused first
    - [ ] Work through a user flow for bugs
        - [ ] Fix any bugs
    - [ ] Have a presentation ready project
- Week 4 - Work on last minute bug fixes and styling. 
    - [ ] Have some of my teacher friends work through a user flow. 

- Week 5 and going forward
 - Work on having an a parent access to their student. 
 - Ability to contact teacher
 - Chat functions for parent/teacher interactions (Stored in database)
 - continue working on connections with SIS


