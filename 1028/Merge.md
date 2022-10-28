# Merge

### 1. Fast Forward

```bash

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge
$ git init
Initialized empty Git repository in C:/Users/multicampus/Desktop/git_merge/.git/

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ touch test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$
 *  복원된 기록 


SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git commit -m "master-1"
[master (root-commit) 3b3b3c5] master-1
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git commit -m "master-2"
[master 8542282] master-2
 1 file changed, 1 insertion(+)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git commit -m "master-3"
[master e6a90fa] master-3
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git log --oneline
e6a90fa (HEAD -> master) master-3
8542282 master-2
3b3b3c5 master-1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git branch hotfix

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git switch hotfix
Switched to branch 'hotfix'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (hotfix)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (hotfix)
$ git commit -m "hotfix-1"
[hotfix 662a816] hotfix-1
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (hotfix)
$ git switch master
Switched to branch 'master'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git merge hotfix
Updating e6a90fa..662a816
Fast-forward
 test.txt | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge (master)
$ git log --oneline
662a816 (HEAD -> master, hotfix) hotfix-1
e6a90fa master-3
8542282 master-2
3b3b3c5 master-1
```

### 2. 3-way Merge

```bash

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way
$ git init
Initialized empty Git repository in C:/Users/multicampus/Desktop/git_merge_3way/.git/

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ touch tset.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git commit -m "master 1"
[master (root-commit) 73d6d15] master 1
 1 file changed, 1 insertion(+)        
 create mode 100644 tset.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git commit -m "master 2"
[master 04e91fa] master 2
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git commit -m "master 3"
[master c98bdce] master 3
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline
c98bdce (HEAD -> master) master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git branch hotfix

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git switch hotfix
Switched to branch 'hotfix'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git commit -m "hotfix 1"
[hotfix 6e11c37] hotfix 1
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git commit -m "hotfix 2"
[hotfix 09020c9] hotfix 2
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git log --oneline
09020c9 (HEAD -> hotfix) hotfix 2
6e11c37 hotfix 1
c98bdce (master) master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git switch master
Switched to branch 'master'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline
c98bdce (HEAD -> master) master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all
09020c9 (hotfix) hotfix 2
6e11c37 hotfix 1
c98bdce (HEAD -> master) master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
* 09020c9 (hotfix) hotfix 2
* 6e11c37 hotfix 1
* c98bdce (HEAD -> master) master 3
* 04e91fa master 2
* 73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ touch master.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        master.txt

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git commit -m "master 4"
[master 80c7509] master 4
 1 file changed, 1 insertion(+)
 create mode 100644 master.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
* 80c7509 (HEAD -> master) master 4
| * 09020c9 (hotfix) hotfix 2
| * 6e11c37 hotfix 1
|/
* c98bdce master 3
* 04e91fa master 2
* 73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git merge hotfix
Merge made by the 'ort' strategy.
 tset.txt | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
*   21bd3a9 (HEAD -> master) Merge branch 'hotfix'
|\
| * 09020c9 (hotfix) hotfix 2
| * 6e11c37 hotfix 1
* | 80c7509 master 4
|/
* c98bdce master 3
* 04e91fa master 2
* 73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git branch -d hotfix
Deleted branch hotfix (was 09020c9).

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
*   21bd3a9 (HEAD -> master) Merge branch 'hotfix'
|\
| * 09020c9 hotfix 2
| * 6e11c37 hotfix 1
* | 80c7509 master 4
|/
* c98bdce master 3
* 04e91fa master 2
* 73d6d15 master 1
```

### 3. Merge Conflict

```bash

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way
$ git init
Initialized empty Git repository in C:/Users/multicampus/Desktop/git_merge_3way/.git/

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ touch tset.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git commit -m "master 1"
[master (root-commit) 73d6d15] master 1
 1 file changed, 1 insertion(+)        
 create mode 100644 tset.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git commit -m "master 2"
[master 04e91fa] master 2
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git commit -m "master 3"
[master c98bdce] master 3
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline
c98bdce (HEAD -> master) master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git branch hotfix

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git switch hotfix
Switched to branch 'hotfix'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git commit -m "hotfix 1"
[hotfix 6e11c37] hotfix 1
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git commit -m "hotfix 2"
[hotfix 09020c9] hotfix 2
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git log --oneline
09020c9 (HEAD -> hotfix) hotfix 2
6e11c37 hotfix 1
c98bdce (master) master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (hotfix)
$ git switch master
Switched to branch 'master'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline
c98bdce (HEAD -> master) master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all
09020c9 (hotfix) hotfix 2
6e11c37 hotfix 1
c98bdce (HEAD -> master) master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
* 09020c9 (hotfix) hotfix 2
* 6e11c37 hotfix 1
* c98bdce (HEAD -> master) master 3
* 04e91fa master 2
* 73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ touch master.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        master.txt

nothing added to commit but untracked files present (use "git add" to track)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git commit -m "master 4"
[master 80c7509] master 4
 1 file changed, 1 insertion(+)
 create mode 100644 master.txt

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
* 80c7509 (HEAD -> master) master 4
| * 09020c9 (hotfix) hotfix 2
| * 6e11c37 hotfix 1
|/
* c98bdce master 3
* 04e91fa master 2
* 73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git merge hotfix
Merge made by the 'ort' strategy.
 tset.txt | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
*   21bd3a9 (HEAD -> master) Merge branch 'hotfix'
|\
| * 09020c9 (hotfix) hotfix 2
| * 6e11c37 hotfix 1
* | 80c7509 master 4
|/
* c98bdce master 3
* 04e91fa master 2
* 73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git branch -d hotfix
Deleted branch hotfix (was 09020c9).

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
*   21bd3a9 (HEAD -> master) Merge branch 'hotfix'
|\
| * 09020c9 hotfix 2
| * 6e11c37 hotfix 1
* | 80c7509 master 4
|/
* c98bdce master 3
* 04e91fa master 2
* 73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline 
21bd3a9 (HEAD -> master) Merge branch 'hotfix'
80c7509 master 4
09020c9 hotfix 2
6e11c37 hotfix 1
c98bdce master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git status
On branch master
nothing to commit, working tree clean

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git brach signup
git: 'brach' is not a git command. See 'git --help'.

The most similar command is
        branch

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git branch signup

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git switch signup
Switched to branch 'signup'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (signup)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (signup)
$ git commit -, "signup 1"
error: unknown switch `,'
usage: git commit [<options>] [--] <pathspec>...

    -q, --quiet           suppress summary after successful commit
    -v, --verbose         show diff in commit message template

