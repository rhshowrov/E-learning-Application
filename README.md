# E-Learning Platform

This project is a Django-based e-learning application designed for educational institutions, providing distinct features for students and teachers. The application supports features like course materials, assignments, quizzes, and a question-and-answer section, all in a structured environment using both raw CSS and Tailwind CSS for styling.

## Features

### User Roles
- **Student**: Access course materials, submit assignments, take quizzes, and view results.
- **Teacher**: Upload and manage course materials, assignments, and quizzes, and evaluate student performance.

### Core Functionality
- **Class Material**: Teachers can upload materials for their courses, which students can view and download.
- **Assignments**: Teachers can create and upload assignments for students. Students can:
  - Submit assignments.
  - View submission status (late or on-time).
  - See assignment deadlines and track submission history.
- **Quiz Section**: Teachers can create quizzes, and students can:
  - Take quizzes.
  - View quiz results upon submission.

### Same-Role Views
- Students only view the Student dashboard, while Teachers only view the Teacher dashboard.

### Question and Answer Section
- A space where students can post questions and engage with teachers for clarifications.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, Raw CSS, Tailwind CSS for styling
- **Database**: SQLite 
- **Template Engine**: Django Templates
- **python pacakge**: formify for form

