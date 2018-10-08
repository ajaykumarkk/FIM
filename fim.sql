-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 06, 2018 at 09:45 AM
-- Server version: 5.7.21
-- PHP Version: 5.6.35

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fim`
--

-- --------------------------------------------------------

--
-- Table structure for table `hashes`
--

DROP TABLE IF EXISTS `hashes`;
CREATE TABLE IF NOT EXISTS `hashes` (
  `serial` int(11) NOT NULL AUTO_INCREMENT,
  `sysid` int(11) NOT NULL,
  `path` varchar(500) NOT NULL,
  `filename` varchar(256) NOT NULL,
  `hash` varchar(500) NOT NULL,
  `Time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`serial`)
) ENGINE=MyISAM AUTO_INCREMENT=18666 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `hashes`
--

INSERT INTO `hashes` (`serial`, `sysid`, `path`, `filename`, `hash`, `Time`) VALUES
(18658, 11, 'F:/outer//temp.txt', 'null', '0791e7a3f864bb5707012bd466837e4e#3f348daf7362bfd2ee8475a2b768c888', '2018-08-14 08:10:12'),
(18659, 11, 'F:/outer//temp.txt', 'null', '3f348daf7362bfd2ee8475a2b768c888#81ebef9cae9e113e5016058ac93217a7', '2018-08-14 09:26:07'),
(18660, 11, 'C:/test//test - Copy (2).odg', 'null', 'a0736cf22384f9dfa745d4788423b8c2', '2018-08-14 09:30:04'),
(18661, 11, 'C:/test//test - Copy (3).odg', 'null', 'a0736cf22384f9dfa745d4788423b8c2', '2018-08-14 09:30:04'),
(18662, 11, 'C:/test//test - Copy.odg', 'null', 'a0736cf22384f9dfa745d4788423b8c2', '2018-08-14 09:30:04'),
(18663, 11, 'C:/test//test.odg', 'null', 'a0736cf22384f9dfa745d4788423b8c2', '2018-08-14 09:30:04'),
(18664, 11, 'C:/test//etrs.txt', 'null', '779d0196b3fcb908b293a30f7c75c437', '2018-08-14 09:31:01'),
(18665, 11, 'C:/test//etrs.txt', 'null', '779d0196b3fcb908b293a30f7c75c437', '2018-08-14 09:42:03');

-- --------------------------------------------------------

--
-- Table structure for table `paths`
--

DROP TABLE IF EXISTS `paths`;
CREATE TABLE IF NOT EXISTS `paths` (
  `serial` int(11) NOT NULL AUTO_INCREMENT,
  `sysid` int(11) NOT NULL,
  `path` varchar(2000) NOT NULL,
  PRIMARY KEY (`serial`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `systems`
--

DROP TABLE IF EXISTS `systems`;
CREATE TABLE IF NOT EXISTS `systems` (
  `serial` int(11) NOT NULL AUTO_INCREMENT,
  `mac_id` varchar(30) NOT NULL,
  `system_name` varchar(30) NOT NULL,
  PRIMARY KEY (`serial`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `systems`
--

INSERT INTO `systems` (`serial`, `mac_id`, `system_name`) VALUES
(9, '28:c6:3f:1a:16:1f', 'NULL'),
(8, 'f8:94:c2:0f:c2:60', 'NULL'),
(11, 'f8:94:c2:0f:c2:64', 'NULL');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
