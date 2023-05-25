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
5. As a Site User I can view the post page so that I can view the posts
6. As a Site User I can click a post so that I can read the full post
7. As a Site User I can comment on the post so that I can be involved in conversation
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

#### Profile model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|  user       | user     | OneToOneField|  User, on_delete=models.CASCADE|
|  profile_image       |  profile_image     |CloudinaryField | 'image', default='placeholder'  |
| first_name| first_name  | CharField | max_length=50 blank=True   |
| last_name| last_name  | CharField | max_length=50 blank=True   |
|  email   | email  | EmailField  | max_length=100 null=True blank=True |

#### Contact model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| message_id       | message_id     | AutoFirld |  PrimaryKey=True |
|user       | user     | ForeignKey|  User, on_delete=models.CASCADE null=True|
|  name   | name  | CharField  | max-length=50 null=True  |
|  email   | email  | EmailField  | max_length=100 default="" |
|  created_on     | created_on      | DateTimeField   | auto_now_add=True    |
|  message   | message  | TextField  |   |

#### Booking model

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
|user       | user     | ForeignKey|  User, on_delete=models.CASCADE null=True|
|  date   | date  | DateField  | default=timezone.now |
|  timeblock   | timeblock  | CharField  | max_length=10, choices=TIMEBLOCK_CHOICES, default="A" |
|  helptype    | helptype     | CharField   | max_length=100, default=""    |

#### BlogPost model


| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| title        | title      | CharField| max_length=200, unique=True  |
| creator        | creator       |ForeignKey   | User, on_delete=models.CASCADE  |
|  slug   | slug   | SlugField   | max_length=200, null=True, unique=True, blank=True |
| body       | body     |TextField |      |
| status      | status     |IntegerField |   choices=STATUS, default=1   |
|  cover_image     | cover_image      | CloudinaryField  | 'image', default='placeholder'   |
|  created_on     | created_on      | DateTimeField   | auto_now_add=True    |
|  updated_on     | updated_on      | DateTimeField   | auto_now_add=True    |


#### Comment model


| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| author         |  author          | ForeignKey | User, on_delete=models.CASCADE   |
| created_on        | created_on      | DateTimeField    | auto_now_add=True   |
| humanitas_post | humanitas_post   | ForeignKey   | HumanitasPost, on_delete=models.CASCADE, related_name='comments'     |
| content    | content    | TextField    | max_length=400   |
| approved      | approved     |BooleanField |  default=True     |


### Code structure
Project code structure is organized and divided into various application folders and constructed using Django Framework 

#### Project Apps:
- Home app - constructed to deliver basic information for the User about the app via Home page with simple an intuitive navigation(links in nav-bar and footer to navigate throughout the app).

    It also provides the following functionalities:
    1.  basic contact form for user to contact the team and a footer
    2.  user authentication and profile management functionality, full CRUD functionality, so user can create an account, update profile, upload supporting images for a profile

- stories app - constructed to deliver CRUD functions of a humanitas stories app, where  the structure includes the necessary files for running the application, including the views, models, and templates required to create, read, update, and delete blog posts and comments.


- booking app - delivers functionality for users to book a call with the team and site owner . The app includes views and templates for displaying the bookings of user and also to create, update and delete existing bookings.