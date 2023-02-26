-- Question 7 dipesh1
SELECT Title
FROM IMDBMovie
WHERE INSTR(Actors,Director)
AND ((Title NOT IN ( SELECT Title FROM NPHDMovies)) OR (Title IN ( SELECT Title FROM NPHDMovies WHERE (Netflix + Hulu + PrimeVideo + Disney = 0))));