-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: plasma_bank
-- ------------------------------------------------------
-- Server version	5.7.31-0ubuntu0.18.04.1

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
-- Table structure for table `DONOR`
--

DROP TABLE IF EXISTS `DONOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `DONOR` (
  `Donor_id` varchar(12) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Aadhar_num` bigint(20) NOT NULL,
  `Blood_type` varchar(5) NOT NULL,
  `Number_of_donations` int(11) NOT NULL,
  `Age` int(11) NOT NULL,
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
  `Age` int(11) NOT NULL,
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
  `Sample_no` int(11) NOT NULL,
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
-- Table structure for table `USER`
--

DROP TABLE IF EXISTS `USER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `USER` (
  `Login_id` varchar(50) NOT NULL,
  `Password` varchar(25) NOT NULL,
  `Contact` bigint(20) NOT NULL,
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-02 14:24:54
