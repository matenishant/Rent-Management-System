/*
SQLyog Enterprise - MySQL GUI v7.02 
MySQL - 5.0.67-community-nt : Database - build_flats
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`build_flats` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `build_flats`;

/*Table structure for table `flat_details` */

DROP TABLE IF EXISTS `flat_details`;

CREATE TABLE `flat_details` (
  `flat_no` varchar(200) NOT NULL,
  `owner_name` varchar(200) default NULL,
  `address` varchar(200) default NULL,
  `area` varchar(200) default NULL,
  `security` varchar(200) default NULL,
  `due_amount` varchar(200) default NULL,
  `maintainance` varchar(200) default NULL,
  `remark` varchar(200) default NULL,
  `contact` varchar(20) default NULL,
  `month` varchar(8) default NULL,
  `last_year_balance` varchar(20) default NULL,
  `last_year_date` varchar(20) default NULL,
  `total_due` varchar(20) default NULL,
  PRIMARY KEY  (`flat_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `flat_details` */

insert  into `flat_details`(`flat_no`,`owner_name`,`address`,`area`,`security`,`due_amount`,`maintainance`,`remark`,`contact`,`month`,`last_year_balance`,`last_year_date`,`total_due`) values ('1002','','','','','','2000','','88888wwwww',NULL,'0','','24000'),('102','kdsodof','okokokok','2033','3040','10020','2000','ok','8239562757',NULL,NULL,NULL,NULL),('2000','10000','2000','2000','2000','2000','000','ok','200000000000',NULL,'1002','2999',NULL),('2020','20303','33333333333','2000','2000','2000','2000','1000','200011111',NULL,'10000','10/2/2019',NULL),('222222','','','','','','22222','okkkk','8888888888',NULL,'1000','18/08/2000','267664'),('a102','Nishant MAthur','1200','123, Marathalli Bangalore','40000','10000','1200','Amount due hai','9024347004',NULL,NULL,NULL,NULL),('a707','Avi sharma','kuch bhi hai sala','500','4000','8000','4000','88899','8239562757','11',NULL,NULL,NULL),('b10022','hello kd','102','ejejjee','2003','3003','4004','400','4004333333333',NULL,NULL,NULL,NULL),('b102','shubham sharma','500','jaipur,amity univerisyt','0','50000','500','Security due','8239562757',NULL,NULL,NULL,NULL),('b108','parth khandelwal','100','iffjjfjf','2000','3000','4000','hi','8239562757',NULL,NULL,NULL,NULL),('b202','Amit','Parth','Nishant','Jaipur','2022','Student','Remark','1111111111111111','12','2000','12/23/18','21000'),('s-405','Parth','agjsdjshdhjskbcmbm\nsachjscjkshjchksjc\nckjsckzscscn,zc','500','40000','10000','500','kch due hai','9024347004',NULL,NULL,NULL,NULL);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `uname` varchar(200) default NULL,
  `pass` varchar(200) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`uname`,`pass`) values ('ok','ok');

/*Table structure for table `monthly_pay` */

DROP TABLE IF EXISTS `monthly_pay`;

CREATE TABLE `monthly_pay` (
  `flat_no` varchar(200) default NULL,
  `maintainance` varchar(200) default NULL,
  `payment_mode` varchar(200) default NULL,
  `manual_date` varchar(200) default NULL,
  `payment_date` varchar(200) default NULL,
  `month` varchar(200) default NULL,
  `remark` varchar(200) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `monthly_pay` */

insert  into `monthly_pay`(`flat_no`,`maintainance`,`payment_mode`,`manual_date`,`payment_date`,`month`,`remark`) values ('b202','11111','111111','111111','2018-11-25','111111','1111111'),('b202','10000','cash','10/20/2018','2018-11-25','june','bhg'),('b202','100000','cheque','10/02/2018','2018-11-25','july','thik h'),('b202','1000','','','2018-12-29','',''),('b202','200','','','2018-12-29','',''),('b202','200','','','2018-12-29','',''),('b202','200','','','2018-12-29','',''),('b202','2000','','','2018-12-29','','');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
