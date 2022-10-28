# RESET

```bash

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice
$ git status
fatal: not a git repository (or any of the parent directories): .git

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice
$ cd soft/

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/soft (master)
$ git log --oneline
20d320d (HEAD -> master) third
1eb059e second
6baf32f first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/soft (master)
$ cd ..

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice
$ cd mixed/

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/mixed (master)
$ git log --oneline
20d320d (HEAD -> master) third
1eb059e second
6baf32f first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/mixed (master)
$ git reset --mixed 6baf32f

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/mixed (master)
$ git log --oneline
6baf32f (HEAD -> master) first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/mixed (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        2.txt
        3.txt
        untracked.txt

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/mixed (master)
$ cd ..

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice
$ cd hard/

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/hard (master)
$ git log --oneline
20d320d (HEAD -> master) third
1eb059e second
6baf32f first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/hard (master)
$ git reset --hard 6baf32f
HEAD is now at 6baf32f first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/hard (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        untracked.txt

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/hard (master)
$ git reflog
6baf32f (HEAD -> master) HEAD@{0}: reset: moving to 6baf32f
20d320d HEAD@{1}: commit: third
1eb059e HEAD@{2}: commit: second
6baf32f (HEAD -> master) HEAD@{3}: commit (initial): first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/hard (master)
$ git checkout 20d320d
Note: switching to '20d320d'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 20d320d third

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/hard ((20d320d...))
$ git log --oneline
20d320d (HEAD) third
1eb059e second
6baf32f (master) first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-reset-practice/hard ((20d320d...))
$

```

