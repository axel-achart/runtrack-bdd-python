-- Job 14 : Trier les étudiants entre 18 et 25 ans et par ordre croissant
SELECT *
    -> FROM etudiant
    -> WHERE age BETWEEN 18 AND 25
    -> ORDER BY age ASC;