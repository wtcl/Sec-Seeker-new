-- MySQL dump 10.13  Distrib 5.5.58, for Win64 (AMD64)
--
-- Host: localhost    Database: tracker
-- ------------------------------------------------------
-- Server version	5.5.58

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
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `password` varchar(500) NOT NULL,
  `uuid` varchar(100) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `phonenumber` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` VALUES (1,'10001','pbkdf2:sha256:260000$0GBqJpLnrtcTVa2k$1a03d23b5d254632437730509b38a36cf9f97b53b65e9839cca109a6f96993db','8db4e07cfec22979','nagtive','100000000001'),(2,'10002','pbkdf2:sha256:260000$I7EveFTAAiQNvhp5$84979cde5d041a48302e2f128cdf65242e71ed5a6e3fe8e704df1daddf3cd821','91edbc5c876c4715','nagtive','100000000002'),(3,'zjj','pbkdf2:sha256:260000$UEQ4mXKb64wxWLgq$060970574f40d668fe063ca6189613f9bf10c581d692c0bc38c9063a13f0c741','ba5966825c6c58d4','nagtive','100000000003'),(4,'zydzyd','pbkdf2:sha256:260000$4pTtbWahaBEYHbhb$c5208ac4a445d31f9c8c6daa8b6c994669f5b5735015f4876eb7cfd16af9aa39','a4dcf190ba8c8ba8','nagtive','100000000004'),(8,'kk','pbkdf2:sha256:260000$4GfWrWBMG6B18CT7$8f0ab2b50e8f9f0f53ce626642c96e07a5f82ccc79c7d3abd23c839f4710a58e','ae442d30f7130b7d','nagtive','252916925097'),(9,'xxx','pbkdf2:sha256:260000$mR0ht7a456vonVmR$eff284383dba4131a244231a34bf8419a5a6ee61a4e3f08db9f46f4b54a93d14','8ec29286b20602eb','nagtive','959281406528'),(10,'zyd0','pbkdf2:sha256:260000$VR0yaWvn46lqIEHl$726f3a4b344dbba257be30416fa6e60e0c7d0744ab3d37157e52373fd70df8f9','ea191e21270f2929','nagtive','317292488124'),(11,'zyd2','pbkdf2:sha256:260000$KCw1HrtxOkrMxgjq$ea2224fa39daf2c87fec2f6163a4da1c54f8af0e15640ccd330ddde4918c7987','feb9be529a76040c','nagtive','489604478357');
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'tracker'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-10 16:47:20
