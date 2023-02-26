-- Question 8 dipesh1
SELECT N1.Year, COUNT(*)
FROM NPHDMovies N1, IMDBMovie I1
WHERE N1.Title = I1.Title
AND N1.Year IN (SELECT DISTINCT Year FROM NPHDMovies N2)
AND N1.PrimeVideo = 1
AND I1.Genre LIKE '%drama%'
GROUP BY N1.Year
UNION
SELECT DISTINCT Year, 'NULL'
FROM NPHDMovies N3
WHERE Year NOT IN (SELECT DISTINCT Year FROM NPHDMovies N4, IMDBMovie I4 WHERE N4.Title = I4.Title AND N4.PrimeVideo = 1 AND I4.Genre LIKE '%drama%')
ORDER BY Year;
