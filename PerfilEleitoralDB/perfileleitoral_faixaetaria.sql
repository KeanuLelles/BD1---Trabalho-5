CREATE DATABASE  IF NOT EXISTS `perfileleitoral` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `perfileleitoral`;
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: perfileleitoral
-- ------------------------------------------------------
-- Server version	8.0.38

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `faixaetaria`
--

DROP TABLE IF EXISTS `faixaetaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faixaetaria` (
  `CodFaixaEtaria` int NOT NULL,
  `DescricaoFaixaEtaria` varchar(25) NOT NULL,
  PRIMARY KEY (`CodFaixaEtaria`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faixaetaria`
--

LOCK TABLES `faixaetaria` WRITE;
/*!40000 ALTER TABLE `faixaetaria` DISABLE KEYS */;
INSERT INTO `faixaetaria` VALUES (-3,'Inválido'),(1600,'16 anos'),(1700,'17 anos'),(1800,'18 anos'),(1900,'19 anos'),(2000,'20 anos'),(2124,'21 a 24 anos'),(2529,'25 a 29 anos'),(3034,'30 a 34 anos'),(3539,'35 a 39 anos'),(4044,'40 a 44 anos'),(4549,'45 a 49 anos'),(5054,'50 a 54 anos'),(5559,'55 a 59 anos'),(6064,'60 a 64 anos'),(6569,'65 a 69 anos'),(7074,'70 a 74 anos'),(7579,'75 a 79 anos'),(8084,'80 a 84 anos'),(8589,'85 a 89 anos'),(9094,'90 a 94 anos'),(9599,'95 a 99 anos'),(9999,'100 anos ou mais');
/*!40000 ALTER TABLE `faixaetaria` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-24 17:31:04
