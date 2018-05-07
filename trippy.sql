BEGIN;
--
-- Create model Accomodation
--
CREATE TABLE "trippy_accomodation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "AccomodationName" varchar(30) NOT NULL, "AccomodationType" varchar(5) NOT NULL, "Rate" decimal NOT NULL, "Discount" decimal NOT NULL);
--
-- Create model Airport
--
CREATE TABLE "trippy_airport" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "AirportCode" varchar(3) NOT NULL, "AirportName" varchar(100) NOT NULL);
--
-- Create model CarRentalTime
--
CREATE TABLE "trippy_carrentaltime" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "StartRentalTime" date NOT NULL, "EndRentalTime" date NOT NULL);
--
-- Create model Group
--
CREATE TABLE "trippy_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "size" integer NOT NULL);
--
-- Create model Location
--
CREATE TABLE "trippy_location" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "City" varchar(30) NOT NULL, "State" varchar(30) NOT NULL, "Country" varchar(30) NOT NULL);
--
-- Create model Passenger
--
CREATE TABLE "trippy_passenger" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "FirstName" varchar(30) NOT NULL, "LastName" varchar(30) NOT NULL, "Email" varchar(254) NOT NULL, "Gender" varchar(1) NOT NULL, "GroupId_id" integer NOT NULL REFERENCES "trippy_group" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Payment
--
CREATE TABLE "trippy_payment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "CardNumber" varchar(16) NOT NULL, "PaymentAmount" integer NOT NULL, "CardExpiryDate" varchar(5) NOT NULL, "GroupId_id" integer NOT NULL REFERENCES "trippy_group" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Transportation
--
CREATE TABLE "trippy_transportation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Transport_Type" varchar(10) NULL);
--
-- Create model CarRental
--
CREATE TABLE "trippy_carrental" ("TransportId_id" integer NOT NULL PRIMARY KEY REFERENCES "trippy_transportation" ("id") DEFERRABLE INITIALLY DEFERRED, "Rate" integer NOT NULL, "CarType" varchar(30) NOT NULL, "Location_id" integer NOT NULL REFERENCES "trippy_location" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Flight
--
CREATE TABLE "trippy_flight" ("FlightNumber" varchar(10) NOT NULL, "FlightCarrier" varchar(30) NOT NULL, "FlightPrice" integer NOT NULL, "DepartureTime" datetime NOT NULL, "ArrivalTime" datetime NOT NULL, "TransportId_id" integer NOT NULL PRIMARY KEY REFERENCES "trippy_transportation" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field Driver to carrentaltime
--
ALTER TABLE "trippy_carrentaltime" RENAME TO "trippy_carrentaltime__old";
CREATE TABLE "trippy_carrentaltime" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "StartRentalTime" date NOT NULL, "EndRentalTime" date NOT NULL, "Driver_id" integer NOT NULL REFERENCES "trippy_passenger" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "trippy_carrentaltime" ("id", "StartRentalTime", "EndRentalTime", "Driver_id") SELECT "id", "StartRentalTime", "EndRentalTime", NULL FROM "trippy_carrentaltime__old";
DROP TABLE "trippy_carrentaltime__old";
CREATE INDEX "trippy_passenger_GroupId_id_84e8b53a" ON "trippy_passenger" ("GroupId_id");
CREATE INDEX "trippy_payment_GroupId_id_a7dcbc66" ON "trippy_payment" ("GroupId_id");
CREATE INDEX "trippy_carrental_Location_id_569d1177" ON "trippy_carrental" ("Location_id");
CREATE INDEX "trippy_carrentaltime_Driver_id_2b6368ed" ON "trippy_carrentaltime" ("Driver_id");
--
-- Add field LocationId to airport
--
ALTER TABLE "trippy_airport" RENAME TO "trippy_airport__old";
CREATE TABLE "trippy_airport" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "AirportCode" varchar(3) NOT NULL, "AirportName" varchar(100) NOT NULL, "LocationId_id" integer NOT NULL REFERENCES "trippy_location" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "trippy_airport" ("id", "AirportCode", "AirportName", "LocationId_id") SELECT "id", "AirportCode", "AirportName", NULL FROM "trippy_airport__old";
DROP TABLE "trippy_airport__old";
CREATE INDEX "trippy_airport_LocationId_id_7b84d018" ON "trippy_airport" ("LocationId_id");
--
-- Add field LocationId to accomodation
--
ALTER TABLE "trippy_accomodation" RENAME TO "trippy_accomodation__old";
CREATE TABLE "trippy_accomodation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "AccomodationName" varchar(30) NOT NULL, "AccomodationType" varchar(5) NOT NULL, "Rate" decimal NOT NULL, "Discount" decimal NOT NULL, "LocationId_id" integer NOT NULL REFERENCES "trippy_location" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "trippy_accomodation" ("id", "AccomodationName", "AccomodationType", "Rate", "Discount", "LocationId_id") SELECT "id", "AccomodationName", "AccomodationType", "Rate", "Discount", NULL FROM "trippy_accomodation__old";
DROP TABLE "trippy_accomodation__old";
CREATE INDEX "trippy_accomodation_LocationId_id_e96f56ad" ON "trippy_accomodation" ("LocationId_id");
--
-- Add field ArrivalAirport to flight
--
ALTER TABLE "trippy_flight" RENAME TO "trippy_flight__old";
CREATE TABLE "trippy_flight" ("FlightNumber" varchar(10) NOT NULL, "FlightCarrier" varchar(30) NOT NULL, "FlightPrice" integer NOT NULL, "DepartureTime" datetime NOT NULL, "ArrivalTime" datetime NOT NULL, "TransportId_id" integer NOT NULL PRIMARY KEY REFERENCES "trippy_transportation" ("id") DEFERRABLE INITIALLY DEFERRED, "ArrivalAirport_id" integer NOT NULL REFERENCES "trippy_airport" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "trippy_flight" ("FlightNumber", "FlightCarrier", "FlightPrice", "DepartureTime", "ArrivalTime", "TransportId_id", "ArrivalAirport_id") SELECT "FlightNumber", "FlightCarrier", "FlightPrice", "DepartureTime", "ArrivalTime", "TransportId_id", 0 FROM "trippy_flight__old";
DROP TABLE "trippy_flight__old";
CREATE INDEX "trippy_flight_ArrivalAirport_id_4a2e0f39" ON "trippy_flight" ("ArrivalAirport_id");
--
-- Add field DepartureAirport to flight
--
ALTER TABLE "trippy_flight" RENAME TO "trippy_flight__old";
CREATE TABLE "trippy_flight" ("FlightNumber" varchar(10) NOT NULL, "FlightCarrier" varchar(30) NOT NULL, "FlightPrice" integer NOT NULL, "DepartureTime" datetime NOT NULL, "ArrivalTime" datetime NOT NULL, "TransportId_id" integer NOT NULL PRIMARY KEY REFERENCES "trippy_transportation" ("id") DEFERRABLE INITIALLY DEFERRED, "ArrivalAirport_id" integer NOT NULL REFERENCES "trippy_airport" ("id") DEFERRABLE INITIALLY DEFERRED, "DepartureAirport_id" integer NOT NULL REFERENCES "trippy_airport" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "trippy_flight" ("FlightNumber", "FlightCarrier", "FlightPrice", "DepartureTime", "ArrivalTime", "TransportId_id", "ArrivalAirport_id", "DepartureAirport_id") SELECT "FlightNumber", "FlightCarrier", "FlightPrice", "DepartureTime", "ArrivalTime", "TransportId_id", "ArrivalAirport_id", 0 FROM "trippy_flight__old";
DROP TABLE "trippy_flight__old";
CREATE INDEX "trippy_flight_ArrivalAirport_id_4a2e0f39" ON "trippy_flight" ("ArrivalAirport_id");
CREATE INDEX "trippy_flight_DepartureAirport_id_9374a677" ON "trippy_flight" ("DepartureAirport_id");
--
-- Add field Car to carrentaltime
--
ALTER TABLE "trippy_carrentaltime" RENAME TO "trippy_carrentaltime__old";
CREATE TABLE "trippy_carrentaltime" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "StartRentalTime" date NOT NULL, "EndRentalTime" date NOT NULL, "Driver_id" integer NOT NULL REFERENCES "trippy_passenger" ("id") DEFERRABLE INITIALLY DEFERRED, "Car_id" integer NOT NULL REFERENCES "trippy_carrental" ("TransportId_id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "trippy_carrentaltime" ("id", "StartRentalTime", "EndRentalTime", "Driver_id", "Car_id") SELECT "id", "StartRentalTime", "EndRentalTime", "Driver_id", NULL FROM "trippy_carrentaltime__old";
DROP TABLE "trippy_carrentaltime__old";
CREATE INDEX "trippy_carrentaltime_Driver_id_2b6368ed" ON "trippy_carrentaltime" ("Driver_id");
CREATE INDEX "trippy_carrentaltime_Car_id_57cdd521" ON "trippy_carrentaltime" ("Car_id");
COMMIT;
