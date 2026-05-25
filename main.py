import os
import csv
from post import Post
#파일경로
file_path = "./data.csv"

# 게시글 저장할 리스트
post_list = []

# data.csv 파일 있다면
if os.path.exists(file_path):
    # 게시글 로딩
    print("게시글 로딩중...")
    file = open(file_path, 'r', encoding = 'utf8')
    reader = csv.reader(file)
    for data in reader:
        #Post 인스턴스 생성하기
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    #파일 생성하기
    file = open(file_path, "w", encoding= "utf-8", newline="")
    file.close()

def write_post():
    print("\n\n- 게시글 쓰기 -")
    


def list_post():
    pass
def save():
    file = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(file)
    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    file.close()
    print("#저장이 완료되었습니다.")
    print("#프로그램 종료")

while True:
    print("\n\n- My BLOG -")
    print("- 메뉴를 선택해주세요 - ")
    print("1. 게시글 쓰기")    
    print("2. 게시글 목록")
    print("3.  프로그램 종료")
    try:
        choice = int(input(">>>")) #
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



