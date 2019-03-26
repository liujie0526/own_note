### nginx+php实现渲染markdown文件

* shell操作

```shell
mkdir /usr/local/nginx/html/note
cd /usr/local/nginx/html/note
wget 
```



* nginx vhost conf

```nginx
server {
    listen       80;
    server_name  ********;
    root   /usr/local/nginx/html/note;
    index  index.html ;
    
    autoindex_exact_size off;
    autoindex_localtime on;
    autoindex on;

    default_type 'text/html';
    charset utf-8;

    access_log logs/access_note.log;
    error_log  logs/error_note.log;

    location ~ \.md$ {
        rewrite ^/([^?]*)(?:\?(.*))? /md.php?f=$1&$2 last;
    }
    location ~ .*\.(php|php5)?$
      {
        #fastcgi_pass  unix:/tmp/php-cgi.sock;
        fastcgi_pass  127.0.0.1:9000;
        fastcgi_index index.php;
        include fcgi.conf;
    }
```

