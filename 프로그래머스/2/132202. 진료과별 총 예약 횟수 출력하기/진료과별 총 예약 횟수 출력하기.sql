# 22년 5월에 예약 환자 수를 진료과코드 별로조회 AS 진료과 코드, 5월예약건수
# 환자 수 기준 오름차순, 진료과 코드 기준 오름차순
SELECT MCDP_CD AS 진료과코드, COUNT(MCDP_CD) AS 5월예약건수
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = 2022 AND MONTH(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY 5월예약건수, 진료과코드