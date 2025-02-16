--Represents users taking the course
CREATE TABLE "users" (
    id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    healthyfy_name TEXT NOT NULL UNIQUE,
    started NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ("id")
);

--Represents instructors in the course
CREATE TABLE "instructors"(
    id INTEGER,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    PRIMARY KEY ("id")
);

--Represents the goals of the user
CREATE TABLE "goals"(
    id INTEGER,
    name TEXT NOT NULL,
    PRIMARY KEY ("id")
);

--Represents the goals acheived by users
CREATE TABLE "goals_acheived"(
    id INTEGER,
    user_id INTEGER,
    goal_id INTEGER,
    goals_acheived TEXT NOT NULL,
    correctness NUMERIC NOT NULL CHECK("correctness" IN (0, 1)),
    timestamp NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("user_id") REFERENCES users ("id") ON DELETE CASCADE,
    FOREIGN KEY ("goal_id") REFERENCES goals ("id") ON DELETE CASCADE
);

--Represents the comments by the instructor for the user
CREATE TABLE "comments" (
    id INTEGER,
    instructor_id INTEGER,
    goals_acheived_id INTEGER,
    comments TEXT NOT NULL,
    PRIMARY KEY ("id"),
    FOREIGN KEY ("instructor_id") REFERENCES instructors ("id") ON DELETE CASCADE,
    FOREIGN KEY ("goals_acheived_id") REFERENCES goals_acheived ("id") ON DELETE CASCADE
);

--INDEXES FOR EXPECTED COMMON SEARCH
CREATE INDEX "user_name_search" ON users ("first_name","last_name");
CREATE INDEX "user_healthyfy_name_search" ON users ("healthyfy_name");
CREATE INDEX "search_goals_name" ON goals ("name");
CREATE INDEX "search_goals_acheived_id" ON comments("goals_acheived_id");
CREATE INDEX "search_id" ON users ("id");
CREATE INDEX "search_user_id" ON goals_acheived ("user_id");
