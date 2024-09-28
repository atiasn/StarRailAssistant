![ico](SRAicon.ico)
# StarRailAssistant(SRA)
崩坏星穹铁道自动化助手
## 什么是SRA？
一个基于图像识别的崩铁自动化程序，帮您完成从启动到退出的崩铁日常。
## 有什么功能？
* 启动游戏
  * 在这里选择好游戏路径，输入账号与密码，`坐和放宽`程序会帮你解决好一切。
* 领取助战奖励
* 领取兑换码奖励
  * 可以一次性输入多个`兑换码`，确保每个`兑换码`分隔开。
* 领取派遣奖励
* 领取巡星之礼
  * *最爱的十连*
* 领取邮件
* 清体力
  * 您可以自由选择关卡，是否`补充体力`、`连战次数`、`执行次数`，一切都交由您来决定，也可以`混合搭配`。
* 领取每日实训
  * *最爱的`星琼`*
* 领取无名勋礼
* 退出游戏
  * *从不回头看`“爆炸”`*
## 我怎么才能使用SRA？急急急
下载链接：[SRAv0.6](https://github.com/Shasnow/StarRailAssisant/releases)
* 如果你是小白，只需要下载项目中的`rar`文件，*一切都为您准备妥当*，只需解压到您喜欢的位置，然后运行`.exe`即可！
* **我想挑战一下自己！** 当然没问题。下载项目中所有的`.py`文件，噢，别忘了 **`.json`与`img`**。确保你的电脑中已经安装好了`Python`，并安装好了下面的库，如果没有，使用`pip`来安装它们。
  ```bash
  pip install opencv-python,pyautogui,json,pyqt5,ctypes,plyer,sys,subprogress,pywing32
  ```
  > 万事俱备，只欠东风
  
  在您最喜爱的**Python编译器**中运行带有 **`SRA`** 前缀的`.py`文件，然后就可以享受`SRA`为您带来的服务。

### 注意事项
* **调整游戏分辨率为1920*1080并保持游戏窗口无遮挡，不要让游戏窗口超出屏幕**
* **执行任务时不要进行其他键鼠操作！请使用游戏默认键位！**
## 你这代码保熟吗？
我们无法保证代码能完美的运行，这便是 **`issues`** 存在的意义。
* 通过 **`issues`** 反馈：https://github.com/Shasnow/StarRailAssisant/issues
* 通过 **`Bilibili私信`** 反馈：https://space.bilibili.com/349682013
* 通过 **`电子邮件`** 反馈：<yukikage@qq.com>
* 或者加入测试群 **994571792** 在这里，你可以：
  * 提取获取版本更新
  * 反馈和意见得到及时回复
  * 与精通 `Python` , `Java` , `C/C++` , `SQL`, `C#` , `Go` , `Vue3` , `HTML` , `JavaScript` , `CSS` , `TypeScript` 的大佬交流。
  * 与 **`太卜司·符玄`** 交流
  * 与*音乐制作人*交流
* 欢迎通过上述渠道反馈问题和提交意见！
  
# 更新公告
beta v0.6 更新公告  
新功能：  
1. 体验优化，新增日志文件 `log.txt` 便于在程序闪退时定位问题。  
2. 新增补充体力功能。  
3. 新增领取兑换码功能。  
4. 新增Windows消息提醒，在任务全部完成时会弹出消息。  
5. 体验优化，现在SRA可以主动获取管理员权限。
   
问题修复：  
1. 修复了在特定情况下未正确移动鼠标导致无法跳转到“侵蚀隧洞”和“历战余响”的问题。  
2. 修复了战斗遇到体力不足时无法处理的问题。  
3. 修正了“执行”与“停止”按钮的行为。  
4. 修复了游戏画面贴近或超出屏幕显示边缘时程序后台直接闪退的问题。
5. 移除了him。
   
已知问题：  
1. 在差分宇宙中因奇物“绝对失败处方(进入战斗时，我方全体有150%的基础概率陷入冻结状态，持续1回合)冻结队伍会导致无法开启自动战斗，建议开启游戏的沿用自动战斗设置。  
2. 游戏画面贴近或超出屏幕显示边缘时功能无法正常执行。  
3. 在执行“历战余响”时若未选择关卡，会导致程序闪退。

未来的更新内容（不代表先后顺序）：
1. 角色试用
2. 账号切换
3. 键位适应
   
感谢您对SRA的支持！  

## 过往的更新公告
beta v0.5 更新公告  
新功能：  
1. 结束对饰品提取的维护，现在可以正常使用该功能。  
2. 新增停止按键，在执行任务后，你可以点击此按键来停止执行。  
3. 体验优化，在进入战斗时如果未启用自动战斗，程序会为你启用，除非你再一次取消。  
4. 外观更新，为程序添加了图标。  
5. 外观更新，调整字体大小，保护视力。  
6. 在常见问题中更新了内容。
   
问题修复：  
1. 修复了在勾选“启动游戏”时手动启动游戏后执行任务会导致程序闪退的问题。  
2. 修复了在未启动游戏且未勾选“启动游戏”时执行任务时会导致程序闪退的问题。  
3. 修复了存在回归任务时，领取巡星之礼异常失败的问题。  
4. 修复了巡星之礼第7天奖励无法领取的问题。
   
beta v0.4 更新公告  
重磅更新：自定义清体力！  
新功能：  
1. 体验优化，现在不需要保持窗口居中，但仍然需要窗口无遮挡。  
2. 体验优化，现在可以记录上一次运行时的选择。  
3. 在常见问题中更新了内容。  
4. 在问题反馈中更新了内容。
   
问题修复：  
1. 修复了某些情况下任务结束未正确返回大世界，导致下一个任务无法执行的问题。  
2. 修复了若干问题。
   
beta v0.3 更新公告  
重磅更新：新增图形化界面！  
新功能：  
1. 新增账号登录功能，输入你的账号和密码后（本地），如果启动游戏时未登录，可以自动登录。  
2. 新增领取巡星之礼功能，现在可以帮你领取巡星之礼。  
3. 现在你可以对功能进行一些更加自由的自定义。  
4. 新增退出游戏功能，在任务结束后，可以选择为你关闭游戏。
   
问题修复：  
1. 修复了某些情况下任务结束未正确返回大世界，导致下一个任务无法执行的问题。  
2. 修复了若干问题。
   
