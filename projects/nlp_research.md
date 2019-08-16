---
layout: project
type: project
image: images/nlp_research/uhmanoa_logo.png
title: PDC Parser
permalink: projects/pdc_parser
date: 2018
labels:
  - Python
  - Stanford Parser
  - Regular Expressions
  - Natural Language Processing

summary: Research on NLP with Dr. David Chin from the UH Manoa and Matthew Lee from the University of Rochester. Implemented an NLP solution for the Pacific Disaster Center to better summarize information from unstandardized disaster data from events such as volcanoes, tsunamis, and cyclones.

---
<img class class="ui medium right floated rounded image" src="../images/nlp_research/uhmanoa_logo.png">

I began working with Dr. Chin and Matthew since I was interested in expanding my knowledge of the applications of computer science. After emailing back and forth, I finally met with Dr. Chin and Matthew to discuss the project we would be doing with the PDC. 

The main problem that we were tasked to solve was that their current parser uses regular expressions and does not accurately extract information from disaster text files. Regular expressions follow conrete patterns to find information. Unlike humans, it is unable to understand the relationship between words or see the distinction between sections of text. This is the main reason why we decided to implement auto-correct APIs to fix spelling mistakes and the Stanford Parser to extract word dependency relationships.

Multiple warning centers write text files when disasters such as tsunamis, cyclones, or volcanoes take place and there is no standardized format for each warning center. This discrepancy in format makes it very difficult to extract data. To see the typical format for the tsunami, cyclone, and volcano warnings along with their respective XML files, you can visit the GitHub repository below. A basic flowchart on the order of operations can also be seen through GitHub.

If you want to learn more about this project, please check out this Github link below!

Source: <a href="https://github.com/fpang0502/nlp_project"><i class="large github icon"></i>PDC Parser</a>
