-- SQLite
create table renter (
        Number int,
        First_Name varchar(255),
        Middidle_Intial varchar(255),
        Last_Name varchar(255),
        Address varchar(255),
        City varchar(255),
        State varchar(255),
        Postal_code int,
        Telephone_Number int,
        Email_Address varchar(255)
);

create table property (
        Condo_Location_Number varchar(255),
        Condo_Location_Name varchar(255),
        Address varchar(255),
        City varchar(255),
        State varchar(255),
        Postal_code int,
        Condo_Unit_Number varchar(255),
        Square_Footage varchar(255),
        Number_of_Bedrooms int,
        Number_of_Bathrooms int,
        Maximum_number_of_Persons int,
        Base_Weekly_Rate varchar(255)
);
create table rental_agreement (
        Renter_Number int,
        First_Name varchar(255),
        Middle_Initial varchar(255),
        Last_Name  varchar(255),
        Address varchar(255),
        Weekly_Rental_Amount int
);




