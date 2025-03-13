-- Job 23 : Sélectionner l'étudiant le plus âgé 
SELECT *
    -> FROM etudiant
    -> ORDER BY age DESC
    -> LIMIT 1;