确保服务器安全  
最好断开网络 本机操作

    vi /etc/my.cnf 
        #在[mysqld]的段中加上一句：skip-grant-tables 
    /etc/init.d/mysqld restart 

    mysql 
        > USE mysql ; 
        > UPDATE user SET Password = password ( 'new-password' ) WHERE User = 'root' ; 
        > flush privileges ; 
        > quit 

    vi /etc/my.cnf 
        #将刚才在[mysqld]的段中加上的skip-grant-tables删除 

    /etc/init.d/mysqld restart 
