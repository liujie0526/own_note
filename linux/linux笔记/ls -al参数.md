     1）第一栏是文件属性，共有10个属性，每一位代表一个属性。
        第1位属性代表这个文件是目录、文件、链接、设备中的哪一类：
        # d：表示目录 #
        # -：表示普通文件 #
        # l：表示链接文件 #
        # b：表示设备文件中可供存储的接口设备 #
        # c：表示设备文件中的串行端口设备，比如鼠标、键盘等 #

        第2位到第十位共9个属性，分为3组，均以rwx形式组合，其中：
        # r：代表该文件可读 #
        # w：代表该文件可写 #
        # x：代表该文件可执行 #
        如果不具备某属性，则对应的字母换成“-”
           范例【1】某文件只有读写能力，没有执行能力，则表示为“rw-”
        这三组属性分别代表文件拥有者的权限、文件所属组的权限、其他用户的权限。
           范例【2】“rwxrw-r--”表示该文件的拥有者对该文件可读可写可执行，该文件所在组的成员对文件有读写权限，其他用户对该文件只能读。
        注意（PS）：X属性对目录有特殊含义，表示是否可以进入该目录的权限。
           范例【3】config目录，属性为“drwx------”表示只有root用户能进入，而所在组其他用户均不能进入。
        
     2）第二栏表示链接占用的节点（inode），新文件一般都为1，建立硬链接后此数会增加。如果是目录，则指目录中包含的子目录数，空目录为2，因为空目录中至少包含“.”和“..”目录。
     3）第三栏表示该文件或目录的拥有者。
     4）第四栏表示该文件所属的群组。
     5）第五栏表示这个文件的大小。
     6）第六栏表示改文件最新修改时间。
     7）第七栏表示该文件的文件名。