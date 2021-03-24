'''
docker优势：
    1.简化配置
    这是Docker初始目的，虚拟机VM最大的好处是基于你的应用配置能够无缝运行在任何平台上。Docker提供同样类似VM的能力，但是没有任何副作用，它能让你将环境和配置放入代码然后部署，同样的Docker配置能够在各种环境中使用，这实际是将应用环境和底层环境实现了解耦。
    2.代码管道化管理
    能够对代码以流式pipeline管道化进行管理，从开发者的机器到生产环境机器这个流程中都能有效管理。因为在这个流程中会有各种不同的环境，每个都可能有微小的区别，Docker提供了跨越这些异构环境以一致性的微环境，从开发到部署实现流畅发布。
    3.开发人员的生产化
    在一个开发环境，我们希望我们的开发环境能更加接近于生产环境，我们会让每个服务运行在自己的VM中，这样能模拟生产环境，比如有时我们并不总是需要跨越网络连接，这样我们可以将多个Docker装载一系列服务运行在单机上最大程度模拟生产分布式部署的环境。
    4.应用隔离
    有很多理由你需要在一台机器上运行多个应用，这就需要将原来铁板一块monolithic的应用切分为很多微服务。实现应用之间的解耦，将多个应用服务部署在多个Docker中能轻松达到这个目的。
    5.服务合并
    使用Docker也能合并多个服务以降低费用，不多的操作系统内存占用，跨实例共享多个空闲的内存，这些技术Docker能以更加紧密资源提供更有效的服务合并。
    6.多租户
    Docker能够作为云计算的多租户容器，使用Docker能容易为每个租户创建运行应该多个实例，这得益其灵活的快速环境以及有效diff命令。
    7.快速部署
    Docker通过创建进程的容器，不必重新启动操作系统，几秒内能关闭，你可以在数据中心创建或销毁资源，不用担心额外消耗。典型的数据中心利用率是30%，通过更积极的资源分配，以低成本方式对一个新的实例实现一个更聚合的资源分配，我们很容易超过这个利用率，大大提高数据中心的利用效率。
    8.环境统一
    docker将容器打包成镜像，创建符合docker hub规范的镜像，上传进个人的私有docker hub，转换环境时直接pull即可，最大程度的保证了开发环境，正式环境统一。
    原文链接：https://blog.csdn.net/qq_37527715/article/details/79878891

docker三要素
    1.容器
    容器是镜像的一个实例，是一个小型的运行时环境，比如一般是小型的linux环境(基于linux内核的小型环境),用java代码比喻就是：容器是一个类的实例对象，比如 Person 小明 = new Person(); Person就是一个模板，也是要给镜像
    2.镜像
    镜像是保存在镜像仓库中的，pull镜像，相当于 将镜像实例化成容器后部署在自己的环境中，用java来说就是一个类对象
    3.仓库
    仓库是用来保存多个注册仓库的，每个注册仓库中保存了不同的镜像image文件

docker安装
    参考文档：https://www.runoob.com/docker/windows-docker-install.html

docker基本命令
    参考文档：https://www.runoob.com/docker/docker-command-manual.html

docker安装nginx
    参考文档：https://www.runoob.com/docker/docker-install-nginx.html

搭建测试用例管理平台TestLink
    1.部署数据库
    2.部署testlink

搭建持续集成平台Jenkins
    1.部署Jenkins

Docker-Compose使用
    参考文档：https://www.runoob.com/docker/docker-compose.html

Docker的Registry介绍
    参考文档：https://www.jianshu.com/p/fef890c4d1c2
            https://www.cnblogs.com/big-cousin/p/10116396.html

Dockerfile语法与指令
    参考文档：https://www.runoob.com/docker/docker-dockerfile.html

Docker镜像构建
    docker commit:
    docker build:
    参考文档：https://www.runoob.com/docker/docker-image-usage.html

side car模式


'''
