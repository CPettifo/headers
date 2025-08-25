-- Logs the date and country, once user-agent has been abstracted that could be included too
CREATE TABLE logs (
    id SERIAL,
    date DATE,
    country VARCHAR(255)
);