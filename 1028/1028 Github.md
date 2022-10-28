# 1028 Github

### 목차

1. Git undoing
2. Git reset&revert
3. Git branch&merge
4. Git workflow



### Git 구조

#### working directory :arrow_right: staging area  :arrow_right: repository



### 1. Git undoing(작업 단계 간 되돌리기)

- working directory작업단계
  -  `git restore 파일이름`
  - 이전 버전으로 되돌리기
  - 복원 불가
  - 과거 명령어(2.23.0 이전): `git checkout 파일이름`
- staging area 작업단계
  - root-commit이 없는 경우:`git rm --cached` 
  - root-commit이 있는 경우`git restore --staged`
- repository 작업단계
  - `git commit --amend`
  - Staging Area에 새로 올라온 내용이 없는 경우: 직전커밋 메시지만 수정
  - Staging Area에 새로 올라온 내용이 있는 경우: 경우 덮어쓰기



### **2. Git reset&revert**(commit 버전 간 되돌리기)

- reset: 시계를 되돌림
  - `git reset 옵션 커밋ID`
  - 특정 커밋으로 되돌아 갔을 때, 해당 커밋 이후로 쌓였던 커밋들은 전부 사라짐
  - 옵션(되돌아간 커밋 이후의 파일을 저장하는 위치) 
  - :exclamation:질문:exclamation:그러면 3에서 1로 돌아가면 2,3이 남는 건지 2만 남는건지
    - `--soft`: 되돌아간 커밋 이후의 파일들은 Staging Area로 돌려놓음 
    - `--mixed`: working Directory에 남겨놓음. 기본값
    - `--hard`: 아무것도 안남김
  - `git reflog`: 복구 
- revert: 과거의 시점을 없었던 일로 하고 새로 커밋 (무너소리야...?!)
  - `git revert 커밋ID`
  - 협업시 커밋내역 차이로 인한 충돌 방지



### 3. Git branch&merge

- branch : 여러갈래로 작업 공간을 나워 `독립적으로 작업` 할 수 있도록 도와주는 git 도구
  - 장점
    - 원본(master)에 대해 안전함
    - 기능별 브랜치 : 체계적 개발이 가능
    - 빠르고 작은 용량소모
  - 명령어
    - 조회
      - `git brach`: 로컬 저장소의 브랜치 목록
      - `git branch -r`: 원격 저장소의 브랜치 목록
    - 생성
      - `git branch 브랜치이름`: 새로운 브랜치 생성
      - `git branch 브랜치이름 커밋ID`: 특정 커밋 기준으로 브랜치 생성
    - 삭제
      - `git branch -d 브랜치이름`: 병합된 브랜치(개발 완료되었다고 판단)만 삭제 가능
      - `git branch -D 브랜치이름`: 강제 삭제
    - 이동
      - `git switch 브랜치이름`: 다른 브랜치로 이동
      - `git switch -c 브랜치이름`: 브랜치를 새로 생성 및 이동
      - `git switch -c 브랜치이름 커밋ID`: 특정 커밋 기준으로 브랜치 생성 및 이동
      - 스위치 하기 전에 변경 사항을 반드시 커밋 해야함
  - HEAD
    - 현재 브랜치를 가리킨다.
- merge : 분기된 브랜치를 하나로 합치는 명령어
  - `git merge 합칠브랜치이름`
  - `(master) $ git merge hotfix`
  - 메인 브랜치로 스위치 한 후 병합
  - 종류
    - Fast-Forward
      - 빨리감기 처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
    - 3-way Merge
      - 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법
    - Merge Conflict
      - 두 브랜치에서 같은 부분을 수정한 경우

### 4. Git workflow

- 원격 저장소 소유권이 있는 경우: Shared repository model
- 원격 저장소 소유권이 없는 경우: Fork&Pull model
  - Fork: 자신의 소유가 아닌 원격 저장소를 내 원격 저장소에 복제하는 것







##### Vim

**입력모드** `i`

**명령모드**`esc` 

​	저장 및 종료:`:wq` 

​	강제종료: `:q!`

