-- Job 21 : Compter les étudiants entre 18 et 25 ans
SELECT COUNT(*)
    -> FROM etudiant
    -> WHERE age BETWEEN 18 AND 25;