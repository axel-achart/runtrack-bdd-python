-- Job 20 : Compter les étudiants mineurs
SELECT COUNT(*)
    -> FROM etudiant
    -> WHERE age < 18;