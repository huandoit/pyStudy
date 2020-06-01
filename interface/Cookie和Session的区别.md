# Cookie

- Cookie存放在客户端(浏览器)的进程内存和客户端所在的机器硬盘上
- Cookie只能存储少量文本，大概4K
- Cookie不能在不同浏览器之间共享


# Session

- Session存放在服务器端，存放在网站进程的内存中
- Session在初次设置时，会在session池中实例化一个session对象，以sessionid的值作为key，同时将key以cookie的形式保存到客户端的内存中
- Session的作用域只存在当前浏览器的绘画中，当浏览器关闭后会将sessionid丢失，但是服务器的session对象要20分钟以后才会回收