## git note 

### 命令记录

- git 初始化命令

``` bash
git init
```

- 文件状态命令

  ``` bash
  git status
  ```

- 管理指定文件

  ``` bash
  git add 文件名
  git add .
  ```

- 个人信息配置：用户名&邮箱

  ```bash
  git config --global user.email "wboy1999@qq.com"
  git config --global user.name "wboy"
  ```

- 生成（提交）版本

  ``` bash
  git commit -m '描述信息'
  ```

- 查看提交信息

  ``` bash
  git log
  ```

- 版本回滚

  ``` bash
  # 查看提交记录
  git log
  git reset --hard 版本号
  ```

- 回滚恢复

  ``` bash
  # 查看全部提交记录
  git reflog
  git reset --hard 版本号
  ```

  