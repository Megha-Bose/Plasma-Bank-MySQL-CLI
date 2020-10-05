-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: localhost    Database: plasma_bank
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `DEPARTMENT`
--

DROP TABLE IF EXISTS `DEPARTMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DEPARTMENT` (
  `Department_id` varchar(12) NOT NULL,
  `Manager` varchar(12) NOT NULL,
  `Description` varchar(100) DEFAULT NULL,
  `No_of_employees` int NOT NULL,
  `Remarks` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEPARTMENT`
--

LOCK TABLES `DEPARTMENT` WRITE;
/*!40000 ALTER TABLE `DEPARTMENT` DISABLE KEYS */;
INSERT INTO `DEPARTMENT` VALUES ('DL','1234','list of vehicles in logistivs dept',2,NULL),('DPI','1','count of samples in each inventory in plasma inventories dept',3,NULL);
/*!40000 ALTER TABLE `DEPARTMENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEPENDENT`
--

DROP TABLE IF EXISTS `DEPENDENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DEPENDENT` (
  `Staff_id` varchar(12) NOT NULL,
  `First_name` varchar(50) NOT NULL,
  `Last_name` varchar(50) NOT NULL,
  `Age` int DEFAULT NULL,
  `Gender` varchar(20) NOT NULL,
  `Relationship` varchar(30) NOT NULL,
  PRIMARY KEY (`Staff_id`,`First_name`,`Last_name`),
  CONSTRAINT `DEPENDENT_ibfk_1` FOREIGN KEY (`Staff_id`) REFERENCES `STAFF` (`Staff_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEPENDENT`
--

LOCK TABLES `DEPENDENT` WRITE;
/*!40000 ALTER TABLE `DEPENDENT` DISABLE KEYS */;
/*!40000 ALTER TABLE `DEPENDENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DONOR`
--

DROP TABLE IF EXISTS `DONOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DONOR` (
  `Donor_id` varchar(12) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Aadhar_num` bigint NOT NULL,
  `Blood_type` varchar(5) NOT NULL,
  `Number_of_donations` int NOT NULL,
  `Age` int NOT NULL,
  `Birth_date` date NOT NULL,
  `Login_id` varchar(50) NOT NULL,
  PRIMARY KEY (`Donor_id`),
  KEY `Login_id` (`Login_id`),
  CONSTRAINT `DONOR_ibfk_1` FOREIGN KEY (`Login_id`) REFERENCES `USER` (`Login_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `DONOR_chk_1` CHECK ((`Age` >= 18))
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DONOR`
--

LOCK TABLES `DONOR` WRITE;
/*!40000 ALTER TABLE `DONOR` DISABLE KEYS */;
/*!40000 ALTER TABLE `DONOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HOSPITAL`
--

DROP TABLE IF EXISTS `HOSPITAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `HOSPITAL` (
  `Hospital_id` varchar(12) NOT NULL,
  `Hospital_name` varchar(300) NOT NULL,
  `Distance` decimal(6,2) NOT NULL,
  `Login_id` varchar(50) NOT NULL,
  PRIMARY KEY (`Hospital_id`),
  KEY `Login_id` (`Login_id`),
  CONSTRAINT `HOSPITAL_ibfk_1` FOREIGN KEY (`Login_id`) REFERENCES `USER` (`Login_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HOSPITAL`
--

LOCK TABLES `HOSPITAL` WRITE;
/*!40000 ALTER TABLE `HOSPITAL` DISABLE KEYS */;
/*!40000 ALTER TABLE `HOSPITAL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LOGISTICS`
--

DROP TABLE IF EXISTS `LOGISTICS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `LOGISTICS` (
  `Vehicle_id` varchar(10) NOT NULL,
  `Vehicle_type` varchar(50) NOT NULL,
  `Availability` tinyint(1) NOT NULL,
  `Deliveries` int NOT NULL,
  `Department_id` varchar(12) NOT NULL,
  PRIMARY KEY (`Vehicle_id`),
  KEY `Department_id` (`Department_id`),
  KEY `Vehicle_type` (`Vehicle_type`),
  CONSTRAINT `LOGISTICS_ibfk_1` FOREIGN KEY (`Department_id`) REFERENCES `DEPARTMENT` (`Department_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `LOGISTICS_ibfk_2` FOREIGN KEY (`Vehicle_type`) REFERENCES `VEHICLE_DETAILS` (`Vehicle_type`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LOGISTICS`
--

LOCK TABLES `LOGISTICS` WRITE;
/*!40000 ALTER TABLE `LOGISTICS` DISABLE KEYS */;
/*!40000 ALTER TABLE `LOGISTICS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ORDER_REQUEST`
--

DROP TABLE IF EXISTS `ORDER_REQUEST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ORDER_REQUEST` (
  `Order_id` varchar(12) NOT NULL,
  `Blood_type` varchar(5) NOT NULL,
  `Order_date` date NOT NULL,
  `Distance` decimal(6,2) NOT NULL,
  `Accepted` tinyint(1) NOT NULL,
  `Vehicle_id` varchar(10) DEFAULT NULL,
  `Donor_id` varchar(12) DEFAULT NULL,
  `Hospital_id` varchar(12) NOT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `Vehicle_id` (`Vehicle_id`),
  KEY `Hospital_id` (`Hospital_id`),
  KEY `Donor_id` (`Donor_id`),
  CONSTRAINT `ORDER_REQUEST_ibfk_1` FOREIGN KEY (`Vehicle_id`) REFERENCES `LOGISTICS` (`Vehicle_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ORDER_REQUEST_ibfk_2` FOREIGN KEY (`Hospital_id`) REFERENCES `HOSPITAL` (`Hospital_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ORDER_REQUEST_ibfk_3` FOREIGN KEY (`Donor_id`) REFERENCES `PLASMA` (`Donor_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ORDER_REQUEST`
--

LOCK TABLES `ORDER_REQUEST` WRITE;
/*!40000 ALTER TABLE `ORDER_REQUEST` DISABLE KEYS */;
/*!40000 ALTER TABLE `ORDER_REQUEST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PATIENT`
--

DROP TABLE IF EXISTS `PATIENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PATIENT` (
  `Patient_id` varchar(12) NOT NULL,
  `First_name` varchar(50) NOT NULL,
  `Last_name` varchar(50) NOT NULL,
  `Age` int NOT NULL,
  `Birth_date` date NOT NULL,
  `Blood_type` varchar(5) NOT NULL,
  `Hospital_id` varchar(12) NOT NULL,
  PRIMARY KEY (`Patient_id`),
  KEY `Hospital_id` (`Hospital_id`),
  CONSTRAINT `PATIENT_ibfk_1` FOREIGN KEY (`Hospital_id`) REFERENCES `HOSPITAL` (`Hospital_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PATIENT`
--

LOCK TABLES `PATIENT` WRITE;
/*!40000 ALTER TABLE `PATIENT` DISABLE KEYS */;
/*!40000 ALTER TABLE `PATIENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PATIENT_ALLERGIES`
--

DROP TABLE IF EXISTS `PATIENT_ALLERGIES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PATIENT_ALLERGIES` (
  `Patient_id` varchar(12) NOT NULL,
  `Allergies` varchar(500) NOT NULL,
  PRIMARY KEY (`Patient_id`,`Allergies`),
  CONSTRAINT `PATIENT_ALLERGIES_ibfk_1` FOREIGN KEY (`Patient_id`) REFERENCES `PATIENT` (`Patient_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PATIENT_ALLERGIES`
--

LOCK TABLES `PATIENT_ALLERGIES` WRITE;
/*!40000 ALTER TABLE `PATIENT_ALLERGIES` DISABLE KEYS */;
/*!40000 ALTER TABLE `PATIENT_ALLERGIES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PLASMA`
--

DROP TABLE IF EXISTS `PLASMA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PLASMA` (
  `Donor_id` varchar(12) NOT NULL,
  `Donation_date` date NOT NULL,
  `Sample_no` int NOT NULL,
  `Used` tinyint(1) NOT NULL,
  `Inventory_id` varchar(12) NOT NULL,
  PRIMARY KEY (`Donor_id`,`Donation_date`,`Sample_no`),
  CONSTRAINT `PLASMA_ibfk_1` FOREIGN KEY (`Donor_id`) REFERENCES `DONOR` (`Donor_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PLASMA`
--

LOCK TABLES `PLASMA` WRITE;
/*!40000 ALTER TABLE `PLASMA` DISABLE KEYS */;
/*!40000 ALTER TABLE `PLASMA` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PLASMA_INVENTORY`
--

DROP TABLE IF EXISTS `PLASMA_INVENTORY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PLASMA_INVENTORY` (
  `Inventory_id` varchar(12) NOT NULL,
  `No_of_Aplus` int NOT NULL,
  `No_of_Aminus` int NOT NULL,
  `No_of_Bplus` int NOT NULL,
  `No_of_Bminus` int NOT NULL,
  `No_of_Oplus` int NOT NULL,
  `No_of_Ominus` int NOT NULL,
  `No_of_ABplus` int NOT NULL,
  `No_of_ABminus` int NOT NULL,
  `Capacity` int NOT NULL,
  `Vacancy` int NOT NULL,
  `Department_id` varchar(12) NOT NULL,
  PRIMARY KEY (`Inventory_id`),
  KEY `Department_id` (`Department_id`),
  CONSTRAINT `PLASMA_INVENTORY_ibfk_1` FOREIGN KEY (`Department_id`) REFERENCES `DEPARTMENT` (`Department_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PLASMA_INVENTORY`
--

LOCK TABLES `PLASMA_INVENTORY` WRITE;
/*!40000 ALTER TABLE `PLASMA_INVENTORY` DISABLE KEYS */;
/*!40000 ALTER TABLE `PLASMA_INVENTORY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STAFF`
--

DROP TABLE IF EXISTS `STAFF`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `STAFF` (
  `Staff_id` varchar(12) NOT NULL,
  `First_name` varchar(50) NOT NULL,
  `Last_name` varchar(50) NOT NULL,
  `Date_of_joining` date NOT NULL,
  `Salary` int NOT NULL,
  `Birth_date` date NOT NULL,
  `Age` int NOT NULL,
  `Supervisor` varchar(12) DEFAULT NULL,
  `Login_id` varchar(50) NOT NULL,
  PRIMARY KEY (`Staff_id`),
  KEY `Login_id` (`Login_id`),
  KEY `Supervisor` (`Supervisor`),
  CONSTRAINT `STAFF_ibfk_1` FOREIGN KEY (`Login_id`) REFERENCES `USER` (`Login_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `STAFF_ibfk_2` FOREIGN KEY (`Supervisor`) REFERENCES `STAFF` (`Staff_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STAFF`
--

LOCK TABLES `STAFF` WRITE;
/*!40000 ALTER TABLE `STAFF` DISABLE KEYS */;
INSERT INTO `STAFF` VALUES ('1234','ahana','name','2020-10-05',4396873,'1980-01-01',28,NULL,'STAFF1234');
/*!40000 ALTER TABLE `STAFF` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STAFF_SKILLS`
--

DROP TABLE IF EXISTS `STAFF_SKILLS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `STAFF_SKILLS` (
  `Staff_id` varchar(12) NOT NULL,
  `Skills` varchar(500) NOT NULL,
  PRIMARY KEY (`Staff_id`,`Skills`),
  CONSTRAINT `STAFF_SKILLS_ibfk_1` FOREIGN KEY (`Staff_id`) REFERENCES `STAFF` (`Staff_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STAFF_SKILLS`
--

LOCK TABLES `STAFF_SKILLS` WRITE;
/*!40000 ALTER TABLE `STAFF_SKILLS` DISABLE KEYS */;
INSERT INTO `STAFF_SKILLS` VALUES ('1234','C++'),('1234','Java'),('1234','Python');
/*!40000 ALTER TABLE `STAFF_SKILLS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SUPPLY`
--

DROP TABLE IF EXISTS `SUPPLY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SUPPLY` (
  `Order_id` varchar(12) NOT NULL,
  `Donor_id` varchar(12) DEFAULT NULL,
  `Vehicle_id` varchar(10) DEFAULT NULL,
  `Inventory_id` varchar(12) NOT NULL,
  PRIMARY KEY (`Order_id`),
  KEY `Donor_id` (`Donor_id`),
  KEY `Vehicle_id` (`Vehicle_id`),
  KEY `Inventory_id` (`Inventory_id`),
  CONSTRAINT `SUPPLY_ibfk_1` FOREIGN KEY (`Donor_id`) REFERENCES `PLASMA` (`Donor_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SUPPLY_ibfk_2` FOREIGN KEY (`Vehicle_id`) REFERENCES `LOGISTICS` (`Vehicle_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `SUPPLY_ibfk_3` FOREIGN KEY (`Inventory_id`) REFERENCES `PLASMA_INVENTORY` (`Inventory_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SUPPLY`
--

LOCK TABLES `SUPPLY` WRITE;
/*!40000 ALTER TABLE `SUPPLY` DISABLE KEYS */;
/*!40000 ALTER TABLE `SUPPLY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER`
--

DROP TABLE IF EXISTS `USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USER` (
  `Login_id` varchar(50) NOT NULL,
  `Password` varchar(25) NOT NULL,
  `Contact` bigint NOT NULL,
  `Address` varchar(100) NOT NULL,
  PRIMARY KEY (`Login_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USER`
--

LOCK TABLES `USER` WRITE;
/*!40000 ALTER TABLE `USER` DISABLE KEYS */;
INSERT INTO `USER` VALUES ('123','abc',123456789,'hi,hello, bye'),('ADMIN','admin',123456789,'a_address'),('DONOR1','d1',123456789,'d_address1'),('HOSPITAL1','h1',123456789,'h_address1'),('STAFF1','s1',123456789,'s_address1'),('STAFF1234','1234',1234,'testaddress'),('STAFF2','s2',123456789,'s_address2');
/*!40000 ALTER TABLE `USER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VEHICLE_DETAILS`
--

DROP TABLE IF EXISTS `VEHICLE_DETAILS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `VEHICLE_DETAILS` (
  `Vehicle_type` varchar(50) NOT NULL,
  `Max_dist` int NOT NULL,
  `Speed` int NOT NULL,
  PRIMARY KEY (`Vehicle_type`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VEHICLE_DETAILS`
--

LOCK TABLES `VEHICLE_DETAILS` WRITE;
/*!40000 ALTER TABLE `VEHICLE_DETAILS` DISABLE KEYS */;
/*!40000 ALTER TABLE `VEHICLE_DETAILS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WORKS_FOR`
--

DROP TABLE IF EXISTS `WORKS_FOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WORKS_FOR` (
  `Department_id` varchar(12) NOT NULL,
  `Staff_id` varchar(12) NOT NULL,
  PRIMARY KEY (`Staff_id`,`Department_id`),
  KEY `Department_id` (`Department_id`),
  CONSTRAINT `WORKS_FOR_ibfk_1` FOREIGN KEY (`Department_id`) REFERENCES `DEPARTMENT` (`Department_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WORKS_FOR`
--

LOCK TABLES `WORKS_FOR` WRITE;
/*!40000 ALTER TABLE `WORKS_FOR` DISABLE KEYS */;
/*!40000 ALTER TABLE `WORKS_FOR` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-05 14:50:34
