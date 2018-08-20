---
layout: project
type: project
image: images/shifted.png
title: AllData
permalink: projects/shifted_energy
date: 2018
labels:
  - Python
  - Automate Green API
summary: A data processing tool written in Python to parse data taken recieved from Automate Green's API. This project was done during Summer 2018 for an internship with Shifted Energy where I worked with Olin Lagon, the co-founder and current CTO of Shifted Energy.

---
<img class class="ui medium right floated rounded image" src="../images/htdc.png">

I had the opportunity to intern with Shifted Energy through [Hawaii Technology Development Corporation] (https://www.htdc.org/about/) (HTDC), a state agency that is in charge of managing and supervising Hawaii's growing technology industry through providing services for startups. Through HTDC, I learned a lot about Hawaii's growing efforts in technology and more about the entrepreneur mindset.

<img class class="ui medium right floated rounded image" src="../images/shifted.png">


[Shifted Energy] (https://www.shiftedenergy.com/) is a startup in Hawaii that builds controllers and develops software to retrofit electric resistance water heaters into "massively scalable, cost-effective, real-time demand response assets." With the use of machine learning, they are able to analyze the usage patterns of water heaters and provide important grid services such as fast frequency response, capacity load shifting, and emergence demand response. Additionally, they are able to do this without installing the control systems on the water heater.


Our mentor taught both of us how to code in C++ and helped us understand the OpenCV library for this project. For the programming side, he helped us construct the basic framework to track motion using the concept of [image differencing](https://en.wikipedia.org/wiki/Image_differencing) and we then used a Windows grid display app for validation during data collection.

To achieve real-time motion detection, AIRIS uses the concept of image differencing in which the current frame is compared to the previous frame. If the current frame is different from the previous frame then there is indeed movement.
<img src="../images/airispic.png">

This project won Best of Systems Software at the 2016 Honolulu District Science and Engineering Fair and was nominated as a possible project for the Intel Science and Engineering Fair. After the 2016 Honolulu District Science and Engineering Fair, we worked to apply this image differencing algorithm to leukemia detection for the 2016 Hawaii State Science and Engineering Fair -- which resulted in this project receiving the University of Hawaii at Manoa Department of Information and Computer Sciences Award and 3rd Prize in Systems Software.

This project was my very first time coding and it helped me learn a lot about C++ and the topic of Computer Vision. In addition to being mentored, it was a great experience to build my interpersonal skills when working in a team. As both my partner and I had no prior programming knowledge, it was very important that we were patient and worked well with one another. Looking back at the project as a whole, it has made me appreciate team members and mentorship. I hope that in the future I will also be able to share the same depth of knowledge.

<br>
<img class class="ui medium left floated rounded image" src="../images/airisgroup.jpg">
<br>
<br>

This project and my partner and I were also featured on Hawaii News Now on Sunrise for the [March 11](http://www.hawaiinewsnow.com/story/31448254/students-discuss-their-entries-in-the-hawaii-state-science-and-engineer-fair) airing and the [March 22](http://www.hawaiinewsnow.com/story/31539501/interview-hawaii-state-science-engineering-fair) airing.

If you want to learn more about this project, please check out this Github link below!

Source: <a href="https://github.com/fpang0502/AIRIS"><i class="large github icon"></i>AIRIS</a>
