INSERT INTO "users" (first_name, last_name, email, password)
VALUES ('Yuki', 'Falcon', 'yfalcon8@gmail.com', 'blah'),
('Harry', 'Potter', 'quidditch@gmail.com', 'blah'),
('Sherlock', 'Holmes', 'sherlock@mystery.com', 'blah'),
('Harvey', 'Specter', 'harvey@gmail.com', 'blah'),
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
