# REVERT

```bash
Revert "second"

SSAFY@DESKTOP MINGW64 ~/Downloads/git-revert-practice (master)
$ git log --oneline
20d320d (HEAD -> master) third
1eb059e second
6baf32f first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-revert-practice (master)
$ git revert 1eb059e
[master d53318c] Revert "second"
 1 file changed, 1 deletion(-)  
 delete mode 100644 2.txt       

SSAFY@DESKTOP MINGW64 ~/Downloads/git-revert-practice (master)
$ git log --oneline
d53318c (HEAD -> master) Revert "second"
20d320d third
1eb059e second
6baf32f first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-revert-practice (master)
$ git log
commit d53318cb17bc24fbf1acf81e896e3366b62137cc (HEAD -> master)
Author: dongind.oct <dongind.oct@gmail.com>
Date:   Fri Oct 28 10:28:16 2022 +0900

    Revert "second"

    This reverts commit 1eb059eac1e3051a31d84188f80e1ae5626dd2c3.

commit 20d320d4b5327fbebddc0e1ccdf27415e91d0289
Author: harryjjun <harry@hphk.kr>
Date:   Fri Apr 15 02:32:02 2022 +0900

    third

commit 1eb059eac1e3051a31d84188f80e1ae5626dd2c3
Author: harryjjun <harry@hphk.kr>
Date:   Fri Apr 15 02:31:54 2022 +0900

    second

commit 6baf32fc513509f568c785dbcc8bef6e03f7b567
Author: harryjjun <harry@hphk.kr>
Date:   Fri Apr 15 02:31:30 2022 +0900

    first

SSAFY@DESKTOP MINGW64 ~/Downloads/git-revert-practice (master)
$

SSAFY@DESKTOP MINGW64 ~/Downloads/git-revert-practice (master)
$
```

