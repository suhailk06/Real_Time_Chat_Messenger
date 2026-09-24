# DOT CHAT || Real-Time Chat Messenger

A Django-based real-time chat platform with user authentication, 
friend management, profiles, and instant messaging.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## About

DOT CHAT is a full-stack real-time chat application built with Django. 
It supports secure user authentication, friend management, user profiles, 
and real-time messaging between users.

The project uses PostgreSQL for data storage with dedicated models for 
users, messages, and friendships. Email verification is handled via Gmail 
SMTP, and the responsive frontend is built with HTML, CSS, and JavaScript, 
integrated with the Django backend.

## Features

- Secure user authentication with email verification (Gmail SMTP)
- Friend management — send, accept, and manage friend requests
- Real-time messaging between friends
- User profiles with customizable details
- PostgreSQL database with models for users, messages, and friendships
- Responsive frontend built with HTML, CSS, and JavaScript
- Session-based authentication and password security

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django (Python)
- **Database:** PostgreSQL

## Screenshots

### Index Page
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/8f330321-47fa-4393-9924-c84c3fd4e53d" />

### Login Page
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/c64ca3ea-7188-4295-9dd6-cda4e8ff71ba" />

### Register Page
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e5fc3c31-5437-48b6-811b-555909c5d980" />

### Email Verification
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/474018ab-d81a-46c0-b65e-29e367440249" />

### Home Page
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/39622b0b-9dfe-49b8-95e6-db839d4dd78c" />

### User Profile
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/a6c8819a-54f4-4acd-93c2-158d7facb34c" />

### Friend Requests
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/a616b06a-30f5-4fa1-a455-dd0fcf274796" />

### Real-Time Chat
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/e3fc9f9d-c61e-4de1-96fd-b9566afba81e" />

### Friends List
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/dcb6ed6a-81e9-4c11-9783-92627684d235" />


## Installation

### Prerequisites

- Python
- PostgreSQL
- Git

### Steps

**1. Clone the repository:**

    git clone https://github.com/suhailk06/Real_Time_Chat_Messenger.git
    cd Real_Time_Chat_Messenger/dot_chat

**2. Create and activate a virtual environment:**

    python -m venv venv

    # Windows
    venv\Scripts\activate

    # macOS / Linux
    source venv/bin/activate

**3. Install dependencies:**

    pip install -r requirements.txt

**4. Configure the database** in `settings.py` with your PostgreSQL credentials.

**5. Apply migrations:**

    python manage.py migrate

**6. Run the development server:**

    python manage.py runserver

**7. Open in your browser:** http://127.0.0.1:8000/

## Usage

1. Register a new account and verify your email.
2. Log in and complete your profile.
3. Search for users and send friend requests.
4. Once accepted, start chatting in real time.

## Contributing

1. Fork the repo
2. Create a branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push (`git push origin feature/amazing`)
5. Open a Pull Request

