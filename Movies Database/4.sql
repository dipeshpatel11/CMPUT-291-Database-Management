-- Question 4 dipesh1
SELECT COUNT(Title)
FROM NPHDMovies
WHERE (Netflix + Hulu + PrimeVideo + Disney) >=3;