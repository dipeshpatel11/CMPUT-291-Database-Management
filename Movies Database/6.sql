-- Question 6 dipesh1
SELECT DISTINCT(I_one.Director)
FROM IMDBMovie I_one , IMDBMovie I_two , NPHDMovies N_one
WHERE I_one.Title != I_two.Title 
AND I_one.Director = I_two.Director 
AND I_one.Title IN (SELECT N_one.Title FROM NPHDMovies N_one WHERE N_one.Disney = 1) 
AND I_two.Title IN (SELECT N_one.Title FROM NPHDMovies N_one WHERE N_one.Disney = 1);