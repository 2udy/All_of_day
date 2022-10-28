```bash

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice
$ git init
Initialized empty Git repository in C:/Users/multicampus/Dit/

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ touch test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be comm
        test.txt

nothing added to commit but untracked files present (use "

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git commit -m "commit 1"
[master (root-commit) 3804c5c] commit 1
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git log
commit 3804c5ca2af09df9ae514428f0200525f90f3352 (HEAD -> m
Author: dongind.oct <dongind.oct@gmail.com>
Date:   Fri Oct 28 09:19:30 2022 +0900

    commit 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committe
  (use "git restore <file>..." to discard changes in worki
        modified:   test.txt

no changes added to commit (use "git add" and/or "git comm

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git restore test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git restore test.txt
\
SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git restore test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committe
  (use "git restore <file>..." to discard changes in worki
        modified:   test.txt

no changes added to commit (use "git add" and/or "git comm

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git restore test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ ^C

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice
$ git init
Initialized empty Git repository in C:/Users/multicampus/Dice/.git/

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be comm
        test.txt

nothing added to commit but untracked files present (use "k)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   test.txt


SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git rm --cached .
fatal: not removing '.' recursively without -r

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   test.txt


SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git rm --cached test.txt
rm 'test.txt'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be comm
        test.txt

nothing added to commit but untracked files present (use "k)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git commit -m "commit 1"
[master (root-commit) ad082c8] commit 1
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committe
  (use "git restore <file>..." to discard changes in worki
        modified:   test.txt

no changes added to commit (use "git add" and/or "git comm

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   test.txt


SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git restore --staged test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committe
  (use "git restore <file>..." to discard changes in worki
        modified:   test.txt

no changes added to commit (use "git add" and/or "git comm

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ ^C

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice
$ git init
Initialized empty Git repository in C:/Users/multicampus/Dice/.git/

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be comm
        test.txt

nothing added to commit but untracked files present (use "k)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   test.txt


SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git commit -m "commit 1"
[master (root-commit) 41bbdd6] commit 1
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git log
commit 41bbdd6fcf3337de656a117babe40726541cf64b (HEAD -> m
Author: dongind.oct <dongind.oct@gmail.com>
Date:   Fri Oct 28 09:34:01 2022 +0900

    commit 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git log --oneline
41bbdd6 (HEAD -> master) commit 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git commit --ammend
error: unknown option `ammend'
usage: git commit [<options>] [--] <pathspec>...

    -q, --quiet           suppress summary after successfu
    -v, --verbose         show diff in commit message temp

Commit message options
    -F, --file <file>     read message from file
    --author <author>     override author for commit
    --date <date>         override date for commit
    -m, --message <message>
                          commit message
    -c, --reedit-message <commit>
                          reuse and edit message from spec
    -C, --reuse-message <commit>
                          reuse message from specified com
    --fixup [(amend|reword):]commit
                          use autosquash formatted messagend/reword specified commit
    --squash <commit>     use autosquash formatted messagefied commit
    --reset-author        the commit is authored by me nowc/--amend)
    --trailer <trailer>   add custom trailer(s)
    -s, --signoff         add a Signed-off-by trailer
    -t, --template <file>
                          use specified template file
    -e, --edit            force edit of commit
    --cleanup <mode>      how to strip spaces and #comment
    --status              include status in commit message
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit

Commit contents options
    -a, --all             commit all changed files
    -i, --include         add specified files to index for
    --interactive         interactively add files
    -p, --patch           interactively add changes
    -o, --only            commit only specified files
    -n, --no-verify       bypass pre-commit and commit-msg
    --dry-run             show what would be committed
    --short               show status concisely
    --branch              show branch information
    --ahead-behind        compute full ahead/behind values
    --porcelain           machine-readable output
    --long                show status in long format (defa
    -z, --null            terminate entries with NUL
    --amend               amend previous commit
    --no-post-rewrite     bypass post-rewrite hook
    -u, --untracked-files[=<mode>]
                          show untracked files, optional ml, no. (Default: all)
    --pathspec-from-file <file>
                          read pathspec from file
    --pathspec-file-nul   with --pathspec-from-file, paths separated with NUL character


SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git commit -ammend
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git co
git: 'co' is not a git command. See 'git --help'.

The most similar commands are
        commit
        clone
        log

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git commit --amend
[master 61f6f0f] new commit 1
 Date: Fri Oct 28 09:34:01 2022 +0900
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git log --oneline
61f6f0f (HEAD -> master) new commit 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ touch test2.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be comm
        test2.txt

nothing added to commit but untracked files present (use "k)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committe
  (use "git restore <file>..." to discard changes in worki
        modified:   test.txt

Untracked files:
  (use "git add <file>..." to include in what will be comm
        test2.txt

no changes added to commit (use "git add" and/or "git comm

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git add test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   test.txt

Untracked files:
  (use "git add <file>..." to include in what will be comm
        test2.txt


SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git commit -m "commit 2"
[master 95f7e40] commit 2
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be comm
        test2.txt

nothing added to commit but untracked files present (use "k)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git log -oneline
fatal: unrecognized argument: -oneline

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git log --oneline
95f7e40 (HEAD -> master) commit 2
61f6f0f new commit 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   test2.txt


SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git log --oneline
95f7e40 (HEAD -> master) commit 2
61f6f0f new commit 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ ^C

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ ^C

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git commit --amend
[master 853054d] add test2 file
 Date: Fri Oct 28 09:41:02 2022 +0900
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 test2.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$ git log --oneline
853054d (HEAD -> master) add test2 file
61f6f0f new commit 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_practice (master)
$

```

