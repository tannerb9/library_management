INSERT INTO libraryapp_library
  (title, address)
VALUES
  ('Bellview Library', '500 Main Street');


INSERT INTO libraryapp_book
  (title, isbn, year_published, location_id, author, librarian_id)
VALUES
  ('Lamb', 59359409490, 2004, 1, 'Christopher Moore', 1);

INSERT INTO libraryapp_book
  (title, isbn, year_published, location_id, author, librarian_id)
VALUES
  ('Taiko', 4275747474873, 2001, 1, 'Eiji Yoshikawa', 1);

INSERT INTO libraryapp_book
  (title, isbn, year_published, location_id, author, librarian_id)
VALUES
  ('The Golem and the Jinni', 8592475822, 2013, 1, 'Helene Wecker', 2);

INSERT INTO libraryapp_book
  (title, isbn, year_published, location_id, author, librarian_id)
VALUES
  ('The Old Man and the Sea', 8234938989, 1952, 1, 'Ernest Hemingway', 3);

INSERT INTO libraryapp_book
  (title, isbn, year_published, location_id, author, librarian_id)
VALUES
  ('Siddhartha', 8092309209, 1922, 1, 'Herman Hesse', 4);

SELECT
  l.id,
  l.location_id,
  l.user_id,
  u.first_name,
  u.last_name,
  u.email
FROM libraryapp_librarian l
  JOIN auth_user u on l.user_id = u.id;

