-- Question 9 dipesh1
SELECT 'Netflix', N.Title, MAX(Revenue)
FROM IMDBMovie I, NPHDMovies N
WHERE N.Title = I.Title AND N.Netflix = 1
UNION
SELECT 'Hulu', N.Title, MAX(Revenue)
FROM IMDBMovie I, NPHDMovies N
WHERE N.Title = I.Title AND N.Hulu = 1
UNION
SELECT 'Prime Video', N.Title, MAX(Revenue)
FROM IMDBMovie I, NPHDMovies N
WHERE N.Title = I.Title AND N.PrimeVideo = 1
UNION
SELECT 'Disney', N.Title, MAX(Revenue)
FROM IMDBMovie I, NPHDMovies N
WHERE N.Title = I.Title AND N.Disney = 1;