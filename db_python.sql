-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 15-11-2023 a las 23:27:23
-- Versión del servidor: 5.7.36
-- Versión de PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_python`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `consejos`
--

DROP TABLE IF EXISTS `consejos`;
CREATE TABLE IF NOT EXISTS `consejos` (
  `Problema` varchar(255) NOT NULL,
  `Consejo` text NOT NULL,
  `Actividad` text NOT NULL,
  `Libro` varchar(255) NOT NULL,
  PRIMARY KEY (`Problema`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `consejos`
--

INSERT INTO `consejos` (`Problema`, `Consejo`, `Actividad`, `Libro`) VALUES
('Ansiedad', 'La terapia cognitiva conductual (TCC) es la manera más eficaz de la psicoterapia para tratar los trastornos de ansiedad', 'Hacer ejercicio. El ejercicio regular, aunque sean 15 minutos diarios, puede aliviar el estrés liberando endorfinas, además de otros efectos como mejorar la calidad del sueño o mejorar la autoestima. ', 'El cerebro de la gente feliz'),
('Depresión', 'Con la psicoterapia, se ofrece seguridad, confianza, comprensión y apoyo emocional; se intentan corregir los pensamientos distorsionados; se explica el carácter temporal y se desdramatiza la situación; se consigue la participación del paciente en el proceso curativo y, por último, se enseña a prever las posibles recaídas.', 'Hacer ejercicio durante 30 minutos o más al día de tres a cinco días a la semana puede mejorar significativamente los síntomas de depresión.', 'Terapia cognitiva de la depresión (Aaron T. Beck)');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

DROP TABLE IF EXISTS `persona`;
CREATE TABLE IF NOT EXISTS `persona` (
  `User` varchar(255) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `Edad` int(2) NOT NULL,
  PRIMARY KEY (`User`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`User`, `Nombre`, `Edad`) VALUES
('guada', 'Guadalupe Kiara', 16);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `progreso`
--

DROP TABLE IF EXISTS `progreso`;
CREATE TABLE IF NOT EXISTS `progreso` (
  `User` varchar(255) NOT NULL,
  `Problema` varchar(255) NOT NULL,
  `Objetivo` text NOT NULL,
  PRIMARY KEY (`User`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `progreso`
--

INSERT INTO `progreso` (`User`, `Problema`, `Objetivo`) VALUES
('Guada', 'Ansiedad', 'Tratar el problema con las mejores herramientas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `User` varchar(255) NOT NULL,
  `Pass` varchar(255) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`Id`, `User`, `Pass`) VALUES
(1, 'guada', 'guada'),
(2, 'admin', 'admin');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
