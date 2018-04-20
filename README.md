# spider_project
In the process of learning crawlers, all projects are hosted here, and some of them are annotated.

### douban-movie-info

第一个写的项目是一个爬取豆瓣全站电影信息的`crawlspider`,豆瓣的站用来新手入门可以说是完美，尽管豆瓣提供了自身的api接口（然而爬api并没有什么意思-_-），并且豆瓣自身做了一定的反爬措施，他会检测你的`user-agent`和`cookies`，当你的访问频率达到一定次数的时候，它会自动对你的访问进行限制，不论怎样都是403错误，遇到这种情况，就尽快去的去更换`user-agent`吧，在这个项目中，实现了`crawlspider`的规则化抓取和随机`user-agent`的设置，以及随机ip地址的分配,数据存储的形式为json形式。