-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-08-2024 a las 20:31:41
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `maquinaexpendedora`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `matricula` bigint(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(235) NOT NULL,
  `carrera` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`matricula`, `nombre`, `apellido`, `carrera`) VALUES
(3041000002, 'Ana', 'López', 'TSU en Diseño Digital Área Animación'),
(3041000003, 'Carlos', 'García', 'TSU en Energías Renovables Área Calidad '),
(3041000004, 'María', 'Rodríguez', 'TSU en Tecnologías de la Información'),
(3041000005, 'Luis', 'Martínez', 'TSU en Mantenimiento Área Industrial'),
(3041000006, 'Sofía', 'Hernández', 'TSU en Mecatrónica Área Sistemas de Manu'),
(3041000007, 'David', 'González', 'TSU en Desarrollo de Negocios Área Merca'),
(3041000008, 'Laura', 'Díaz', 'TSU en Diseño Digital Área Animación'),
(3041000009, 'Jorge', 'Ramírez', 'TSU en Energías Renovables Área Calidad '),
(3041000010, 'Elena', 'Torres', 'TSU en Tecnologías de la Información'),
(3041230367, 'Juan', 'Pérez', 'TSU en Desarrollo de Negocios Área Merca');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `codigo` varchar(5) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `precio` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `tipo_producto` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`codigo`, `nombre`, `precio`, `stock`, `tipo_producto`) VALUES
('A1', 'Coca Cola', 25, 8, 'Bebidas'),
('A3', 'Fanta', 20, 10, 'Bebidas'),
('B1', 'Sabritas', 25, 8, 'Snacks'),
('B2', 'Churrumais', 15, 7, 'Snacks'),
('C1', 'Gomitas', 25, 3, 'Golosinas'),
('C2', 'LolyPop', 5, 8, 'Golosinas'),
('C3', 'Chocoretas', 20, 9, 'Golosinas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id` int(11) NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp(),
  `hora` time NOT NULL DEFAULT current_timestamp(),
  `matricula` bigint(20) NOT NULL,
  `codigo` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id`, `fecha`, `hora`, `matricula`, `codigo`) VALUES
(1, '2024-08-10', '16:20:26', 3041230367, 'C3'),
(2, '2024-08-10', '16:24:14', 3041230367, 'C3'),
(3, '2024-08-10', '16:25:47', 3041230367, 'C1'),
(4, '2024-08-10', '16:27:54', 3041230367, 'B2'),
(5, '2024-08-10', '19:30:44', 3041000005, 'A3'),
(6, '2024-08-10', '19:37:09', 3041000003, 'B1'),
(7, '2024-08-10', '19:37:32', 3041000003, 'B2'),
(8, '2024-08-10', '19:39:57', 3041230367, 'A3'),
(9, '2024-08-10', '19:47:41', 3041000007, 'C3'),
(10, '2024-08-10', '19:52:43', 3041230367, 'C1'),
(17, '2024-08-16', '13:10:47', 3041000002, 'A1'),
(18, '2024-08-16', '14:53:44', 3041000002, 'B2'),
(19, '2024-08-16', '16:12:34', 3041230367, 'C1'),
(20, '2024-08-16', '16:52:11', 3041230367, 'C1'),
(21, '2024-08-16', '17:24:57', 3041230367, 'A1'),
(22, '2024-08-16', '17:25:56', 3041230367, 'C3'),
(23, '2024-08-16', '17:41:19', 3041230367, 'B2'),
(24, '2024-08-16', '17:42:18', 3041230367, 'B1'),
(25, '2024-08-16', '18:36:50', 3041230367, 'B1'),
(26, '2024-08-16', '18:37:55', 3041230367, 'A1');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`matricula`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `matricula` (`matricula`),
  ADD KEY `codigo` (`codigo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`matricula`) REFERENCES `estudiantes` (`matricula`),
  ADD CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`codigo`) REFERENCES `productos` (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
