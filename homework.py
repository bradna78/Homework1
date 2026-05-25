#9
data = [1,2,3]
for i in range(5):
  try:
    print(data[i])
  except IndexError:
    print("list index out of range")

#10 #조건문 분기처리!!!!
won = input("원화금액을 입력하세요>>>")
dollar = input("환율을 입력하세요>>>")
try:                               #except 와 final 과 같이 쓴다 #예외가 발생할 수 있는 코드
    print(int(won)/int(dollar))
except ValueError as e:
    print("예외가 발생했습니다.",e)
except ZeroDivisionError as e:
    print("예외가 발생했습니다.",e) # except 여러개 가능


#except: #예외가 발생했을 때 나오게
    #print("예외가 발생했습니다")
# valueerror
#zerodivisionerror

else:
    print("예외가 발생하지 않을때 수행할 코드")
finally:
    print("예외가 발생하던지, 발생하지 않던지 항상 실행되는 코드") # 한글들어가면  ValueError, Finally
per = ["10.31", "", "8.00"]
for i in per:
  try:
    print(float(i))
  except:
    print(0)
  else:
    print("clean data")
  finally:
    print("변환 완료")

#10.1.1
import csv
file = open("./mystock.csv", "w", encoding="utf-8", newline='') #줄바꿈 방지
writer = csv.writer(file) #인스턴스 생성 
writer.writerow(["종목","매입가","수량", "목표가"])  #인스턴스.메서드() ?  #csv파일에 한 줄씩 작성하기
writer.writerow(["삼성전자", "85000","10", "90000"])
writer.writerow(["NAVER", "380000","5","400000"])
file.close()
try:
    with open("mystock.csv","r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines[1:]:
            data = line.strip().split(',')
            name = data[0]
            buy_price = int(data[1])
            quantity = int(data[2])
            target_price = int(data[3])

            profit = (target_price-buy_price)*quantity
            profit_rate = (target_price/buy_price-1)*100
            print(f"{name} {profit} {profit_rate:.2f}%")
except FileNotFoundError:
    print("mystock.csv 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
    



class Post(object):
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
        return self.title
    def get_content(self):
        return self.content
    def get_view_count(self):
        return self.view_count
  