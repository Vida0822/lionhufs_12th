
## 실습 과정 

```bash
SHIN HEEMIN@DESKTOP-DGFPD6H MINGW64 /d/Programming/lionhufs/Assignment1
$ git init
Initialized empty Git repository in D:/Programming/lionhufs/Assignment1/.git/

SHIN HEEMIN@DESKTOP-DGFPD6H MINGW64 /d/Programming/lionhufs/Assignment1 (master)
$ git remote add origin https://github.com/Vida0822/lionhufs.git

SHIN HEEMIN@DESKTOP-DGFPD6H MINGW64 /d/Programming/lionhufs/Assignment1 (master)
$ git branch -M main

SHIN HEEMIN@DESKTOP-DGFPD6H MINGW64 /d/Programming/lionhufs/Assignment1 (main)
$ git add .

SHIN HEEMIN@DESKTOP-DGFPD6H MINGW64 /d/Programming/lionhufs/Assignment1 (main)
$ git commit -m "first commit"
[main (root-commit) 2f5303a] first commit
 3 files changed, 148 insertions(+)
 create mode 100644 assignment.html
 create mode 100644 assignmentStyles.css
 create mode 100644 bg.jpg

SHIN HEEMIN@DESKTOP-DGFPD6H MINGW64 /d/Programming/lionhufs/Assignment1 (main)
$ git log
commit 2f5303a5fdbb6948fb6a330efa40fc1d7e2aa9ba (HEAD -> main)
Author: DESKTOP-DGFPD6H\SHIN HEEMIN <sinhimin11@naver.com>
Date:   Mon Mar 25 19:23:28 2024 +0900

    first commit

SHIN HEEMIN@DESKTOP-DGFPD6H MINGW64 /d/Programming/lionhufs/Assignment1 (main)
$ git push -u origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 279.95 KiB | 20.00 MiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/Vida0822/lionhufs.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```





