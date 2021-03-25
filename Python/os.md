## 디렉토리 생성

#### os.mkdir()   
> : 해당 위치에 디렉토리 생성.    
> 해당 위치가 존재하지 않는다면 에러 발생.
> 

#### os.makedirs(path, exist_ok=True)   
> : 해당 위치에 디렉토리 생성.   
> 해당 위치가 존재하지 않는다면 중간 폴더들 모두 생성.   
> exist_ok 가 True 가 아니고 해당 위치에 이미 폴더가 존재하면 에러 발생.


## 경로 작업

#### os.path.isdir(path)
> : 디렉토리가 존재하는지 / 디렉토리인지 체크.   

#### os.path.isfile(path)   
> : 파일이 존재하는지 / 파일인지 체크.

#### os.path.sep   
> : 파일 경로 구분자   
> 예시)   
> path.split(os.path.sep) => 경로 토큰 리스트   
> `C:/A/B\\C.txt => [C:, A, B, C.txt]`

## 조작 : 생성 / 이동 / 복사 / 삭제
