# Brach

```bash

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ touch test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git commit -m "master-1"
[master (root-commit) 92d2d04] master-1
 1 file changed, 1 insertion(+)        
 create mode 100644 test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git commit -m "master-2"
[master 0e3477c] master-2
 1 file changed, 1 insertion(+)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git commit -m "master-3"
[master e39ce06] master-3
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git log --oneline
e39ce06 (HEAD -> master) master-3
0e3477c master-2
92d2d04 master-1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git branch login

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git log --oneline
e39ce06 (HEAD -> master, login) master-3
0e3477c master-2
92d2d04 master-1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git branch
  login
* master

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test.txt

no changes added to commit (use "git add" and/or "git commit -a")

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git commit -m "master-4"
[master ec13153] master-4
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git log --oneline
ec13153 (HEAD -> master) master-4
e39ce06 (login) master-3
0e3477c master-2
92d2d04 master-1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (master)
$ git switch login
Switched to branch 'login'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (login)
$ git log --oneline
e39ce06 (HEAD -> login) master-3
0e3477c master-2
92d2d04 master-1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (login)
$ git log --oneline --all
ec13153 (master) master-4
e39ce06 (HEAD -> login) master-3
0e3477c master-2
92d2d04 master-1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (login)
$ git status
On branch login
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   test.txt

no changes added to commit (use "git add" and/or "git commit -a")

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (login)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (login)
$ git commit -m "login-1"
[login 3406676] login-1
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (login)
$ git log --oneline
3406676 (HEAD -> login) login-1
e39ce06 master-3
0e3477c master-2
92d2d04 master-1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (login)
$ git log --oneline --all
3406676 (HEAD -> login) login-1
ec13153 (master) master-4
e39ce06 master-3
0e3477c master-2
92d2d04 master-1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (login)
$ git log --oneline --all --graph
* 3406676 (HEAD -> login) login-1
| * ec13153 (master) master-4
|/
* e39ce06 master-3
* 0e3477c master-2
* 92d2d04 master-1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_branch (login)
$
```

