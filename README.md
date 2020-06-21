# 해야할것
### 구현해야할 페이지
1. 사장님 페이지 부분수정(일단 페이지만 만들어놨음)
test

# 요청사항
1. 매장수정하는페이지(management_modify.html)부분에서 Django 배울때 블로그 글수정하기 처럼 해줬으면 좋겠습니다.

# 수정사항
## 8/9 07:00
1. 사장님 페이지 실 기능 더 추가
 * 사장님 메뉴 페이지에서 등록된 매장 이름을 클릭시 자세한 정보가 나옴
 * 자세한 정보에서 예약하기 버튼으로 예약 데이터 실 저장 가능
 * 예약 확인하기로 매장에 현제 등록된 예약 데이터 전부 확인 가능
 * 매장목록, 예약목록 페이지네이터로 정렬
 * 매장 상세목록에 지도 API 추가, 추가 정보 입력 없이 데이터베이스 기반
 
 ## 8/9 00:00
1. 사장님 페이지 실 기능 추가
 * 로그인시 가입시 설정했던 타입(사장님, 손님)에 따라 다른 메뉴화면 표시 (예약 확인하기,  매장 관리)
 * 매장 관리 페이지에서 매장 등록기능, 본인 계정에 연결된 매장 목록 표시(css 미적용)
 * 매장 등록시 카카오API 이용하여 자동 입력 가능(본 기능때문에 form 미적용함)
 * 유저 모델 초기화, 데이터 테이블 추가가 아닌 AbstractUser 사용하여 상속받은 모델 생성 후 기본 모델로 지정(Settings.py -> AUTH_USER_MODEL = 'account_user.User')
 
 ## 8/8 18:00
1. 매장 등록 페이지 추가
 * manager/Restaurant_register.html(매장 사진, 음식사진, 매장 주인정보 추가)
 * 카카오로그인버튼 크기 수정
 
## 8/6 17:55
1. 사장님 페이지 추가
 * management.html(매장 관리페이지_예약자현황확인,매장수정하기 기능)
 * management_modify.html(매장 수정페이지)  ==>css 추가 O
 * management_reservation_list.html(매장 관리페이지에서 예약자현황리스트 확인할수있는 페이지)
 
## 8/4 22:00
1. 카카오톡 Api 수정중
2. 데이터베이스 적용 완료, 데이터베이스 오류 수정
3. 기초적인 검색 기능 적용완료

## 8/4 21:00
1. nav-bar 예약현황 확인하기 추가(로그인했을때)
2. CSS Table 이용해서 예약현황 페이지 추가(reservation_list.html)
3. 예약취소완료 페이지 추가(reservation_cancel.html)
4. 메인화면 '도로명 주소로 검색하기' CSS수정(모바일)
5. 사장님메뉴추가
 * 앱추가(account_manager)
 * 로그인페이지추가(manager_signin.html)



 





# likelion_hackathon
# likelion_hackathon
