### nginx与tomcat之间https通信配置方式

 <Engine name="Catalina" defaultHost="localhost" jvmRoute = "jvm-jspt1">
    <Valve className="org.apache.catalina.valves.RemoteIpValve"  
           remoteIpHeader="X-Forwarded-For"  
           protocolHeader="X-Forwarded-Proto"  
           protocolHeaderHttpsValue="https"/>
需要注意;
           remoteIpHeader="X-Forwarded-For"  
           protocolHeader="X-Forwarded-Proto" 
要在proxy文件中定义

