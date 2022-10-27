class Star:

    type = 'Star'
    x = 100

    def change():
        x = 200
        print('x is ', x)


print('x IS ', Star.x) # 클래스 변수 액세스
Star.change() # 클래스 함수

star = Star()

print(star.x) # 비록 객체 변수로 액세스 했으나 같은 이름의 클래스 변수가 우선

star.change() # Star.change(star)와 동일
