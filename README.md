# WeblogicWeakPwd
Weblogic弱口令批量检测工具
```
weblogicpwd.py      单目标扫描，初始版本
weblogicweakpwd.py  批量扫描，过渡版本
weblogicweakpwds.py 批量扫描，多进程版本，最终版本

最终版weblogicweakpwds.py仍有欠缺，在异常处理这块还需完善，
尤其是遇到非weblogic的url，所以强烈推荐预识别中间件。
什么？为什么我没有增加预识别模块？
因为之前已经发布过weblogic识别脚本了，
传送门：https://github.com/rabbitmask/WhoIsWeblogic
另外因为多进程模块自有的小bug，尽可能在非交互界面下使用（即使用命令窗口执行）
```
