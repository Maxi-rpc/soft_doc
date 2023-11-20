-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 20-11-2023 a las 19:39:31
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
  `Descripcion` text NOT NULL,
  `Consejo` text NOT NULL,
  `Libro` varchar(255) NOT NULL,
  PRIMARY KEY (`Problema`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `consejos`
--

INSERT INTO `consejos` (`Problema`, `Descripcion`, `Consejo`, `Libro`) VALUES
('Trastorno de conducta Alimentaria TCA', 'Son trastornos mentales que pueden llegar a ser muy graves. En ellos, las preocupaciones\r\nfundamentales del paciente son la comida y la percepción de la silueta corporal.', 'Buscar ayuda de un profesional estos pueden ayudar a sobrellevar el trastorno, Hablar sobre\r\nello puede ser un gran paso y ayuda a saber que no estas solo, Cuida tu salud física como\r\nmantener una rutina de ejercicios y asegurarte de estar obteniendo los nutrientes necesarios\r\npara el cuerpo, practica la autocompasión, no te castigues por tener un trastorno alimentario.', '“El cuerpo sabe” - Bev Mattocks'),
('Depresión', 'La depresión es un trastorno del estado de ánimo que afecta a cómo te sientes, piensas y\r\nmanejas las actividades diarias, puede afectar a personas de todas las edades, razas y\r\ncondiciones sociales, y puede ser desencadenada por una combinación de varios factores.\r\nExisten dos tipos de depresión:\r\nDepresión mayor, que implica síntomas de depresión la mayoría del tiempo durante por lo\r\nmenos dos semanas. Estos síntomas interfieren con la capacidad para trabajar, dormir,\r\nestudiar y comer.\r\nTrastorno depresivo persistente (distimia), que a menudo incluye síntomas de depresión\r\nmenos graves que duran mucho más tiempo, generalmente por lo menos durante 2 años.', 'Hablar y desahogarse con algún amigo o familiar (lo recomendable es un profesional /\r\npsicólogo), no tomar decisiones precipitadas, ser sincero con uno mismo, tratar de pensar en\r\npositivo aunque no sea fácil, no encerrarse en uno mismo, moverse y hacer actividades\r\nsimples (ir al cine, a caminar etc), comer y dormir bien, evitar el estrés, no abusar de alcohol\r\nu otras drogas, cumplir un tratamiento médico.', '\"Feeling Good: The New Mood Therapy\" de David D. Burns'),
('Trastorno Bipolar', 'El trastorno bipolar no se trata sólo de tener cambios de humor. Es una condición de salud\r\nmental grave que solía denominarse depresión maníaca. Hay dos tipos principales de\r\ntrastorno bipolar que pueden diferir en cuanto a la gravedad y la naturaleza de sus síntomas.\r\nLas personas con trastorno bipolar experimentan cambios dramáticos en su estado de ánimo\r\nque pueden incluir períodos de depresión y manía. La naturaleza y gravedad de estos\r\nsíntomas dependen del tipo de trastorno bipolar que tengan.', 'Dejar de beber alcohol o usar drogas recreativas, establecer relaciones saludables,\r\nestablecer una rutina saludable, consultar con un profesional antes de hacer uso de\r\nun medicamento, tener un registro del estado de ánimo sería bueno.', 'La enfermedad de las emociones. El trastorno bipolar (2004)\r\n-Eduard Vieta, Francesc Colom, Anabel Martines Aran.'),
('Trastorno de ansiedad generalizada TAG', 'Se caracteriza por la preocupación y la ansiedad exagerada y excesiva sobre cualquier evento\r\ndel día a día sin ningún motivo aparente que justifique esta preocupación. De hecho, es uno\r\nde los trastornos de ansiedad con unos síntomas más molestos e incapacitantes, ya que\r\naparecen en muchas situaciones diferentes. Las personas que sufren este trastorno siempre\r\nesperan que las cosas salgan mal y no pueden dejar de preocuparse por su salud, el dinero, la\r\nfamilia, el trabajo, etc.', 'Terapia cognitivo-conductual: Este tipo de terapia puede ser muy efectiva para tratar la\r\nansiedad. Técnicas de relajación; La meditación, la respiración profunda y el yoga pueden\r\nayudarte a relajarte y reducir tus niveles de ansiedad. Mantén una dieta saludable: Algunos\r\nalimentos pueden aumentar tus niveles de ansiedad. Haz ejercicio regularmente: El ejercicio\r\npuede ayudarte a reducir tus niveles de ansiedad y mejorar tu estado de ánimo. Duerme lo\r\nsuficiente: La falta de sueño puede aumentar tus niveles de ansiedad.', '\"El poder del ahora\" de Eckhart Tolle.'),
('Duelo', 'En los momentos de duelo, es fácil caer en una dinámica de comportamientos dañinos para\r\ncon uno mismo y abandono de las tareas de autocuidado en general. Hay que identificar las 5\r\nfases del duelo:\r\n- Negación: Consiste en no creer que se haya producido la pérdida o en no ser capaz\r\nde percibir dicha pérdida como algo real que nos ha pasado a nosotros.\r\n- ira: Uno de los primeros sentimientos que afloran en las personas es la ira por el\r\ndolor, así como la frustración y la impotencia de haber perdido a esa persona querida.\r\n- Negociación: La persona empieza a darse cuenta de la realidad de lo sucedido e\r\ninicia un proceso de reflexión interna en el que sopesa las posibles opciones que hay\r\npara solucionar el problema.\r\n- depresión: La persona experimenta principalmente sentimientos de pena, desolación,\r\naislamiento social, dolor, nostalgia y pérdida de interés por todo lo que rodea su vida\r\nen general.\r\n- aceptación: Esta fase es la culminación del proceso de duelo, cuando se llega a la\r\nmisma se puede dar por concluido. Se asocia a un estado de bienestar y a un\r\nsentimiento de liberación de todo el dolor y el sufrimiento experimentado durante el\r\nproceso.', 'Es recomendable que en este periodo se eviten situaciones estresantes o generadoras de\r\nansiedad. Permitámonos realizar un acto simbólico de despedida de nuestro ser querido que\r\nresulta de gran apoyo a nivel psicológico. Buscar el apoyo en otras personas en los\r\nmomentos más difíciles es la mejor forma de superar el duelo. Rellenar un diario personal\r\npara comprender mejor lo que sentimos. Seguir un horario de sueño estable durante las\r\nsemanas o meses posteriores a la pérdida.', '\"El camino de las lágrimas\" de Jorge Bucay'),
('Autosabotaje', 'Es un acto inconsciente que aparece en los momentos que puedan suponer un gran cambio\r\nen la vida de las personas, sea del tipo que sea. Estas conductas tienden a obstaculizar la\r\nconsecuencia de metas o logros mediante auto-manipulaciones inconscientes', 'Autoconocimiento, intenta identificar los patrones de autosabotaje en tu vida. Cambia tus\r\ncreencias limitantes, muchas veces el autosabotaje está impulsado por creencias negativas\r\nsobre uno mismo. Establece metas realistas, a veces nos saboteamos porque establecemos\r\nmetas demasiado altas o poco realistas. Practica el autocuidado, cuida de ti mismo física,\r\nemocional y mentalmente. Busca apoyo, habla con amigos, familiares o un profesional de la\r\nsalud mental.', '\"El arte de no amargarse la vida\" de Rafael Santandreu');

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
('guada', 'Guadalupe Kiara', 16),
('maxi', 'maximiliano', 30),
('santi', 'Santiago', 16);

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
('Guada', 'Trastorno de conducta Alimentaria TCA', 'Tratar el problema con las mejores herramientas'),
('maxi', 'Duelo', 'debe mejorar autoestima'),
('santi', 'Trastorno de ansiedad generalizada TAG', 'Tratar de disminuir esta ansiedad');

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
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`Id`, `User`, `Pass`) VALUES
(1, 'guada', 'guada'),
(2, 'admin', 'admin'),
(6, 'santi', 'santi'),
(10, 'maxi', 'maxi');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
