/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.5.40 : Database - test
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`test` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `test`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `admin` */

insert  into `admin`(`id`,`name`,`password`) values (1,'root','123456');

/*Table structure for table `field` */

DROP TABLE IF EXISTS `field`;

CREATE TABLE `field` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `field` */

insert  into `field`(`id`,`name`) values (1,'data scientist'),(2,'software development'),(3,'security'),(4,'user experience'),(5,'hardware'),(8,'software dev'),(9,'robotics'),(10,'hci');

/*Table structure for table `mentor` */

DROP TABLE IF EXISTS `mentor`;

CREATE TABLE `mentor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `race` varchar(255) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `field` varchar(255) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `mentor` */

insert  into `mentor`(`id`,`name`,`email`,`position`,`gender`,`race`,`number`,`field`,`password`) values (1,'m1','m1@qq.com','professor','man','asian',2,'security','123456'),(2,'m2','m2@qq.com','professor','man','black',2,'robotics','123456'),(3,'m3','m3@qq.com','professor','woman','black',2,'data scientist','123456'),(4,'m4','m4@qq.com','professor','woman','white',2,'hci','123456'),(5,'m5','m5@qq.com','professor','man','white',2,'software dev','123456'),(6,'m6','test6@qq.com','associate professor','man','black',1,'user experience','123456');

/*Table structure for table `relationship` */

DROP TABLE IF EXISTS `relationship`;

CREATE TABLE `relationship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mentor_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `relationship` */

insert  into `relationship`(`id`,`mentor_id`,`student_id`) values (1,2,7),(2,3,8),(3,6,9),(4,5,10),(5,4,11),(6,1,12);

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `panther_id` int(11) DEFAULT NULL,
  `race` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `p_gender` varchar(255) DEFAULT NULL,
  `p_race` varchar(255) DEFAULT NULL,
  `p_position` varchar(255) DEFAULT NULL,
  `field` varchar(255) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

/*Data for the table `student` */

insert  into `student`(`id`,`name`,`email`,`panther_id`,`race`,`gender`,`p_gender`,`p_race`,`p_position`,`field`,`password`) values (7,'zz1','111@qq.com',111,'black','man','man','black','professor','security','123456'),(8,'zz2','1112@qq.com',1112,'black','man','woman','asian','professor','security','123456'),(9,'zz2','1113@qq.com',1113,'black','man','man','black','professor','software dev','123456'),(10,'zz4','1114@qq.com',1114,'black','man','man','white','professor','robotics','123456'),(11,'zz5','1115@qq.com',1115,'black','man','woman','white','professor','robotics','123456'),(12,'test6','test6@qq.com',1116,'black','woman','man','asian','lecturer','software development','123456');

/*Table structure for table `system_info` */

DROP TABLE IF EXISTS `system_info`;

CREATE TABLE `system_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `system_info` */

insert  into `system_info`(`id`,`name`,`status`) values (1,'register_info',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
