# Git 命令教學


## 開始使用

```sh
git init # 初始化git
git clone XXXXXXX # 放連結至XXXXX，可以是github, bitbucket 或其他地方

# 選擇 1
git branch wei # 建立一個wei
git checkout wei # 切換到wei

# 選擇 2
git checkout -b wei # 創建並直接切換到wei，等於同時做選擇 1 的兩個動作
```

## 當你想刪除wei時
### 要注意主分支 master/main 不能刪除
#### 假設今天有一個branch叫做wei，我們要刪除wei這個branch
```sh
git checkout master # 一定要先切換至master，否則無法刪除
git branch -d wei # 刪除wei這個branch (如果遇到錯誤，把d換成D即可改成強制刪除)
git push origin :wei # 將遠端的branch刪除 (github/bitbucket等等)
```

## 如果 master 有更新，wei一定要更新 (視更薪幅度/內容決定，但基本上是一定要)

```sh
git checkout master # 首先要切回主分支
git pull origin master # 將遠端的主分支拉回本地 (會直接覆蓋掉)
git checkout wei # 切回wei
git merge master # 將剛剛拉回的主分支更新合併到wei (這段將會把最新的本地master合併至你目前所在的branch)
git push origin wei # 將wei推上遠端
```

## 如果 master 有更新，同時wei也剛好有更新
### 建議先把最新的master拉回本地，再把最新的本地master合併至本地wei
### 最後再開始更新wei的部分以避免衝突 (可以把code拉到別的視窗後再視情況去增加/減少)

```sh
git checkout master # 首先要切回主分支
git pull origin master # 將遠端的主分支拉回本地 (會直接覆蓋掉)
git checkout wei # 切回wei
git merge master # 將剛剛拉回的主分支更新合併到wei (這段將會把最新的本地master合併至你目前所在的branch)
開始修改你的更新，更新完畢後...
git push origin wei # 將wei推上遠端
注意，如果兩個branch有更改到同一條代碼，就會報錯，這時候就要手動去檢查
剩下待補
```

## git rebase to combine commits
### 假設你有一個branch叫做wei，你想要把wei的最後兩個commit合併成一個
```sh
git checkout wei # 切回wei
git rebase -i HEAD~2 # 這個指令會打開一個編輯器，你可以選擇要合併的commit
# 這時會看見
pick 1a2b3c4 commit 1
pick 4d5e6f7 commit 2
# 你可以把commit 2的pick改成squash，然後存檔
# 改完以後
pick 1a2b3c4 commit 1
squash 4d5e6f7 commit 2
# 這時候你可以修改commit 2的訊息，然後存檔
# 這時候你的commit就會合併成一個了

額外功能
git rebase --abort # 可以取消剛剛的rebase操作可重新來過
```