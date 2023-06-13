CREATE PROCEDURE searchRecommendation
    @berat FLOAT,
    @menit INT,
    @calories FLOAT
AS
    DECLARE
        @caloriesPerOneKg FLOAT
    
    SET @caloriesPerOneKg = @calories / @berat / @menit

    CREATE TABLE #jarakTemporary
    (
        namaExercise VARCHAR(255),
        calories FLOAT,
        caloriesTarget FLOAT,
        jarak FLOAT
    )

    INSERT INTO #jarakTemporary
    SELECT
        namaExercise,
        calories,
        @caloriesPerOneKg,
        (ABS(calories-@caloriesPerOneKg))
    FROM
        exercise
    CROSS JOIN 
        @caloriesPerOneKg

    SELECT
        TOP (5) namaExercise
    FROM 
        #jarakTemporary
    ORDER BY
        jarak ASC