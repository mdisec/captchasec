# Captchasec

chaptchasec is a captcha difficulty tester. It uses de-captcher.com as an OCR server. 

  - Gets images from local directory
  - Generate report as HTML, CSV, JSON

```
➜  ~  captchasec -u mmetince -p 687226 -d /tmp/ptt/
Your current account balance = 9.848000000
Determining of jpeg files from given directory...
Total number of jpeg = 20
Sending /tmp/ptt/1. image to api...
Yay! Cracked in 7.196321 second..! Answer is = 825b3
Sending /tmp/ptt/10. image to api...
Yay! Cracked in 15.235815 second..! Answer is = mrv6n
Sending /tmp/ptt/11. image to api...
Yay! Cracked in 13.220645 second..! Answer is = vh32j
Sending /tmp/ptt/12. image to api...
Yay! Cracked in 5.227966 second..! Answer is = ggz8k
Sending /tmp/ptt/13. image to api...
Yay! Cracked in 3.146601 second..! Answer is = 8xk34
Sending /tmp/ptt/14. image to api...
Yay! Cracked in 10.163727 second..! Answer is = 2nd3w
Sending /tmp/ptt/15. image to api...
Yay! Cracked in 7.188108 second..! Answer is = 46rgd
Sending /tmp/ptt/16. image to api...
Yay! Cracked in 8.175217 second..! Answer is = x76xy
Sending /tmp/ptt/17. image to api...
Yay! Cracked in 2.163303 second..! Answer is = 
Sending /tmp/ptt/18. image to api...
Yay! Cracked in 8.165439 second..! Answer is = 5h6mr
Sending /tmp/ptt/19. image to api...
Yay! Cracked in 5.157223 second..! Answer is = t82pc
Sending /tmp/ptt/2. image to api...
Yay! Cracked in 16.233299 second..! Answer is = nvg5y
Sending /tmp/ptt/20. image to api...
Yay! Cracked in 5.194488 second..! Answer is = 8wfd3
Sending /tmp/ptt/3. image to api...
Yay! Cracked in 4.234764 second..! Answer is = sfs9d
Sending /tmp/ptt/4. image to api...
Yay! Cracked in 13.203672 second..! Answer is = cms67
Sending /tmp/ptt/5. image to api...
Yay! Cracked in 12.225136 second..! Answer is = h3g4j
Sending /tmp/ptt/6. image to api...
Yay! Cracked in 6.161707 second..! Answer is = 58vd6
Sending /tmp/ptt/7. image to api...
Yay! Cracked in 16.198338 second..! Answer is = 78c2j
Sending /tmp/ptt/8. image to api...
Yay! Cracked in 7.174163 second..! Answer is = 238z4
Sending /tmp/ptt/9. image to api...
Yay! Cracked in 17.220729 second..! Answer is = k3dgv
Results are saved into result_02-16-15-09:59:42.html
```

HTML report 

![alt tag](https://www.mehmetince.net/wp-content/uploads/2015/02/Screen-Shot-2015-02-16-at-10.00.29.png)

### Version
0.0.1

### Tech

It uses following native Python 2 modules. 

* Datetime
* imghdr
* urllib
* io

### Installation

Following instructions will be complate installation.

```sh
$ python setup.py install
```

### Development

Want to contribute? Great!

* Fork it!
* Create your feature branch: git checkout -b my-new-branch
* Commit your changes: git commit -m 'Add some feature'
* Push to the branch: git push origin my-new-branch
* Submit a pull request.

### Todo's

 - Error handling
 - Custom OCR server
 - Fetch captches from remote URL.

License
----

MIT

**Free Software, Hell Yeah!**
