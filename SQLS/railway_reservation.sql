-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 22, 2022 at 05:08 AM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `railway_reservation`
--

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `resno` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `age` varchar(10) NOT NULL,
  `no_ofac1stclass` int(5) NOT NULL,
  `no_ofac2ndclass` int(5) NOT NULL,
  `no_ofac3rdclass` int(5) NOT NULL,
  `no_ofsleeper` int(5) NOT NULL,
  `no_oftickets` int(5) NOT NULL,
  `totaf` int(5) NOT NULL,
  `status` varchar(50) NOT NULL DEFAULT 'CONFIRMED',
  `trainno` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`resno`, `name`, `age`, `no_ofac1stclass`, `no_ofac2ndclass`, `no_ofac3rdclass`, `no_ofsleeper`, `no_oftickets`, `totaf`, `status`, `trainno`) VALUES
(1126, 'Arpan Saha', '16', 0, 0, 0, 0, 3, 3, 'CONFIRMED', 11223),
(1856, 'Anubhab', '24', 0, 0, 0, 0, 5, 5, 'CONFIRMED', 12234);

-- --------------------------------------------------------

--
-- Table structure for table `train`
--

CREATE TABLE `train` (
  `trainno` int(5) NOT NULL,
  `no_ofac1stclass` int(5) NOT NULL,
  `no_ofac2ndclass` int(5) NOT NULL,
  `no_ofac3rdclass` int(5) NOT NULL,
  `no_ofsleeper` int(5) NOT NULL,
  `trainname` varchar(50) NOT NULL,
  `startingpt` varchar(50) NOT NULL,
  `destination` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `train`
--

INSERT INTO `train` (`trainno`, `no_ofac1stclass`, `no_ofac2ndclass`, `no_ofac3rdclass`, `no_ofsleeper`, `trainname`, `startingpt`, `destination`) VALUES
(11223, 23, 34, 45, 20, 'SHATAPDI', 'Sealdah', 'Maynaguri'),
(12234, 40, 40, 40, 50, 'Rajdhani Express', 'Hawrah', 'Delhi'),
(12345, 30, 4, 9, 6, 'GITANJALI', 'Hawrah', 'Mumbai');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`resno`),
  ADD KEY `train_no_constraint` (`trainno`);

--
-- Indexes for table `train`
--
ALTER TABLE `train`
  ADD PRIMARY KEY (`trainno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `train`
--
ALTER TABLE `train`
  MODIFY `trainno` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121213;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `train_no_constraint` FOREIGN KEY (`trainno`) REFERENCES `train` (`trainno`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
