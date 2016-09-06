INSERT INTO "users" (first_name, last_name, email, password)
VALUES ('Harvey', 'Specter', 'harvey@gmail.com', 'blah'),
('Harry', 'Potter', 'quidditch@gmail.com', 'blah'),
('Sherlock', 'Holmes', 'sherlock@mystery.com', 'blah'),
('Chow', 'Chow', 'relationshipmanagerhb@gmail.com', 'blah');

INSERT INTO "recommendations" (relatp_type, rcmdn)
VALUES ('fr', 'Grab drinks'),
('fr', 'Grab dinner'),
('fr', 'Catch a show'),
('fr', 'Run a 5k together'),
('fr', 'Take a vacation'),
('fam', 'Send a text'),
('fam', 'Comment on a recent post made in FaceBook'),
('fam', 'Write them a letter'),
('fam', 'Run a 5k'),
('prf', 'Comment on a recent post made on LinkedIn'),
('prf', 'Grab coffee'),
('prf', 'Send an email');


-- Can't store the phone number with '-' in between bc sql will subtract.
INSERT INTO "relationships" (relatp_type, user_id, first_name, last_name, email, bday, phone, work,
edu, fb, linked_in, twitter, google_plus, github, pinterest,
word_press, yelp, skype, other_social_media)
VALUES ('fr', 1, 'Mike', 'Ross', 'mike@gmail.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7025557928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL,NULL, NULL),
('fam', 1, 'Jessica', 'Pearson', 'jessica@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7027777928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL),
('prf', 1, 'Rachel', 'Zane', 'rachel@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7028887928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL),
('fr', 1, 'Louis', 'Litt', 'louis@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7021117928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL),
('fam', 1, 'Harold', 'Jakowski', 'harold@yahoo.com', to_date('1991-02-26', 'YYYY-MM-DD'),
7022227928, 'Merrill Lynch', 'UNLV', 'yfalcon8FB', 'yfalcon8LI', 'yfalcon8TW',
'yfalcon8G+', 'meetmeup', 'yfalcon8GH', 'yfalcon8PIN', NULL, NULL, NULL);
