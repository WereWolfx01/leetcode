CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT e.Salary
      FROM Employee e
      order by e.salary desc
      limit N, 1
  );
END
