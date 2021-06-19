# IndoorRobot
本项目实现室内引导机器人的后端控制部分。
## 方案
 - 地图->获取书架->路径规划->行进

### 地图部分
 - 提前将室内地图导入程序
 - 地图存储为5-10厘米一格
! Make sure the input topics are published ("$ rostopic hz my_topic") and the timestamps in their header are set.  /rtabmap/rgbd_sync subscribed to (approx sync):    /camera/rgb/image_raw \    /camera/depth/image_raw \
### 获取书本位置
 - 调用api接口
 - 获取书架号

### 路径规划
 - 通过BFS找出最佳路径
 - 原路返回

### 行进部分
 - 通过双目识别前方障碍物
 - 一旦发现障碍物将停下
 - 障碍物清除继续按原路线行进

## 进度
 - 2020/11/7 16:54 创建个人项目
 - 
