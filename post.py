
class Post:
    """
       게시글 클래스
       param id: 글번호
       param titel: 글제목
       param content: 글내용
       param view count: 조회수
    """   
    def __init__(self, id: int, title:str, content: str, view_count: int):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count
    
    def set_post(self, id: int, title: str, content: str, view_count: int):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def add_view_count(self):
        self.view_count += 1  #조회수 1 증가하기
    def get_id(self):
        return self.id
    def get_title(self):
        #if self.title <10:
        return self.title
    def get_content(self):
        return self.content
    def get_view_count(self):
        return self.view_count
    
if  __name__== "__main__":
        post = Post(1, "테스트", "데스트입니다", 0)
        post.set_post(1, "테스트2", "테스트입니다2", 0)
        post.add_view_count()
        print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_view_count()}")    
  
# class Post:
#     """
#        게시글 클래스
#        param id: 글번호
#        param title: 글제목
#        param content: 글내용
#        param view count: 조회수
#        """
#     def __init__(self, id: int, title: str, content: str, view_count: int):
#         self.id = id
#         self.title = title
#         self.content = content
#         self.view_count = view_count

#     def set_post(self, id: int, title: str, content: str, view_count: int): # 4개 한번에 수정
#         self.id = id
#         self.title = title
#         self.content = content
#         self.view_count = view_count
#     def add_view_count(self):
#         self.viewl_count += 1 # 조회수 1 증가하기
#     def get_id(self):
#         return self.id
#     def get_title(self):
#         return self.title
#     def get_content(self)
#         return self.content
#     def get_view_count(self):
#         return self.view_count
    
#     #실제 되는지 확인하기, 메인 실행 블록 
#     if __name__== "__main__":
#         post = Post(1, "테스트", "테스트입니다", 0)
#         post.set_post(1, "테스트2", "테스트입니다2", 0)
#         post.add_view_count()
#         print(f"{post.get_id()}, {post.get_title()}, {post.get_content()}, {post.get_view_count()}")




