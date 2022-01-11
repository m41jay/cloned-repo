## Load balancer



Concepts:

- [Load balancing](http://www.thegeekstuff.com/2016/01/load-balancer-intro/)

- [Load balancing algorithms](https://devcentral.f5.com/articles/intro-to-load-balancing-for-developers-ndash-the-algorithms)

- [Web stack debugging-5 commands](https://www.linux.com/blog/first-5-commands-when-i-connect-linux-server)

- [uptime](https://whatis.techtarget.com/definition/uptime-and-downtime)

- [load average](https://blog.scoutapp.com/articles/2009/07/31/understanding-load-averages)

- [Linux load average](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html)



![lb](https://user-images.githubusercontent.com/6486822/29430135-214b6c86-8348-11e7-963d-c0f23cacf0d7.png)



### Read:



 * [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
 
 * [HTTP header](https://www.techopedia.com/definition/27178/http-header)
 
 * You have been given 2 additional servers:
 
      * [STUDENT_ID]-web-02
      
      * [STUDENT_ID]-lb-01
      
 * Let's improve our web stack so that there is [redundancy](https://en.wikipedia.org/wiki/Redundancy_(engineering)) for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.
 
 * For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.
 


### Requirements



- Allowed editors: vi, vim, emacs

- All your files will be interpreted on Ubuntu 14.04 LTS

- All your files should end with a new line

- All your Bash script files must be executable

- Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error

- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash

- The second line of all your Bash scripts should be a comment explaining what is the script doing