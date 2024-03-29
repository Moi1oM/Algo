WITH FILTER AS (
    SELECT CAR_ID
       , COUNT(*) AS CNT
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE >= '2022-08-01' AND START_DATE < '2022-11-01'
    GROUP BY CAR_ID
    ORDER BY CAR_ID DESC
)

SELECT MONTH(START_DATE) AS MONTH
       , C.CAR_ID
       , COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY C INNER JOIN FILTER F
ON  C.CAR_ID = F.CAR_ID
WHERE   F.CNT>=5
        AND START_DATE >= '2022-08-01' AND START_DATE < '2022-11-01'
GROUP BY MONTH(START_DATE), C.CAR_ID
ORDER BY MONTH ASC, CAR_ID DESC