-- Postgresql
CREATE TABLE "user" (
    "user_id" SERIAL PRIMARY KEY,
    "user_name" VARCHAR,
    "user_second_name" VARCHAR,
    "user_nickname" VARCHAR,
    "user_email" VARCHAR,
    "user_active" boolean NOT NULL DEFAULT TRUE,
    "user_blocked_date" timestamp,
    "user_login_date" timestamp
);

CREATE TABLE "comment" (
  "comment_id" SERIAL PRIMARY KEY,
  "comment_created" timestamp NOT NULL DEFAULT now(),
  "text" TEXT NOT NULL

);

ALTER TABLE "comment" ADD "user_id" INTEGER NOT NULL,
    ADD CONSTRAINT "fk_comment_user_id" FOREIGN KEY ("user_id")
    REFERENCES "user" ("user_id");

CREATE INDEX user_user_name_index
  ON "user" (user_name);


CREATE OR REPLACE FUNCTION blocked_date()
RETURNS TRIGGER
AS $$
BEGIN
  NEW.user_blocked_date = now();
  RETURN NEW;
END;
$$ LANGUAGE 'plpgsql';

CREATE TRIGGER set_user_blocked_date AFTER UPDATE ON "user"
FOR EACH ROW WHEN(NEW.user_active IS FALSE) EXECUTE PROCEDURE blocked_date();

-- Statements
-- 1. search the first name of user with the biggest amount of dayly comments
SELECT "user".user_name
FROM "comment"
LEFT JOIN "user" ON "user".user_id = "comment".user_id
Group by "comment".user_id, "user".user_name
Order by count(date_trunc('day', comment_created)) desc LIMIT 10;

-- 2. block the first 10 users without comments
UPDATE "user"
SET user_active = FALSE
WHERE user_id IN
			( SELECT user_id
	      FROM "user"
	      WHERE "user".user_id NOT IN
							(SELECT DISTINCT user_id
						   FROM "comment"
					     )
				LIMIT 10
		 );

-- 3. select a list of users blocked 1 years ago but with attempts of authorization for a last month
SELECT * FROM "user"
WHERE EXTRACT(year FROM "user".user_blocked_date) = EXTRACT(YEAR from current_timestamp - INTERVAL '1 year')
AND "user".user_login_date <= current_timestamp - INTERVAL '1 month';

