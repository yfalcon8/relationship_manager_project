-- Serial indicates an auto-incrementing integer.
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(20) NOT NULL,
);

-- add REFERENCES relationships to relatp_code once relationships is solidified.
CREATE TABLE recommendations (
    rcmdn_id SERIAL PRIMARY KEY,
    relatp_code INTEGER NOT NULL DEFAULT 100,
    rcmdn TEXT NOT NULL UNIQUE
);

-- CREATE TABLE events (
--     event_id SERIAL PRIMARY KEY,
--     user_id INTEGER REFERENCES users,
--     scheduled_at TIMESTAMP NOT NULL,
--     relatp_id INTEGER REFERENCES relationships,
--     rcmdn_text TEXT NOT NULL
-- );

CREATE TABLE relationships (
    relatp_id SERIAL PRIMARY KEY,
    relatp_code INTEGER NOT NULL DEFAULT 100,
    user_id INTEGER,
    email VARCHAR(50),
    bday DATE,
    phone VARCHAR(15),
    work VARCHAR(50),
    edu VARCHAR(50),
    fb VARCHAR(50),
    linked_in VARCHAR(50),
    twitter VARCHAR(50),
    google_plus VARCHAR(50),
    meet_up VARCHAR(50),
    github VARCHAR(50),
    pinterest VARCHAR(50),
    reddit VARCHAR(50),
    word_press VARCHAR(50),
    yelp VARCHAR(50),
    youtube VARCHAR(50),
    skype VARCHAR(50),
    other_social_media VARCHAR(50)
);

-- CREATE TABLE rcmdns_relatps (
--     rcmdnRelatp_id SERIAL PRIMARY KEY,
--     rcmdn_id INTEGER NOT NULL REFERENCES recommendations,
--     relatp_code INTEGER NOT NULL REFERENCES recommendations DEFAULT 100
-- );

-- CREATE TABLE gift_ideas (
--     gift_idea_id SERIAL PRIMARY KEY,
--     gift_idea TEXT
-- );

-- CREATE TABLE goals (
--     goal_id SERIAL PRIMARY KEY,
--     goal TEXT
-- );

-- CREATE TABLE notes (
--     note_id SERIAL PRIMARY KEY,
--     note TEXT
-- );

-- CREATE TABLE pets (
--     pet_id SERIAL PRIMARY KEY,
--     pet TEXT
-- );

-- CREATE TABLE family (
--     famliy_id SERIAL PRIMARY KEY,
--     family TEXT
-- );

-- CREATE TABLE hobbies (
--     hobby_id SERIAL PRIMARY KEY,
--     hobby TEXT
-- );

-- CREATE TABLE likes (
--     like_id SERIAL PRIMARY KEY,
--     likes TEXT
-- );

-- CREATE TABLE dislikes (
--     dislike_id SERIAL PRIMARY KEY,
--     dislike TEXT
-- );

-- CREATE TABLE pet_peeves (
--     pet_peeve_id SERIAL PRIMARY KEY,
--     pet_peeve TEXT
-- );

-- CREATE TABLE fav_foods (
--     fav_food_id SERIAL PRIMARY KEY,
--     fav_food TEXT
-- );

-- CREATE TABLE fav_drinks (
--     fav_drink_id SERIAL PRIMARY KEY,
--     fav_drink TEXT
-- );

-- CREATE TABLE fav_restaurants (
--     fav_restaurant_id SERIAL PRIMARY KEY,
--     fav_restaurant TEXT
-- );

-- CREATE TABLE fav_sports_teams (
--     fav_sports_team_id SERIAL PRIMARY KEY,
--     fav_sports_team TEXT
-- );

-- CREATE TABLE fav_brands (
--     fav_brand_id SERIAL PRIMARY KEY,
--     fav_brand TEXT
-- );

-- CREATE TABLE other_favs (
--     other_favs_id SERIAL PRIMARY KEY,
--     other_fav TEXT
-- );

-- CREATE TABLE convo_log (
--     convo_log_id SERIAL PRIMARY KEY,
--     convo TEXT
-- );

-- CREATE TABLE traits (
--     trait_id SERIAL PRIMARY KEY,
--     trait TEXT
-- );

