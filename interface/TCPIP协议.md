# TCP/IP协议

> 传输控制协议/网络协议，也叫作“网络通讯协议”
> Transmission Control Protocol/Internet Protocol

## 协议族
TCP/IP协议是一类协议，主要包含：
- 应用协议：
    - HTTP
    - SMTP
    - FTP
    - TELNET
    - SNMP
- 传输协议：
    - TCP
    - UDP
- 网际协议：
    - IP
    - ICMP
    - ARP
- 路由控制协议：
    - RIP
    - OSPF
    - BGP

## 协议分层
从上到下依次是：
- 应用层
- 传输层
- 网络层
- 网络接口层

## TCP三次握手
建立一个TCP连接时，需要客户端和服务器端总共发送3个包以确认连接的建立
- 第一次握手：client将标志位SYN置位1，随机产生一个值seq=J，并将该数据包发送给Server，Client状态变为SYN_SENT
- 第二次握手：Server收到标志位SYN=1的数据包知道Client请求建立连接，Server将标志位SYN和ACK都置位1，ack=J+1，随机产生一个值seq=K，并将该数据包发送给Client以确认连接请求，Server状态变为SYN_RCVD
- 第三次握手：
    - Client收到数据包后检查ack是否为J+1，ACK是否为1，如果是则将ACK置为1，ack=K+1，并将数据包发送给Server
    - Server收到后检查ack是否为K+1，ACK是否为1，如果是则建立连接，Client和Server进入ESTABLISHED状态开始传输数据

## TCP四次挥手
终止TCP连接时，需要客户端和服务端总共发送4个包以确认连接的断开
- 第一次挥手：Client发送结束标志FIN和一个随机序号M，用来关闭Client到Server的数据传送，Client进入FIN_WAIT_1状态
- 第二次挥手：Server收到FIN后，发送一个ACK给Client，确认序号为M+1（与SYN相同，一个FIN占用一个序号），Server进入CLOSE_WAIT状态
- 第三次挥手：Server发送一个FIN，用来关闭Server到Client的数据传送，Server进入LAST_ACK状态
- 第四次挥手：Client收到FIN后，Client进入TIME_WAIT状态，接着发送一个ACK给Server，确认序号为收到序号+1，Server进入CLOSED状态，完成四次挥手