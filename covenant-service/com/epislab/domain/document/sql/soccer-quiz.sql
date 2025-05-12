-- 001. 전체 축구팀 목록을 팀이름 오름차순으로 출력하시오

select * from team order by team_name asc;

-- 002. 플레이어의 포지션 종류를 나열하시오. 단 중복은 제거하고, 포지션이 없으면 빈공간으로 두시오

select distinct position from player;

-- 003. 플레이어의 포지션 종류를 나열하시오. 단 중복은 제거하고, 포지션이 없으면 '신입' 으로 기재하시오

select distinct case when position is null then '신입' else position end as position from player;

-- 004. 수원팀에서 골키퍼(GK)의 이름을 모두 출력하시오. 단 수원팀 ID는 K02 입니다.

select player_name from player where team_id = 'K02' and position = 'GK';

-- 005. 수원팀에서 성이 고씨이고 키가 170 이상인 선수를 출력하시오. 단 수원팀 ID는 K02 입니다.

select player_name from player where team_id = 'K02' and player_name like '고%' and height >= 170;


-- 005-1. 수원팀의 ID 는 ?

select team_id from team where team_name = '수원';

-- 005-2. 수원팀에서 성이 고씨이고 키가 170 이상인 선수를 출력하시오. (서브쿼리)

select player_name 
from player 
where team_id = (select team_id 
    from team 
    where team_name = '수원') 
        and player_name like '고%' 
        and height >= 170;


-- 006
-- 다음 조건을 만족하는 선수명단을 출력하시오
-- 소속팀이 삼성블루윙즈이거나 
-- 드래곤즈에 소속된 선수들이어야 하고, 
-- 포지션이 미드필더(MF:Midfielder)이어야 한다. 
-- 키는 170 센티미터 이상이고 180 이하여야 한다.

select player_name 
from player 
where team_id in (select team_id from team where team_name in ('삼성블루윙즈', '드래곤즈')) 
    and position = 'MF' 
    and height >= 170 
    and height <= 180;

-- 첫번째 단계, id를 알았을 경우 진행해 봄

select player_name 
from player 
where team_id = (select team_id from team where team_name = '삼성블루윙즈') 
    or team_id = (select team_id from team where team_name = '드래곤즈') 
    and position = 'MF' 
    and height >= 170 


-- 서브쿼리



-- 인라인뷰


-- 007
-- 수원을 연고지로 하는 골키퍼는 누구인가?

select player_name from player where team_id = (select team_id from team where team_name = '수원') and position = 'GK';

-- 008
-- 서울팀 선수들 이름, 키, 몸무게 목록으로 출력하시오
-- 키와 몸무게가 없으면 "0" 으로 표시하시오
-- 키와 몸무게는 내림차순으로 정렬하시오

select player_name, height, weight 
from player 
where team_id = (select team_id from team where team_name = '서울') order by height desc, weight desc;


-- 009
-- 서울팀 선수들 이름과 포지션과
-- 키(cm표시)와 몸무게(kg표시)와  각 선수의 BMI지수를 출력하시오
-- 단, 키와 몸무게가 없으면 "0" 표시하시오
-- BMI는 "NONE" 으로 표시하시오(as bmi)
-- 최종 결과는 이름내림차순으로 정렬하시오

select player_name, height, weight, 
    case when height is null or weight is null then '0' 
        else round(weight / (height * height) * 10000, 2) 
    end as bmi 
from player 
where team_id = (select team_id from team where team_name = '서울') 




-- 010
-- STADIUM 에 등록된 운동장 중에서
-- 홈팀이 없는 경기장까지 전부 나오도록
-- 카운트 값은 19
-- 힌트 : LEFT JOIN 사용해야함

select s.stadium_name, t.team_name  
from stadium s 
left join schedule sc on s.stadium_id = sc.stadium_id 
left join team t on sc.team_id = t.team_id 
where sc.team_id is null;


-- 011
-- 팀과 연고지를 연결해서 출력하시오
-- [팀 명]             [홈구장]
-- 수원[ ]삼성블루윙즈 수원월드컵경기장


-- 012
-- 수원팀 과 대전팀 선수들 중
-- 키가 180 이상 183 이하인 선수들
-- 키, 팀명, 사람명 오름차순

-- 해결방식 1 (조인 방식)



-- 해결방식 1-1 (뷰 생성 )


-- 해결방식 2 (인라인뷰 방식)



-- 서브쿼리 내용 확인



-- 013
-- 모든 선수들 중 포지션을 배정 받지 못한 선수들의 
-- 팀명과 선수이름 출력 둘다 오름차순


-- 014
-- 팀과 스타디움, 스케줄을 조인하여
-- 2012년 3월 17일에 열린 각 경기의
-- 팀이름, 스타디움, 어웨이팀 이름 출력
-- 다중테이블 join 을 찾아서 해결하시오.


-- 015 
-- 2012년 3월 17일 경기에
-- 포항 스틸러스 소속 골키퍼(GK)
-- 선수, 포지션,팀명 (연고지포함),
-- 스타디움, 경기날짜를 구하시오
-- 연고지와 팀이름은 간격을 띄우시오(수원[]삼성블루윙즈)


