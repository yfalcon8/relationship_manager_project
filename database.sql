INSERT INTO "users" (first_name, last_name, email, password)
VALUES ('Yuki', 'Falcon', 'yfalcon8@gmail.com', 'blah'),
('Mao', 'Falcon', 'magicskittle227@yahoo.com', 'blah'),
('Johnny', 'Falcon', 'yfalcon8@yahoo.com', 'blah'),
('Rachel', 'Shen', 'falcony@unlv.nevada.edu.com', 'blah'),
('Chow', 'Chow', 'relationshipmanagerhb@gmail.com', 'blah');

INSERT INTO "recommendations" (relatp_type, rcmdn)
VALUES ('fr', 'Grab drinks'),
('fr', 'Grab dinner'),
('fr', 'Catch a show'),
('fam', 'Send a text'),
('fam', 'Comment on a recent post made in FaceBook'),
('fam', 'wave at them'),
('prf', 'visit their desk'),
('prf', 'hug them'),
('prf', 'cook them dinner');


-- INSERT INTO "events" (user_id, scheduled_at, relatp_id, rcmdn_text)
-- VALUES (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.'),
-- (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.'),;
-- (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.'),
-- (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.'),
-- (3, to_timestamp('2002-12-27 08:32:57', 'dd/mm/yyyy hh24:mi.ss.ff'), 4, 'Grab dinner with him/her.')


-- Can't store the phone number with '-' in between bc sql will subtract.
INSERT INTO "relationships" (relatp_type, user_id, first_name, last_name, email, bday, phone, work,
edu, fb, linked_in, twitter, google_plus, github, pinterest,
word_press, yelp, skype, other_social_media)
VALUES ('fr', 1, 'Minnie', 'Mouse', 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7022907928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL,NULL, NULL),
('fam', 1, 'Mickie', 'Mouse', 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7022907928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL),
('prf', 1, 'Bambi', 'Deer', 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7022907928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL),
('fr', 2, 'Winnie', 'Pooh', 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7022907928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL),
('fam', 2, 'Eeyore', 'Grey', 'yfalcon8@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7022907928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL);

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

