### nginx配置

```shell
        location ~ (/ccbms$|/ccbms/$) {
            rewrite ^(.*) http://$server_name$1/index.php;
        }
 
        location ~ /ccbms.*\.(js|css|jpg|png|gif)$ {
             proxy_pass http://192.168.1.103;
             include proxy.conf;
             include /usr/local/nginx/conf/ccbejf.rules;
         }
         
         location ~ /ccbms.*(register|edit_info|userinfo|charge|seconds|index|goods|good|faqs|account_money|account_score|order|exchange|lucknum|login|dhcg).php$ {
             proxy_pass http://192.168.1.103;
             include proxy.conf;
             include /usr/local/nginx/conf/ccbejf.rules;
         }
```

