# Humanitas

[Link to the website]()

![An image previewing all devices]()

## Table of Contents

0. [About](#about)
1. [Project Goals](#project-goals)
   1. [User Goals](#user-goals)
2. [User Experience](#user-experience)

   1. [Target Audience](#target-audience)
   2. [User Requirements and Expectations](#user-requirements-and-expectations)
   3. [User Stories](#user-stories)
   4. [Site Owner Stories](#site-owner-stories)

3. [Design](#design)

   1. [Colors](#colours)
   2. [Fonts](#fonts)

4. [Project Structure](#project-structure)

   1. [Web Pages](#web-pages)
   2. [Sections](#sections)
   3. [Code Structure](#code-structure)

5. [Models](#models)

   1. [Data Models](#data-models)

6. [Validation](#validation)
   1. [CSS](#css)
   2. [HTML](#html)
   3. [Python](#python)

# About

- Humanitas is a helping organisation which connects people who needs help to people who can provide help.
- The website is build so that user can book a call with the team and find the right help.
- It also consists of stories written by various people who were helped around the world.

---

## Project Goals

Primary goals of the project (web app):

- Give users  an online platform to connect with a helping organisation
- Enable users to express themselves through a written form i.e. Comment or Stories
- Enable users to book a call and share their problems with the team

### User Goals

- Ability to share their stories
- Be able give an opinion on a topic
- Ability to amend and update content
- Chance to connect with a variety of interesting individuals.
- Able to book an appointment with the team
- Able to change and cancel the appointments

## User Experience

### Target Audience

- People around the world who need help
- Individuals who want to share their stories to the world

### User Requirements and Expectations

- Application with a clear purpose
- An user-friendly interface that allows quick and efficient navigation
- Responsive and visually good design
- Engaging content within the limits of set categories
- Ways to engage with a team or a developer

### User stories

1. As a user I want the navigation to be user-friendly so that I'm able to easily navigate through the app content.
2. As a Site user I want to know info on what the app is about so that I can use its functionality for mutual benefit
3. As a Site user I can be able to login and logout from the website so that I can have a safe environment to work with
4. As a Site User I can be able to send message so that I can communicate with the website owner
5. As a Site User I can view the stories page so that I can view the posts
6. As a Site User I can click a story so that I can read the full post
7. As a Site User I can comment on the story so that I can be involved in conversation
8. As a Site User I can delete comments so that I can delete unwanted comments in my story and also my comments in other's stories
9. As a Site User I can add a story so that I can share my thoughts with different people
10. As a Site User I can edit my story so that I can change the content when I want
11. As a Site User I can be able delete my story so that I can delete my blog when needed
12. As a Site User I can be able to add my profile to the website so that I can interact comfortably
13. As a Site User I can be able to edit and update my profile so that I can change details whenever I want
14. As a Site User I can be able to delete my profile so that I can be sure my data is save when I don't want to use website anymore
15. As a Site User I can book an appointment so that I can communicate with the site owner
16. As a Site User I can edit my appointment so that I can get flexibility in booking
17. As a Site User I can delete my appointment so that I can have decide if I want to cancel the appointment
18. As a Site User I can view my bookings so that I can easily check for my bookings

### Site Owner Stories

19. As a Site Owner I want to restrict access to sections of an app to unauthenticated users so that basic standards of data protection are met
20. As a Site Owner I would like that authenticated users have full access to web app and its functionality
21. As a Site Owner I would like that each data entry is validated before stored in database
22. As a Site Owner I would like that users an leave a message via contact form
23. As a Site Owner I would like that users have more than one way of comunicating with team or myself
24. As a Site Owner I would like that each authenticated user gets prompt messages when performing CRUD(Create,Read,Update,Delete) operations when using web app.
25. As a Site Owner I would like that user can not book an appointment which is already booked

## Design

---

### Colours

Web app is utilizing bootstrap inbuilt dark background and other colors were selected by site owner. It's a self custom design as per wish of Site Owner.

### Fonts

Google fonts "'Playfair', sans-serif" modern and "'Fauna One', sans-serif" font were used for this project as it offers clean and legible design, which makes it easy to read on screens of different sizes and resolutions. It has a neutral appearance and doesn't have any distracting features that can make it difficult to read.

<details><summary>See Playfair</summary>
<img src="documentation/humanitas-pages/playfair.png">
</details>

<details><summary>See Fauna One</summary>
<img src="documentation/humanitas-pages/fauna-one.png">
</details>

## Project Structure

### Web Pages

The web pages are easy to navigate and consists of various pictures and backgrounds for better visual of the website.

### Sections

##### Home page

- A navbar with nav-items to navigate to various pages in the website
- Hero Section consist of carousel which support three images and a Hero-content within it
- Our Mission section explains about the mission of the Humanitas company
- Our Vision section explains about the vision Humanitas company wants to acheive
- Footer with social media and useful navigation links

##### About Page

- A navbar with nav-items to navigate to various pages in the website
- A section about what we doo with a responsive image background
- A section with story of the site owner
- Footer with social media and useful navigation links

##### Our Stories Page

- A navbar with nav-items to navigate to various pages in the website
- A card display of stories written by users
- Footer with social media and useful navigation links

##### Contact Page

- A navbar with nav-items to navigate to various pages in the website
- A contact form to communicate with the website owner and team
- An image for better view

##### Booking Page

- A navbar with nav-items to navigate to various pages in the website
- A table consisting of day,date and timeblocks for booking an appointment
- Footer with social media and useful navigation links

##### Profile Page

- A navbar with nav-items to navigate to various pages in the website
- Page to display data of the user

##### My Bookings Page

- A navbar with nav-items to navigate to various pages in the website
- Table consisting data of bookings of user

##### My Stories Page

- A navbar with nav-items to navigate to various pages in the website
- A card display of stories written by the user
- Footer with social media and useful navigation links

### Code structure

Project code structure is organized and divided into various application folders and constructed using Django Framework

#### Project Apps

- Home app - constructed to deliver basic information for the User about the app via Home page with simple an intuitive navigation(links in nav-bar and footer to navigate throughout the app).

  It also provides the following functionalities:

  1. basic contact form for user to contact the team and a footer
  2. user authentication and profile management functionality, full CRUD functionality, so user can create an account, update profile, upload supporting images for a profile

- stories app - constructed to deliver CRUD functions of a humanitas stories app, where  the structure includes the necessary files for running the application, including the views, models, and templates required to create, read, update, and delete blog posts and comments.

- booking app - delivers functionality for users to book a call with the team and site owner . The app includes views and templates for displaying the bookings of user and also to create, update and delete existing bookings.

#### Other django apps

- **settings.py**: This file contains configuration settings for your Django project, such as database settings, installed apps, and middleware.
- **Procfile**: This file is used to specify the commands that should be executed when your Django app is deployed on a hosting platform.
- **static**: This directory contains the base CSS and JavaScript files
- **templates**- base-level folder with basic templates extended throughout other templates like: base.html, navbar.html, footer.html, also templates for user authentication. and also each app has its own templates folder with HTML files to support the app's functionality and reusability
- **requirements.txt**: This file lists the dependencies required for the Django project to run.
- **env.py**: This file is used to store environment variables for a Django project or application, such as database connection details or API keys.

##### Back to [top](#table-of-contents)

## Models

### Data Models

#### User Model

- User model as part of the Django allauth library contains basic information about authenticated user and contains folowing fields:
  Username, Password, Email

#### Profile model

- Profile model is created for user to add their details and image for better interaction with the website

| Name          | Database Key  | Field Type      | Validation                          |
| ------------- | ------------- | --------------- | ----------------------------------- |
| user          | user          | OneToOneField   | User, on_delete=models.CASCADE      |
| profile_image | profile_image | CloudinaryField | 'image', default='placeholder'      |
| first_name    | first_name    | CharField       | max_length=50 blank=True            |
| last_name     | last_name     | CharField       | max_length=50 blank=True            |
| email         | email         | EmailField      | max_length=100 null=True blank=True |

#### Contact model

- Contact model is created for user to contact with the site owner and team

| Name       | Database Key | Field Type    | Validation                               |
| ---------- | ------------ | ------------- | ---------------------------------------- |
| message_id | message_id   | AutoFirld     | PrimaryKey=True                          |
| user       | user         | ForeignKey    | User, on_delete=models.CASCADE null=True |
| name       | name         | CharField     | max-length=50 null=True                  |
| email      | email        | EmailField    | max_length=100 default=""                |
| created_on | created_on   | DateTimeField | auto_now_add=True                        |
| message    | message      | TextField     |                                          |

#### Booking model

- Booking model is created for user to book an appointment with Timeblocks_CHOICES

| Name      | Database Key | Field Type | Validation                                                |
| --------- | ------------ | ---------- | --------------------------------------------------------- |
| user      | user         | ForeignKey | User, on_delete=models.CASCADE null=True                  |
| date      | date         | DateField  | default=timezone.now                                      |
| timeblock | timeblock    | CharField  | max_length=10, choices=TIMEBLOCK_CHOICES, default="10:00" |
| helptype  | helptype     | CharField  | max_length=100, default=""                                |

#### HumanitasPost model

- Humanitas model is created for user to add a story with a cover_image

| Name        | Database Key | Field Type      | Validation                                         |
| ----------- | ------------ | --------------- | -------------------------------------------------- |
| title       | title        | CharField       | max_length=200, unique=True                        |
| creator     | creator      | ForeignKey      | User, on_delete=models.CASCADE                     |
| slug        | slug         | SlugField       | max_length=200, null=True, unique=True, blank=True |
| body        | body         | TextField       |                                                    |
| status      | status       | IntegerField    | choices=STATUS, default=1                          |
| cover_image | cover_image  | CloudinaryField | 'image', default='placeholder'                     |
| created_on  | created_on   | DateTimeField   | auto_now_add=True                                  |
| updated_on  | updated_on   | DateTimeField   | auto_now_add=True                                  |

#### Comment model

- Comment model was created for user to comment on a story

| Name           | Database Key   | Field Type    | Validation                                                       |
| -------------- | -------------- | ------------- | ---------------------------------------------------------------- |
| author         | author         | ForeignKey    | User, on_delete=models.CASCADE                                   |
| created_on     | created_on     | DateTimeField | auto_now_add=True                                                |
| humanitas_post | humanitas_post | ForeignKey    | HumanitasPost, on_delete=models.CASCADE, related_name='comments' |
| content        | content        | TextField     | max_length=400                                                   |
| approved       | approved       | BooleanField  | default=True                                                     |

## Features

## Validation

---

### CSS

- [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)was used to validate the css in the project. Validator with no errors.

<details><summary>Style.css</summary>
<img src="documentation/html-validations/css-validation.png">
</details>

### Html

- [WC3 Validator](https://validator.w3.org/) was used to validate the html in the project

- Note : all info on validator pages are related with using cloudinary template tags for rendering user uploaded images and there for trailing slash cant be removed

<details><summary>Home</summary>
<img src="documentation/html-validations/index.png"  >
</details>
<details><summary>About</summary>
<img src="documentation/html-validations/about.png" >
</details>

<details><summary>Register</summary>
<img src="documentation/html-validations/signup.png" >
</details>

<details><summary>Login</summary>
<img src="documentation/html-validations/login.png" >
</details>

<details><summary>Logout</summary>
<img src="documentation/html-validations/logout.png" >
</details>

<details><summary>Profile</summary>
<img src="documentation/html-validations/profile-page.png" >
</details>

<details><summary>Edit profile</summary>
<img src="documentation/html-validations/edit-profile.png">
</details>

<details><summary>Delete User</summary>
<img src="documentation/html-validations/delete-user.png" >
</details>

<details><summary>Humanitas Stories</summary>
<img src="documentation/html-validations/our-stories.png" >
</details>

<details><summary>My Stories</summary>
<img src="documentation/html-validations/my-stories.png" >
</details>

<details><summary>Story Detail</summary>
<img src="documentation/html-validations/story-detail.png" >
</details>

<details><summary>Edit Story</summary>
<img src="documentation/html-validations/add-story.png">
</details>

<details><summary>Delete Story</summary>
<img src="documentation/html-validations/delete-story.png" >
</details>

<details><summary>Booking Home Page </summary>
<img src="documentation/html-validations/booking-home.png" >
</details>

<details><summary>My Bookings</summary>
<img src="documentation/html-validations/my-bookings.png" >
</details>

<details><summary>Update Booking</summary>
<img src="documentation/html-validations/add-booking.png" >
</details>

<details><summary>Delete Booking</summary>
<img src="documentation/html-validations/cancel-booking.png" >
</details>

### Python

- [CI Python Linter](https://pep8ci.herokuapp.com/) was used for validation of python files. No errors were found

##### Home App

<details><summary>Home Models</summary>
<img src="documentation/pep8-validations/home-models.png" >
</details>

<details><summary>Home Forms</summary>
<img src="documentation/pep8-validations/home-forms.png" >
</details>

<details><summary>Home Urls</summary>
<img src="documentation/pep8-validations/home-urls.png" >
</details>

<details><summary>Home Views</summary>
<img src="documentation/pep8-validations/home-views.png" >
</details>

##### Stories App

<details><summary>Stories Models</summary>
<img src="documentation/pep8-validations/stories-models.png" >
</details>

<details><summary>Stories Forms</summary>
<img src="documentation/pep8-validations/stories-forms.png" >
</details>

<details><summary>Stories Urls</summary>
<img src="documentation/pep8-validations/stories-urls.png" >
</details>

<details><summary>Stories Views</summary>
<img src="documentation/pep8-validations/stories-views.png" >
</details>

##### Bookings App

<details><summary>Bookings Models</summary>
<img src="documentation/pep8-validations/booking-models.png" >
</details>

<details><summary>Bookings Forms</summary>
<img src="documentation/pep8-validations/booking-forms.png" >
</details>

<details><summary>Bookings Urls</summary>
<img src="documentation/pep8-validations/booking-urls.png" >
</details>

<details><summary>Bookings Views</summary>
<img src="documentation/pep8-validations/booking-views.png" >
</details>
