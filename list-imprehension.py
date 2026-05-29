#리스트 내포
# for 사용
# nums = []
# for i in range(5):
#     nums.append(i)

nums = [i for i in range(5)]
print(nums)

nums2 = [100,200,300]
double_nums=[i*2 for i in nums2]
print(double_nums)

#if 사용 순서 중요
nums3 = [i for i in range(10) if i % 2 == 0]
print(nums3)

nums4 = [100,200,300,400,500]
double_nums2 = [i*2 for i in nums4 if i >= 300] #if 가 뒤에, 기능은 먼저
print(double_nums2)

# if1 - 조건에 따라 값을 변경
# → None은 '텅~'으로, 나머지 간식은 그대로 표시
snacks = ['초코파이', None, '쿠크다스', None, '몽쉘']
display_snacks = [snack if snack is not None else '텅~' for snack in snacks] # else 가 있으면 if 가 앞으로
print(display_snacks)

# if2 - 조건에 따라 요소를 필터링 (없는 건 제외)
# None이 아닌 간식만 모아서 리스트 작성
available_snacks = [snack for snack in snacks if snack is not None]
print(available_snacks)
print("hi")