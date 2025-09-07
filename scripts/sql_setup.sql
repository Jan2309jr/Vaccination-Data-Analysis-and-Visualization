CREATE DATABASE IF NOT EXISTS vaccination_db;
USE vaccination_db;

-- Lookup Tables
CREATE TABLE Countries (
    CountryCode CHAR(3) PRIMARY KEY,
    CountryName VARCHAR(100) NOT NULL,
    WHORegion VARCHAR(50)
);

CREATE TABLE Vaccines (
    VaccineCode VARCHAR(20) PRIMARY KEY,
    VaccineDescription VARCHAR(255) NOT NULL
);

CREATE TABLE Diseases (
    DiseaseCode VARCHAR(20) PRIMARY KEY,
    DiseaseDescription VARCHAR(255) NOT NULL
);

-- Fact Tables with YEAR datatype for year columns
CREATE TABLE CoverageData (
    CoverageID INT PRIMARY KEY AUTO_INCREMENT,
    CountryCode CHAR(3) NOT NULL,
    Year YEAR NOT NULL,
    VaccineCode VARCHAR(20) NOT NULL,
    Coverage FLOAT,
    TargetNumber INT,
    DosesAdministered INT,
    CoverageCategory VARCHAR(50),
    FOREIGN KEY (CountryCode) REFERENCES Countries(CountryCode),
    FOREIGN KEY (VaccineCode) REFERENCES Vaccines(VaccineCode)
);

CREATE TABLE DiseaseIncidence (
    IncidenceID INT PRIMARY KEY AUTO_INCREMENT,
    CountryCode CHAR(3) NOT NULL,
    Year YEAR NOT NULL,
    DiseaseCode VARCHAR(20) NOT NULL,
    IncidenceRate FLOAT,
    Denominator VARCHAR(50),
    FOREIGN KEY (CountryCode) REFERENCES Countries(CountryCode),
    FOREIGN KEY (DiseaseCode) REFERENCES Diseases(DiseaseCode)
);

CREATE TABLE ReportedCases (
    CaseID INT PRIMARY KEY AUTO_INCREMENT,
    CountryCode CHAR(3) NOT NULL,
    Year YEAR NOT NULL,
    DiseaseCode VARCHAR(20) NOT NULL,
    Cases INT,
    FOREIGN KEY (CountryCode) REFERENCES Countries(CountryCode),
    FOREIGN KEY (DiseaseCode) REFERENCES Diseases(DiseaseCode)
);

CREATE TABLE VaccineIntroduction (
    IntroID INT PRIMARY KEY AUTO_INCREMENT,
    CountryCode CHAR(3) NOT NULL,
    Year YEAR NOT NULL,
    VaccineDescription VARCHAR(255),
    Introduced BOOLEAN,
    FOREIGN KEY (CountryCode) REFERENCES Countries(CountryCode)
);

CREATE TABLE VaccineSchedule (
    ScheduleID INT PRIMARY KEY AUTO_INCREMENT,
    CountryCode CHAR(3) NOT NULL,
    VaccineCode VARCHAR(20) NOT NULL,
    Year YEAR NOT NULL,
    ScheduleRound INT,
    TargetPopulation VARCHAR(100),
    GeoArea VARCHAR(100),
    AgeAdministered VARCHAR(50),
    SourceComment TEXT,
    FOREIGN KEY (CountryCode) REFERENCES Countries(CountryCode),
    FOREIGN KEY (VaccineCode) REFERENCES Vaccines(VaccineCode)
);
