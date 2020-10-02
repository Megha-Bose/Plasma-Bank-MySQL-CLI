-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: plasma_bank
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
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
/*!40000 ALTER TABLE `DEPARTMENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEPENDENT`
--

DROP TABLE IF EXISTS `DEPENDENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DEPENDENT` (
  `Staff_id` varchar(12) NOT NULL,
  `First_name` varchar(50) NOT NULL,
  `Last_name` varchar(50) NOT NULL,
  `Age` int DEFAULT NULL,
  `Gender` varchar(20) NOT NULL,
  `Relationship` varchar(30) NOT NULL,
  PRIMARY KEY (`Staff_id`,`First_name`,`Last_name`),
  CONSTRAINT `DEPENDENT_ibfk_1` FOREIGN KEY (`Staff_id`) REFERENCES `STAFF` (`Staff_id`)
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
/*!40101 SET character_set_client = utf8 */;
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
  CONSTRAINT `DONOR_ibfk_1` FOREIGN KEY (`Login_id`) REFERENCES `USER` (`Login_id`)
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HOSPITAL` (
  `Hospital_id` varchar(12) NOT NULL,
  `Hospital_name` varchar(300) NOT NULL,
  `Distance` decimal(6,2) NOT NULL,
  `Login_id` varchar(50) NOT NULL,
  PRIMARY KEY (`Hospital_id`),
  KEY `Login_id` (`Login_id`),
  CONSTRAINT `HOSPITAL_ibfk_1` FOREIGN KEY (`Login_id`) REFERENCES `USER` (`Login_id`)
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
-- Table structure for table `PATIENT`
--

DROP TABLE IF EXISTS `PATIENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  CONSTRAINT `PATIENT_ibfk_1` FOREIGN KEY (`Hospital_id`) REFERENCES `HOSPITAL` (`Hospital_id`)
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PATIENT_ALLERGIES` (
  `Patient_id` varchar(12) NOT NULL,
  `Allergies` varchar(500) NOT NULL,
  PRIMARY KEY (`Patient_id`,`Allergies`),
  CONSTRAINT `PATIENT_ALLERGIES_ibfk_1` FOREIGN KEY (`Patient_id`) REFERENCES `PATIENT` (`Patient_id`)
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PLASMA` (
  `Donor_id` varchar(12) NOT NULL,
  `Donation_date` date NOT NULL,
  `Sample_no` int NOT NULL,
  `Used` tinyint(1) NOT NULL,
  `Inventory_id` varchar(12) NOT NULL,
  PRIMARY KEY (`Donor_id`,`Donation_date`,`Sample_no`),
  CONSTRAINT `PLASMA_ibfk_1` FOREIGN KEY (`Donor_id`) REFERENCES `DONOR` (`Donor_id`)
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
-- Table structure for table `STAFF`
--

DROP TABLE IF EXISTS `STAFF`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
  CONSTRAINT `STAFF_ibfk_1` FOREIGN KEY (`Login_id`) REFERENCES `USER` (`Login_id`),
  CONSTRAINT `STAFF_ibfk_2` FOREIGN KEY (`Supervisor`) REFERENCES `STAFF` (`Staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STAFF`
--

LOCK TABLES `STAFF` WRITE;
/*!40000 ALTER TABLE `STAFF` DISABLE KEYS */;
/*!40000 ALTER TABLE `STAFF` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STAFF_SKILLS`
--

DROP TABLE IF EXISTS `STAFF_SKILLS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `STAFF_SKILLS` (
  `Staff_id` varchar(12) NOT NULL,
  `Skills` varchar(500) NOT NULL,
  PRIMARY KEY (`Staff_id`,`Skills`),
  CONSTRAINT `STAFF_SKILLS_ibfk_1` FOREIGN KEY (`Staff_id`) REFERENCES `STAFF` (`Staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STAFF_SKILLS`
--

LOCK TABLES `STAFF_SKILLS` WRITE;
/*!40000 ALTER TABLE `STAFF_SKILLS` DISABLE KEYS */;
/*!40000 ALTER TABLE `STAFF_SKILLS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USER`
--

DROP TABLE IF EXISTS `USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40000 ALTER TABLE `USER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VEHICLE_DETAILS`
--

DROP TABLE IF EXISTS `VEHICLE_DETAILS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WORKS_FOR` (
  `Department_id` varchar(12) NOT NULL,
  `Staff_id` varchar(12) NOT NULL,
  PRIMARY KEY (`Staff_id`,`Department_id`),
  KEY `Department_id` (`Department_id`),
  CONSTRAINT `WORKS_FOR_ibfk_1` FOREIGN KEY (`Department_id`) REFERENCES `DEPARTMENT` (`Department_id`)
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

-- Dump completed on 2020-10-02 16:33:03
