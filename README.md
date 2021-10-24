It is important to ensure that code is commented in a way that someone else can come behind me and examine, modify, and support the product even after I am gone. To that end, it is also important to make sure that code is easy to maintain and built in modularized parts that can be reused in other projects as well as allowing parts to be replaced if necessary without rewriting the whole project.
For this project, the MongoCRUD module was one part that was designed to be modular and reusable. By separating the communication with the database off into an interface module, the overall project can be modified to work with other database implementations without having to recode the entire dashboard. By replacing MongoCRUD with say MSSQLcrud or MySQLcrud, different database systems could be used. Having this separate module also allows me the oportunity to use that part of the codebase of this project more easily in other projects in the future without having to recode or figure out which parts I needs out of some functions that I just crammed into the dashboard code.
Working on this project, I ran into some issues with using a virtual lab and MongoDB which caused me to be locked out of MongoDB multiple times. To get around this, I installed MongoDB and other necessary software in a virtual machine on my personal computer to allow me to continue work on the project. This took some time to do, but it was a lot better than not knowing how much time I was going to lose each time I got disconnected from the virtual lab environment. From a coding standpoint, I have never used Dash before this project. There were several things that I had to figure out through trial and error. There were also a few things that I never figured out. These items are listed in the README Word file. I plan to continue looking for ways to complete these goals.
During the course of the class in which I worked on this project, I learned a lot about NoSQL databases, indexes, queries, and the aggregation pipeline. I also learned how to use Dash to make a dashboard quickly. I look forward to using these technologies in future projects.
Computer scientists create plans, applications, and systems to meet the needs and desires of themselves, their clients, and their employers. Creating software such as this project enables clients to work more efficiently and find the data that they need in a timely manner. This project would also help the animal shelter with which it is used transition specific breeds of dogs into a safe environment, allowing more resources for taking care of their other animals.

Video description located at: https://www.youtube.com/watch?v=GU0zfVHd1b4
