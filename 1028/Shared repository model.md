# Shared repository model

```

SSAFY@DESKTOP MINGW64 ~/Desktop
$ git clone https://github.com/2udy/git-practice.git
Cloning into 'git-practice'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

SSAFY@DESKTOP MINGW64 ~/Desktop
$ cd git-practice/

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (master)
$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), 891 bytes | 22.00 KiB/s, done.
From https://github.com/2udy/git-practice
   b0ec121..d86b24f  master     -> origin/master
Updating b0ec121..d86b24f
Fast-forward
 dasomzzang.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 dasomzzang.md

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (master)
$ git branch feature/signup

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (master)
$ git switch feature/signup
Switched to branch 'feature/signup'

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (feature/signup)
$ touch signup.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (feature/signup)
$ git status
On branch feature/signup
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        signup.txt

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (feature/signup)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (feature/signup)
$ git commit -m "daeun txt"
[feature/signup 1a65e27] daeun txt
 1 file changed, 1 insertion(+)
 create mode 100644 signup.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (feature/signup)
$ git push origin feature/signup
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 328 bytes | 328.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'feature/signup' on GitHub by visiting:
remote:      https://github.com/2udy/git-practice/pull/new/feature/signup
remote:
To https://github.com/2udy/git-practice.git
 * [new branch]      feature/signup -> feature/signup

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (feature/signup)
$ git switch
fatal: missing branch or commit argument

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (feature/signup)
$ git switch master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (master)
$ git pull origin master
From https://github.com/2udy/git-practice
 * branch            master     -> FETCH_HEAD
Already up to date.

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (master)
$ git branch -d feature/signup
error: The branch 'feature/signup' is not fully merged.
If you are sure you want to delete it, run 'git branch -D feature/signup'.

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (master)
$ git branch -D feature/signup
Deleted branch feature/signup (was 1a65e27).

SSAFY@DESKTOP MINGW64 ~/Desktop/git-practice (master)
$
