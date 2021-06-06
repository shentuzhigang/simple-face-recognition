/*
 Navicat Premium Data Transfer

 Source Server         : RDS MySQL
 Source Server Type    : MySQL
 Source Server Version : 80016
 Source Host           : rm-bp17m6mdi0y0ne9g2co.mysql.rds.aliyuncs.com:3306
 Source Schema         : stzg

 Target Server Type    : MySQL
 Target Server Version : 80016
 File Encoding         : 65001

 Date: 06/06/2021 16:17:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for face
-- ----------------------------
DROP TABLE IF EXISTS `face`;
CREATE TABLE `face`  (
  `学号` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `encoding` varchar(4096) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`学号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
