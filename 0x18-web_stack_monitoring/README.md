## Webstack monitoring



### Concepts:

- [Monitoring](https://intranet.hbtn.io/concepts/13)

- [Server](https://intranet.hbtn.io/concepts/67)



![monitoring](https://user-images.githubusercontent.com/6486822/31350953-fb76188e-acdd-11e7-9359-26d9a9ba6646.png)



### Read



- [What is server monitoring](https://intranet.hbtn.io/rltoken/ujTPhBAl3TvofrBE8Hlc2w)

- [What is application monitoring](https://intranet.hbtn.io/rltoken/fGzCCVr7lwNEvarE8u1HRQ)

- [Sumologic API Acess Keys](https://intranet.hbtn.io/rltoken/mdMRQFYu5rbZvhT9l3epDQ)

- [Nginx logging](https://intranet.hbtn.io/rltoken/w17_g_yJMh0x3-You cannot fix or improve what you cannot  is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.



Web stack monitoring can be broken down into 2 categories:



- Application monitoring: getting data about your running software and making sure it is behaving as expected

- Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)



### Monitor all the things!!!
(https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg)


### What you should learn from this project



- Why do we need monitoring

- What are the 2 types of monitoring

- What is in a web server (such as Nginx) access logs



NGINX writes information about client requests in the access log right after the request is processed. By default, the access log is located at logs/access.log, and the information is written to the log in the predefined combined format. To override the default setting, use the log_format directive to change the format of logged messages, as well as the access_log directive to specify the location of the log and its format. The log format is defined using variables.



- What is in a web server error logs



NGINX writes information about encountered issues of different severity levels to the error log. The error_log directive sets up logging to a particular file, stderr, or syslog and specifies the minimal severity level of messages to log. By default, the error log is located at logs/error.log and messages from all severity levels above the one specified are logged.



### Requirements



- Allowed editors: vi, vim, emacs

- All your files will be interpreted on Ubuntu 14.04 LTS

- All your files should end with a new line

- All your Bash script files must be executable

- Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error

- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash

- The second line of all your Bash scripts should be a comment explaining what is the script doingmeasureEThHonhA)