Commit message options
    -F, --file <file>     read message from file
    --author <author>     override author for commit
    --date <date>         override date for commit
    -m, --message <message>
                          commit message
    -c, --reedit-message <commit>
                          reuse and edit message from specified commit
    -C, --reuse-message <commit>
                          reuse message from specified commit
    --fixup [(amend|reword):]commit
                          use autosquash formatted message to fixup or amend/reword specified commit
    --squash <commit>     use autosquash formatted message to squash specified commit
    --reset-author        the commit is authored by me now (used with -C/-c/--amend)
    --trailer <trailer>   add custom trailer(s)
    -s, --signoff         add a Signed-off-by trailer
    -t, --template <file>
                          use specified template file
    -e, --edit            force edit of commit
    --cleanup <mode>      how to strip spaces and #comments from message
    --status              include status in commit message template
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit

Commit contents options
    -a, --all             commit all changed files
    -i, --include         add specified files to index for commit
    --interactive         interactively add files
    -p, --patch           interactively add changes
    -o, --only            commit only specified files
    -n, --no-verify       bypass pre-commit and commit-msg hooks
    --dry-run             show what would be committed
    --short               show status concisely
    --branch              show branch information
    --ahead-behind        compute full ahead/behind values
    --porcelain           machine-readable output
    --long                show status in long format (default)
    -z, --null            terminate entries with NUL
    --amend               amend previous commit
    --no-post-rewrite     bypass post-rewrite hook
    -u, --untracked-files[=<mode>]
                          show untracked files, optional modes: all, normal, no. (Default: all)     
    --pathspec-from-file <file>
                          read pathspec from file
    --pathspec-file-nul   with --pathspec-from-file, pathspec elements are separated with NUL character


SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (signup)
$ git commit -m "signup 1"
[signup ea1badc] signup 1
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (signup)
$ git switch master
Switched to branch 'master'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git commit -m "master go"
[master 3d42c21] master go
 1 file changed, 2 insertions(+), 1 deletion(-)

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline
3d42c21 (HEAD -> master) master go
21bd3a9 Merge branch 'hotfix'
80c7509 master 4
09020c9 hotfix 2
6e11c37 hotfix 1
c98bdce master 3
04e91fa master 2
73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline -all -grsph
error: switch `l' expects a numerical value

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline -all -graph
error: switch `l' expects a numerical value

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
* 3d42c21 (HEAD -> master) master go
| * ea1badc (signup) signup 1
|/
*   21bd3a9 Merge branch 'hotfix'
|\
| * 09020c9 hotfix 2
| * 6e11c37 hotfix 1
* | 80c7509 master 4
|/
* c98bdce master 3
* 04e91fa master 2
* 73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git merge signup
Auto-merging master.txt
CONFLICT (content): Merge conflict in master.txt
Automatic merge failed; fix conflicts and then commit the result.

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master|MERGING)
$ git status
On branch master
You have unmerged paths.
Merge branch 'signup'
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   master.txt

no changes added to commit (use "git add" and/or "git commit -a")

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master|MERGING)
$ git add .

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master|MERGING)
$ git commit
[master b747af0] Merge branch 'signup'

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph















SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph















SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$
SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$ git log --oneline --all --graph
*   b747af0 (HEAD -> master) Merge branch 'signup'
|\
| * ea1badc (signup) signup 1
* | 3d42c21 master go
|/
*   21bd3a9 Merge branch 'hotfix'
|\
| * 09020c9 hotfix 2
| * 6e11c37 hotfix 1
* | 80c7509 master 4
|/
* c98bdce master 3
* 04e91fa master 2
* 73d6d15 master 1

SSAFY@DESKTOP MINGW64 ~/Desktop/git_merge_3way (master)
$
```

