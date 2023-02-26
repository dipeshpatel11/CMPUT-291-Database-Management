-- Question 5 dipesh1
SELECT COUNT(I.Title)
FROM IMDBMovie I, NPHDMovies N
WHERE I.Title=N.Title 
AND (Netflix = 1 AND Hulu = 0 AND PrimeVideo = 0 AND Disney = 0) AND I.Genre LIKE '%Drama%';