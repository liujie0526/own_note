    vim /etc/vsftpd/vsftpd.conf
        #具体内容参照其他医院配置文件
    useradd jdkqyyftp
    service vsftp start
    passwd jdkqyyftp
    ftp localhost
    
    su - jdkqyyftp
    mkdir .ssh
    #此时，将ccb的公钥发到.ssh
    cat id_rsa.pub >> .ssh/authorized_keys
    chmod 600 .ssh/authorized_keys
    cd
    chmod 700 .ssh/