# nginx log

*version - 0.1*

*by - zhangyin*

******

####  环境需求： 

* python3.6+ 


* plotly 2.7+
* mysql.connector
* pandas
* tornado

*******

#### 使用手册：

* nginx_log_ip 项目：用于绘制提交日期的相关应用的每日访问前20的ip柱状分析图。

* nginx_log_visitor项目： 用于绘制提交日期的相关应用的每时访问总量。

* nginx_log_maxvisitor项目： 用于绘制给定日期的相关应用的每天忙时访问量。

* 具体使用方法如下：

  * nginx_log_ip 项目：

    ```
    cd ${path}/nginx_log/nginx_log_ip
    python3 tornado_helloworld.py &
    ```

    通过上述命令启动应用，会自动在本地打开 `TCP：35855` 端口的监听，通过访问`IP:35855`访问项目首页，并根据提示选择相关的日期及项目。提交后稍作等待即可查看相应图表。

  * nginx_log_visitor项目：

    ```
    cd ${path}/nginx_log/nginx_log_visitor
    python3 tornado_helloworld.py &
    ```

    通过上述命令启动应用，会自动在本地打开 `TCP：35856` 端口的监听，通过访问`IP:35856`访问项目首页，并根据提示选择相关的日期及项目。提交后稍作等待即可查看相应图表。

  * nginx_log_maxvisitor项目：

    ```
    cd ${path}/nginx_log/nginx_log_visitor
    python3 tornado_helloworld.py &
    ```

    通过上述命令启动应用，会自动在本地打开 `TCP：35859` 端口的监听，通过访问`IP:35859`访问项目首页，并根据提示选择相关的日期及项目。提交后稍作等待即可查看相应图表。

*******

#### 参数配置：

* 数据库连接参数：tornado_helloworld.py 文件中的PoemPageHandler类下post函数中，引用了vis函数，配置了相应的参数。如果要修改相应的数据库连接，更改此处并重启即可。

*****












