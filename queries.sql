--Add a new user
INSERT INTO users("first_name","last_name","healthyfy_name")
VALUES
("dhanush","gowda","dhanufit1"),
("sami","N","sami"),
("hemanth","C S","hemanthfit"),
("dhruthi","C S","dhruthiii");

--Add a new instructor
INSERT INTO instructors ("first_name","last_name")
VALUES
("mohith","gowda"),
("Thimme","gowda");

--Adding goal
INSERT INTO goals ("name")
VALUES
("lose weight of 5KG"),
("gain weight of 5KG");

--Add goals_acheived
INSERT INTO goals_acheived ("user_id","goal_id","goals_acheived","correctness")
VALUES
(1, 1, "had healthy food, jogged for 2 miles", 1),
(2, 2, "had 5 times healthy food in one single day", 1),
(3, 2, "had food for 3 times in a day", 1),
(4, 1, "had healty salad with fruits, jogged 5 miles",1);

--Adding comments from instructor
INSERT INTO comments ("instructor_id","goals_acheived_id","comments")
VALUES
(1, 1, "keep the food habit as it is and increase the mile of jog"),
(2, 3, "want to eat still more food also exercise "),
(2, 2, "good keep it up");

--Find all goals acheived by user's firstname and lastname
SELECT * FROM goals_acheived
WHERE user_id IN (
    SELECT id FROM users
    WHERE first_name = 'dhanush'
    AND last_name = 'gowda'
    );

--Find all goals acheived by user's healthyfy_name
SELECT * FROM goals_acheived
WHERE user_id IN (
    SELECT id FROM users
    WHERE healthyfy_name = 'dhanufit1'
);

--Find all goals acheived by the goal name
SELECT * FROM goals_acheived
WHERE goal_id IN (
    SELECT id FROM goals
    WHERE name LIKE ('%gain weight%')
);

--Update the comments
UPDATE comments SET comments = "good keep it up"
WHERE goals_acheived_id = 1;

--DELETE all the records of the user of all tables when he decides to quit from the healthyfy
DELETE FROM users WHERE id = 1;
