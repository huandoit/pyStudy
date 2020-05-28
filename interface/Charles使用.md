# Charles简介
> Charles 是在 PC 端常用的网络封包截取工具，在做移动开发时，我们为了调试与服务器端的网络通讯协议，常常需要截取网络封包来分析。
> 除了在做移动开发中调试端口外，Charles 也可以用于分析第三方应用的通讯协议。配合 Charles 的 SSL 功能，Charles 还可以分析 Https 协议。
>
> Charles 通过将自己设置成系统的网络访问代理服务器，使得所有的网络访问请求都通过它来完成，从而实现了网络封包的截取和分析。
>
> https://www.jianshu.com/p/6777a24c5ec2

# Windows配置Charles
## 设置不代理计算机的请求（推荐）

- **Proxy -> Windows Proxy**
- 勾选则抓取计算机请求
- 在对APP进行数据抓取时，不勾选该选项

## 设置代理HTTPS请求并添加证书

- **Proxy -> SSL Proxy Settings**
    - 选中 Enable SSL Proxying
    - 点击 Add 添加要设置代理的域名和端口
    - 点击 Client Certificates，给域名添加证书（双向认证必须添加证书）
    
## 关心域名重点显示

- **View -> Focused Hosts**
- 用于设置重点关心的域名，在列表中会独立显示

## 安装Charles根证书

- **Help -> SSL Proxying -> Install Charles Root Certificate**

## 安装手机所需配置

- **Help -> SSL Proxying -> Install Charles Root Certificate on a Mobile Device or Remote Browser**

## 手机安装证书

- 手机浏览器（android 手机使用系统浏览器）访问 chls.pro/ssl 安装证书

# 工具导航栏说明
> https://juejin.im/post/5b8350b96fb9a019d9246c4c

- Clear the current Session
- Start/Stop Recording
- Start/Stop Throttling
- Enable/Disable Breakpoints