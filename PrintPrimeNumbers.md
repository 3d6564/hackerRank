```sql
/*
Creator: crobinson89
Date: 20210812
Purpose: Create a MS SQL Server script that will correctly calculate prime numbers with an ampersand (&) between each digit. The result is printed to output.
*/
DECLARE @i INT = 1;
DECLARE @output VARCHAR(3000) = '';

WHILE @i < 1000
BEGIN
    IF @i = 2
    BEGIN
        SET @output += CAST(@i as varchar(1000));
    END
    
    ELSE IF @i = 3
    BEGIN
        SET @output += '&' + CAST(@i as varchar(1000));
    END
    
    ELSE IF (@i % 2 = 0 OR @i % 3 = 0) AND @i > 3
    BEGIN
        SET @output = @output;
    END
    
    ELSE
    BEGIN
        DECLARE @m int=5;
        DECLARE @c int=0;
        WHILE (SQUARE(@m) <= @i)
        BEGIN
            IF (@i % @m = 0 OR @i % (@m + 2) = 0) AND @i > 3
            BEGIN
                SET @c += 1;   
            END
            SET @m += 6
        END
        IF @c = 0 AND @i > 1
        BEGIN
            SET @output += '&' + CAST(@i as varchar(1000));
        END
    END
    SET @i += 1;
END

PRINT(@output);
```