INSERT INTO "users" (first_name, last_name, email, password, bday)
VALUES ('Yuki', 'Falcon', 'yfalcon8@gmail.com', 'blah', to_date('1991-02-27', 'YYYY-MM-DD')),
('Mao', 'Falcon', 'magicskittle227@yahoo.com', 'blah', to_date('1980-02-27', 'YYYY-MM-DD')),
('Johnny', 'Falcon', 'yfalcon8@yahoo.com', 'blah', to_date('1970-02-27', 'YYYY-MM-DD')),
('Rachel', 'Shen', 'falcony@unlv.nevada.edu.com', 'blah', to_date('1991-02-26', 'YYYY-MM-DD')),
('Chow', 'Chow', 'relationshipmanagerhb@gmail.com', 'blah', to_date('1950-02-27', 'YYYY-MM-DD'));

INSERT INTO "recommendations" (rcmdn)
VALUES ('Grab drinks'),
('Grab dinner'),
('Catch a show'),
('Send a text'),
('Comment on a recent post made in FaceBook');

-- INSERT INTO "events" (user_id, scheduled_at, relatp_id, rcmdn_text)
-- VALUES (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.'),
-- (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.'),;
-- (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.'),
-- (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.'),
-- (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.')

-- INSERT INTO "relationships" (relatp_code, user_id, email, bday, phone, work,
-- edu, fb, linked_in, twitter, google_plus, meet_up, github, pinterest, reddit,
-- word_press, yelp, youtube, skype, other_social_media)
-- VALUES (200, 6, 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
-- 702-290-7928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
-- 'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL, NULL,
-- NULL, NULL)
-- (200, 6, 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
-- 702-290-7928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
-- 'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL, NULL,
-- NULL, NULL)
-- (200, 6, 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
-- 702-290-7928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
-- 'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL, NULL,
-- NULL, NULL)
-- (200, 6, 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
-- 702-290-7928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
-- 'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL, NULL,
-- NULL, NULL)
-- (200, 6, 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
-- 702-290-7928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
-- 'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL, NULL,
-- NULL, NULL);

-- INSERT INTO "rcmdns_relatps" (rcmdn_id, relatp_code)
-- VALUES (4, 200),
-- (4, 200),
-- (4, 200),
-- (4, 200),
-- (4, 200);

-- INSERT INTO "gift_ideas" (gift_idea)
-- VALUES ('Tickets to Stephen Colbert Show'),
-- ('Tickets to Stephen Colbert Show'),
-- ('Tickets to Stephen Colbert Show'),
-- ('Tickets to Stephen Colbert Show'),
-- ('Tickets to Stephen Colbert Show');

-- INSERT INTO "goals" (goal)
-- VALUES ('Become an expert networker.'),
-- ('Become an expert networker.'),
-- ('Become an expert networker.'),
-- ('Become an expert networker.'),
-- ('Become an expert networker.');

-- INSERT INTO "notes" (note)
-- VALUES ('Paige is planning a vacation to the Bahamas in July.'),
-- ('Paige is planning a vacation to the Bahamas in July.'),
-- ('Paige is planning a vacation to the Bahamas in July.'),
-- ('Paige is planning a vacation to the Bahamas in July.'),
-- ('Paige is planning a vacation to the Bahamas in July.');

-- INSERT INTO "pets" (pet)
-- VALUES ('Chow Chow - Goliath'),
-- ('Chow Chow - Goliath'),
-- ('Chow Chow - Goliath'),
-- ('Chow Chow - Goliath'),
-- ('Chow Chow - Goliath');

-- INSERT INTO "family" (family)
-- VALUES ('Daughter - Emily');

-- INSERT INTO "hobbies" (hobby)
-- VALUES ('yoga');

-- INSERT INTO "likes" (likes)
-- VALUES ('Sherlock - Netflix');

-- INSERT INTO "dislikes" (dislike)
-- VALUES ('mustard');

-- INSERT INTO "pet_peeves" (pet_peeve)
-- VALUES ('Impatient finger-tapping.');

-- INSERT INTO "fav_foods" (fav_food)
-- VALUES ('Pad See Ew');

-- INSERT INTO "fav_drinks" (fav_drink)
-- VALUES ('Hot milk tea with boba');

-- INSERT INTO "fav_restaurants" (fav_restaurant)
-- VALUES ('Mizumi at the Wynn');

-- INSERT INTO "fav_sports_teams" (fav_sports_team)
-- VALUES ('Green Bay Pakcers');

-- INSERT INTO "fav_brands" (fav_brand)
-- VALUES ('Michael Kors');

-- INSERT INTO "other_favs" (other_fav)
-- VALUES ('Unhealthy obsession with Costco');

-- INSERT INTO "convo_log" (convo)
-- VALUES ('Mom is getting knee surgery.');

-- INSERT INTO "traits" (trait)
-- VALUES ('Dry humor');

