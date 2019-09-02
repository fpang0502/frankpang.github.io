---
layout: project
type: project
image: images/closer/closer_logo.png
title: Closer
permalink: projects/closer
date: 2019
labels:
  - PHP
  - JavaScript
  - HTML/CSS
  - Flexbox
  - MySQL
  - jQuery
  - Bootstrap
  - FFMPEG
summary: Full-Stack web application for families and friends to share memories with one another in one place. A rudimentary version of Google Photos.
---

As a part of my Full-Stack Web Development course at USC, my final project was to create a web application that followed specific guidelines listed [here](). Example requirements were the use of user registration, Create Read Update Delete (CRUD) functionality, an outside API, etc.

I decided to create a website where people could share all their memories in one place. <img class class="ui medium right floated rounded image" src="../images/closer/closer_logo.png">For example, many individuals put their photos and videos on Google Drive or Google Photos and I wanted to make something similar but more personalized (users could have their own family photo album or couples could update media with their adventures). 

In essence, with the application, you can login/register, upload photos/videos, create albums with descriptions and dates, edit them, and make changes to your profile. 

The most difficult part of this was integrating [PHP-FFMPEG]() into the application to create thumbnails for all the videos that a user would upload. This was done for page speed optimizations, as it would take longer to load a video than an image. I was able to get it easily working on Mac, but I needed it to work on the course server. Furthermore, it was also quite difficult to store the images/videos that users would upload, as all images could not be stored on MySQL, but rather had to be stored on the File System and queried through MySQL. So any CRUD actions made by the user would be changed on MySQL, and updated to reflect the File System by CRUDing the File System.

Overall, this project satisfied all the requirements and was really fun to do. Although it wasn't as seamless as I had hoped, I have plans to integrate the Google Photos/Google Drive API so users can login with their Google accounts and display their photos/videos in a much more customized way in comparison to the requirements I had to meet. 

If you want to learn more about this project, please check out this Github link below!

Source: <a href="https://github.com/fpang0502/Closer"><i class="large github icon"></i>Closer</a>
