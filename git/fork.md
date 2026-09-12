多人协作 Fork 模式下的核心流程总结如下：
**基础配置（首次需要，以后无需重复）**
- 本地仓库绑定总仓库为上游源：
    Bash
    ```
    git remote add upstream https://github.com/tian8168/party-games.git
    ```

**日常标准开发与同步循环（四步法）**
- **开工前同步**：写新代码前拉取总仓库更新，避免落后过多
    Bash
    ```
    git pull upstream main
    ```
    
- **本地编码与提交**：完成功能后保存本地历史：
    Bash
    ```
    git add .
    git commit -m "功能说明"
    ```
- **防冲突合并与推送**：推送前再拉一次总仓库，如有冲突则手动修改并重新提交，确认无误后推送到个人 Fork：
    Bash
    ```
    git pull upstream main
    # 若有冲突，在代码中解决冲突并 git add . && git commit
    git push origin main
    ```
- **合入总仓库**：在 GitHub 页面创建 **Pull Request**，检查通过后点击 **Merge pull request** 完成合入。
**两种场景处理原则**
- **常规协作（保留双方修改）**：使用 `git pull upstream main`，产生冲突时手动保留双方所需代码。
- **极端覆盖（彻底舍弃对方改动）**：仅在重构或全量替换时使用 `git merge -s ours upstream/main`，强制以本地代码覆盖总仓库。