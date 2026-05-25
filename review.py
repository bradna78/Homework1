import os
import csv
from post import Post
file_path = "./data.csv" # 파일 경로 (file_path  는 데이터가 저장될 파일의 위히와 이름을 담고 있는 변수)
post_list = []
#게시글 로딩하기
if os.path.exists(file_path):#
    print("게시글 로딩중...")
    file = open(file_path, 'r', encoding = 'utf8')
    reader = csv.reader(file)
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    file = open(file_path, "w", encoding= 'utf-8', newline= "")
    file.close()
#게시글 쓰기
def write_post():
    print("\n\n- 게시글쓰기-")
    title = input("제목을 입력해주세요>>>\n")
    content = input("본문을 입력해 주세요>>>\n")
    #글번호
    if len(post_list) == 0:
         id = 1
    else:
         id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0) #post 인스턴스 생성
    post_list.append(post) # post 리스트에 저장
    print(f"{post.get_title()} 게시글이 등록되었습니다.")

def update_post(target_post):
    print("\n\n- 게시글 수정 -")
    title = input("제목을 입력해 주세요\n>>>")
    content = input("본문을 입력해 주세요\n>>>")
    target_post.set_post(target_post.id, title, content, target_post.view_count)
    print("#게시글이 수정되었습니다.")

def delete_post(target_post):
    post_list.remove(target_post)
    print("#게시글이 삭제되었습니다.")
    
def detail_post(id):
    print("\n\n- 게시글 상세 -")
    for post in post_list:
        if post.get_id() == id:
            post.add_view_count()
            print("번호 : ", post.get_id())
            print("제목 : ", post.get_title())
            print("본문 : ", post.get_content())
            print("조회수 : ", post.get_view_count())
            target_post = post # target  지정
    while True:
        print("Q)  수정: 1 삭제 : 2 (메뉴로 돌아가려면 -1을 입력)")
        try: # try 가 들어갈 위치!!
            choice = int(input(">>>"))        
            if choice == 1:
                update_post(target_post)
                break
            elif choice == 2:
                delete_post(target_post)
                break
            elif choice == -1:
                break #그냥 돌아감
            else:
                print("잘못 입력했습니다.")
        except ValueError:
            print("숫자를 입력")
        

#게시글 목록 확인
def list_post():
    print("\n\n- 게시글 목록-")
    id_list=[]
    for post in post_list:
        print("번호 : ", post.get_id())
        print("제목 : ", post.get_title())
        print("조회수 : ", post.get_view_count())
        print()
        id_list.append(post.get_id())
    while True:
        print("Q) 글 번호를 선택해주세요 (메뉴로 돌아가려면 -1을 입력해주세요)")
        try:
            id = int(input(">>"))
            if id in id_list:
                detail_post(id) # 함수
                break
            elif id == -1:
                break
            else:
                print("없는 글 번호 입니다.")    
        except ValueError:
            print("숫자를 입력해주세요")

    
    
def save():
    file = open(file_path, "w", encoding= "utf8", newline="")
    writer = csv.writer(file)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    file.close()
    print('#저장이 완료되었습니다.')
    print('#프로그램 종료')

#메뉴 출력하기

while True:
    print("\n\n- My BLOG -")
    print("- 메뉴를 선택해주세요-")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try:
        choice = int(input(">>>"))
    except ValueError:
        print("숫자를 입력해주세요")
    else:
        if choice == 1:
               write_post()
        elif choice == 2:
               list_post()
        elif choice == 3:
               save()
               break