
### Statements

CREATE DATABASE
CREATE TABLE
CREATE INDEX
CREATE SEQUENCE
CREATE FUNCTION
CREATE PROCEDURE
CREATE TRIGGER
CREATE VIEW

ALTER TABLE
ALTER SEQUENCE
ALTER FUNCTION
ALTER PROCEDURE
ALTER TRIGGER
ALTER VIEW

DROP DATABASE
DROP TABLE
DROP SEQUENCE
DROP FUNCTION
DROP PROCEDURE
DROP TRIGGER
DROP VIEW

CREATE DATABASE New_AP;

### CREATE TABLE

CREATE TABLE table_name
(column1 datatype attributes)
, column2 datatype attributes
, table attributes)

CREATE TABLE Invoices
(InvoiceID    INT    PRIMARY KEY IDENTITY,
 VendorID   INT    NOT NULL,
  InvoiceDate DATE NULL,
   InvoiceTotal MONEY NULL DEFAULT 0);


### Constraints

5 types of constraints
	each can be column-level or table-level, except NULL can't be table-level

NOT NULL
	prevents null values from being stored

PRIMARY KEY
	each row has a unique value in that column
	not null

UNIQUE
	each row must have a unique value in the column
	
CHECK
	limits the values for a column

FOREIGN KEY
REFERENCES
	referential integrity between columns in related tables


### Script to create database

one or more batches
	each is one or more sql statements executed together
	GO is for end of batch
		not needed after last batch

![[CleanShot 2023-11-02 at 22.58.31@2x.jpg]]


