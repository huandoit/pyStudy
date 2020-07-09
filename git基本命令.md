> https://www.yiibai.com/git/git-quick-start.html

1. 一些必须命令：
- `git clone`
- `git add [filename]`
- `git status`

2. git stash
- 将当前工作区已修改的内容缓存到git栈中，工作区将显示上一次commit时的代码
- 使用场景1：当前工作区的修改未提交到git中，但是想从git上pull最新代码，可以先将本次修改git stach后再pull
- 使用场景2：为了fix一个紧急的bug，先stash，使返回到自己上一个commit，改完bug之后再stash pop，继续原来的工作
- 配套的命令：
    - `git stash list`：将git栈中所有的缓存信息打印出来
    - `git stash pop`：将最新一次缓存的内容恢复到当前工作区，同时将git栈中的该缓存记录清除
    - `git stash apply`：将缓存堆栈中的stash多次应用到工作目录中，但并不删除stash拷贝
    - `git stash show stash@{X}`：查看对应stash的具体缓存内容
    - `git stash save ""`：在保存时添加说明
    
3. git remote
- 管理跟踪的存储库
- 不带参数 列出已经存在的远程分支
- `git remote -v` 列出远程仓库的详细地址信息

4. git branch
- 用于列出、创建或删除分支
- `git branch` 查看本地分支
- `git branch branch_name` 在本地创建分支branch_name
- `git branch -a` 查看本地及远程仓库的所有分支
- `git branch -d` 删除分支

5. git checkout
- 用于切换分支或恢复工作树文件
- `git checkout branch_name` 切换分支到branch_name上
- `git checkout -b branch_name` 创建并切换到branch_name分支上

6. git push
- 用于将本地分支的更新推送到远程主机

7. git status

8. git diff

9. git merge