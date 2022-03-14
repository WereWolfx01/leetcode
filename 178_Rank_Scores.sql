/* Write your T-SQL query statement below */
SELECT
  Score,
  (
    SELECT
      count(*)
    FROM
      (
        SELECT
          DISTINCT Score s
        FROM
          Scores
      ) tmp
    WHERE
      s >= Score
  ) Rank
FROM
  Scores
ORDER BY
  Score DESC