-- 016 
-- 홈팀이 3점이상 차이로 승리한 경기의
-- 경기장 이름, 경기 일정
-- 홈팀 이름과 원정팀 이름을
-- 구하시오

-- 017
-- 다음 조건을 만족하는 선수명단을 출력하시오
-- 소속팀이 삼성블루윙즈이거나 
-- 드래곤즈에 소속된 선수들이어야 하고, 
-- 포지션이 미드필더(MF:Midfielder)이어야 한다. 
-- 키는 170 센티미터 이상이고 180 이하여야 한다.


-- 018
-- 다음 조건을 만족하는 선수명단을 출력하시오
-- 소속팀이 삼성블루윙즈이거나
-- 드래곤즈에 소속된 선수들이어야 하고,
-- 포지션이 미드필더(MF:Midfielder)이어야 한다.
-- 키는 170 센티미터 이상이고 180 이하여야 한다.


-- 019
-- 전체 축구팀의 목록을 출력하시오
-- 단, 팀명을 오름차순으로 정렬하시오.


-- 020
-- 포지션의 종류를 모두 출력하시오
-- 단, 중복은 제거합니다.


-- 021
-- 포지션의 종류를 모두 출력하시오
-- 단, 중복은 제거합니다.
-- 포지션이 없으면 신입으로 기재



-- 022
-- 수원을 연고지로 하는팀의 골키퍼는
-- 누구인가 ?


-- 023
-- 수원 연고팀에서 키가 170 이상 선수
-- 이면서 성이 고씨인 선수는 누구인가


-- 024
-- 광주팀 선수들 이름과
-- 키와 몸무게 목록을 출력하시오
-- 키와 몸무게가 없으면 "0" 표시하시오
-- 키와 몸무게는  내림차순으로 정렬하시오


-- 025
-- 서울팀 선수들 이름과 포지션과
-- 키(cm표시)와 몸무게(kg표시)와  각 선수의 BMI지수를 출력하시오
-- 단, 키와 몸무게가 없으면 "0" 표시하시오
-- BMI는 "NONE" 으로 표시하시오(as bmi)
-- 최종 결과는 이름내림차순으로 정렬하시오


-- 026
-- 4개의 테이블의 키값을 가지는 가상 테이블을 생성하시오 (join)


-- 027
-- 수원팀(K02) 과 대전팀(K10) 선수들 중 포지션이 골키퍼(GK) 인
-- 선수를 출력하시오
-- 단 , 팀명, 선수명 오름차순 정렬하시오


-- 028
-- 팀과 연고지를 연결해서 출력하시오
-- [팀 명]             [홈구장]
-- 수원[ ]삼성블루윙즈 수원월드컵경기장


-- 029
-- 수원팀(K02) 과 대전팀(K10) 선수들 중
-- 키가 180 이상 183 이하인 선수들
-- 키, 팀명, 사람명 오름차순 (편집됨) 


-- 030
-- 모든 선수들 중 포지션을 배정 받지 못한 선수들의
-- 팀명과 선수이름 출력 둘다 오름차순


-- 031
-- 팀과 스타디움, 스케줄을 조인하여
-- 2012년 3월 17일에 열린 각 경기의
-- 팀이름, 스타디움, 어웨이팀 이름 출력
-- 다중테이블 join 을 찾아서 해결하시오.


-- 032
-- 2012년 3월 17일 경기에
-- 포항 스틸러스 소속 골키퍼(GK)
-- 선수, 포지션,팀명 (연고지포함),
-- 스타디움, 경기날짜를 구하시오
-- 연고지와 팀이름은 간격을 띄우시오(수원[]삼성블루윙즈)


-- 033
-- 홈팀이 3점이상 차이로 승리한 경기의
-- 경기장 이름, 경기 일정
-- 홈팀 이름과 원정팀 이름을
-- 구하시오


-- 034
-- STADIUM 에 등록된 운동장 중에서
-- 홈팀이 없는 경기장까지 전부 나오도록
-- 카운트 값은 19
-- 힌트 : LEFT JOIN 사용해야함


-- 034-1 (페이지네이션) limit 0부터, 5개


-- 034-2 (그룹바이: 집계함수 - 딱 5개 min, max, count, sum, avg)
-- 평균키가 인천 유나이티스팀('K04')의 평균키  보다 작은 팀의
-- 팀ID, 팀명, 평균키 추출
-- 인천 유나이티스팀의 평균키 -- 176.59
-- 키와 몸무게가 없는 칸은 0 값으로 처리한 후 평균값에
-- 포함되지 않도록 하세요.


-- 035
-- 포지션이 MF 인 선수들의 소속팀명 및  선수명, 백넘버 출력


-- 036
-- 가장 키큰 선수 5명 소속팀명 및  선수명, 백넘버 출력,
-- 단 키  값이 없으면 제외


-- 037
-- 선수 자신이 속한 팀의 평균키보다 작은  선수 정보 출력
-- (select round(avg(height),2) from player)


-- 038
-- 2012년 5월 한달간 경기가 있는 경기장  조회