<h3><a href="https://github.com/yingzk/spider/tree/master/WeixinArticles">WeixinArticle</a></h3>

<p><strong>URL:</strong>http://weixin.sogou.com/<br />
<strong>Technology:</strong> PyQuery, MongoDB, requests<br />
<strong>Statement:</strong> Use sogou.com search for weixin articles that from official account.
Use IP ProxyPool to deal the limit ip system.
spider all articles of a keyword
and save some information to MongoDB</p>
<br />

<h3><a href="https://github.com/yingzk/spider/tree/master/bsbdqj">bsbdqj</a></h3>
<p><strong>URL:</strong> http://www.budejie.com/<br />
<strong>Technology:</strong> md5, MongoDB, requests, BeautifulSoup<br />
<strong>Statement: </strong>spider the small video from budejie and save some information to MongoDB</p>
<br />

<h3><a href="https://github.com/yingzk/spider/tree/master/jiepai">jiepai</a></h3>
<p><strong>URL:</strong> http://www.toutiao.com/search_content/<br />
<strong>Technology:</strong> MongoDB, requests, BeautifulSoup, multiprocessing, md5<br />
<strong>Statement:</strong> spider the images group or images article. save the images to MongoDB and save the mp4 video to local</p>
<br />

<h3><a href="https://github.com/yingzk/spider/tree/master/qcloud">qcloud</a></h3>
<p><strong>URL: </strong>https://www.qcloud.com/community/all/</p>
<p><strong>Technology: </strong> requests, BeautifulSoup, MongoDB, multiprocessng, jieba, wordcloud, matplotlib</p>
<p><strong>Statement: </strong> use crawler spider all of articles from qcloud/community,</p>
<p>use &#39;jieba&#39; split word system  spilt all articles and made work counter</p>
<p>then use &#39;matplotlib&#39; make a word cloud, can see the main topic for qcloud/community</p>
<p>save all articles to MongoDB</p>
<br />

<h3><a href="https://github.com/yingzk/spider/tree/master/spider_novel">spider_novel</a></h3>
<p><strong>URL: </strong> http://www.17k.com/list/</p>
<p><strong>Technology: </strong> requests</p>
<p><strong>Statement: </strong> use crawler spider the novels, and save the novel to &#39;html&#39; type</p>
<br />

<h3><a href="https://github.com/yingzk/spider/tree/master/taobao">taobao</a></h3>
<p><strong>URL: </strong> https://www.taobao.com</p>
<p><strong>Technology: </strong> MongoDB, selenium, PyQuery</p>
<p><strong>Statement: </strong> Use crawler spider all of the goods information that the goods from taobao search the keyword</p>
<p>Use Selenium simulate the browser(Chrome) operator, then get page source code, Use PyQuery parse the html code and extract goods information and save those information to MongoDB database</p>
<br />

<h3><a href="https://github.com/yingzk/spider/tree/master/zhihuishu">zhihuishu</a></h3>
<p><strong>URL: </strong> http://online.zhihuishu.com/CreateCourse/learning/videoList?courseId=</p>
<p><strong>Technology: </strong> Selenium, PyQuery</p>
<p><strong>Statement: </strong> Use Selenium simulate the browser(Chrome) operator, to achieve use program automatic see the course.</p>
<p>Progress deal the tip window, close them and judge the course over time.</p>
<br />

<h3><a href="https://github.com/yingzk/spider/blob/master/CrackSTBU.py">CrackSTBU.py</a></h3>
<p><strong>URL:</strong> http://172.21.160.114:8080/portal/templatePage/20160629121614757/login_custom.jsp?userip=172.18.13.152&amp;userurl=http://172.18.13.1 (The URL is dynamic, so need connection the school WiFi(STBU-EDU), get the IP and PORT)</p>
<p><strong>Technology:</strong> Selenium</p>
<p><strong>Statement: </strong> Use Selenium simulate the browser(Chrome) operator to achieve the login, is force crack, use all of student number try it (like 2015201001) and the password is 8888</p>

<h3><a href="https://github.com/yingzk/spider/tree/master/book_douban_new_book">book_douban_new_book</a></h3>
<p><strong>URL: </strong> https://book.douban.com/latest</p>
<p><strong>Technology: </strong> re, requests</p>
<p><strong>Statement: </strong> use requests get the douban latest book page&#39;s source code, and use regex, extract the new book information.</p>
<h3><a href="https://github.com/yingzk/spider/blob/master/spiderMaoyan.py">spiderMaoyan.py</a></h3>
<p><strong>URL: </strong> http://maoyan.com/board/4?offset=</p>
<p><strong>Technology: </strong> re, requests</p>
<p><strong>Statement: </strong> use requests get the maoyan movie leaderboard, and use regex extract the movies inforamtion</p>
