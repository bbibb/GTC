CREATE DATABASE Car_Inspection_BB;
GO

USE Car_Inspection_BB;

CREATE TABLE Vehicle
(VIN                CHAR(17)            NOT NULL PRIMARY KEY,
PlateNo             VARCHAR(10)         NOT NULL,
State               CHAR(2)             NOT NULL CHECK (State LIKE '[A-Z][A-Z]'),
Make                VARCHAR(18)         NULL,
YearManufactured    INT                 NOT NULL);

CREATE TABLE Facility
(FacilityIDNo       INT                 IDENTITY PRIMARY KEY,
Name                VARCHAR(40)         NOT NULL,
Street              VARCHAR(40)         NOT NULL,
City                VARCHAR(30)          NOT NULL,
County              VARCHAR(30)         NOT NULL,
ZIP                 VARCHAR(9)          NOT NULL);

CREATE TABLE Inspection
(InspectionNo       INT                 IDENTITY PRIMARY KEY,
InspectDate         DATETIME            NOT NULL,
OdometerReading     DECIMAL(9,2)        NOT NULL CHECK (OdometerReading BETWEEN 0 AND 1000000),
IssuedCertNo        CHAR(12)            NULL,
InspectorCertNo     CHAR(12)            NULL,
VIN                 CHAR(17)            NOT NULL REFERENCES Vehicle (VIN),
FacilityIDNo        INT                 NOT NULL REFERENCES Facility (FacilityIDNo));

CREATE TABLE ProblemMaster
(ProblemCode        CHAR(4)             NOT NULL PRIMARY KEY,
Description         VARCHAR(80)         NOT NULL,
Rejectable          CHAR(1)             NOT NULL CHECK (Rejectable IN ('Y', 'N')),
ActionToTake        VARCHAR(80)         NULL);

CREATE TABLE InspectionProblem
(InspectionProblemNo    INT             IDENTITY PRIMARY KEY,
Reject                  CHAR(1)         NOT NULL CHECK (Reject IN ('P', 'F')),
TirePulled              CHAR(4)         NULL CHECK (TirePulled IN ('FL', 'FR', 'RL', 'RR')),
RepairOrderNo           INT             NULL,
InspectionNo            INT             NOT NULL REFERENCES Inspection (InspectionNo),
ProblemCode             CHAR(4)         NOT NULL REFERENCES ProblemMaster (ProblemCode));




