# Fork&

```

SSAFY@DESKTOP MINGW64 ~/Desktop
$ git clone https://github.com/2udy/fork-practice.git
Cloning into 'fork-practice'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

SSAFY@DESKTOP MINGW64 ~/Desktop
$ git branch login
fatal: not a git repository (or any of the parent directories): .git

SSAFY@DESKTOP MINGW64 ~/Desktop
$ cd fork-practice/

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (master)
$ git branch login

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (master)
$ switch login
bash: switch: command not found

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (master)
$ git switch login
Switched to branch 'login'

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (login)
$ touch test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (login)
$ open test.txt
bash: open: command not found

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (login)
$ git status
On branch login
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        test.txt

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (login)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (login)
$ git commit -m "commit 1"
[login 2ef96bd] commit 1
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (login)
$ git push origin login
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 270 bytes | 270.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'login' on GitHub by visiting:
remote:      https://github.com/2udy/fork-practice/pull/new/login
remote:
To https://github.com/2udy/fork-practice.git
 * [new branch]      login -> login

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (login)
$ git switch master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (master)
$ git remote add upstream https://github.com/edujunho/fork-practice.git

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (master)
$ git remote -v
origin  https://github.com/2udy/fork-practice.git (fetch)
origin  https://github.com/2udy/fork-practice.git (push)
upstream        https://github.com/edujunho/fork-practice.git (fetch)
upstream        https://github.com/edujunho/fork-practice.git (push)

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (master)
$ git pull upstream master
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), 875 bytes | 67.00 KiB/s, done.
From https://github.com/edujunho/fork-practice
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/master
Updating 10c65e9..ca1d64e
Fast-forward
 test.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (master)
$ git branch -D login
Deleted branch login (was 2ef96bd).

SSAFY@DESKTOP MINGW64 ~/Desktop/fork-practice (master)
$

```

