# Python-Gestos

Detecta una mano con la cámara web, calcula qué dedos están levantados y envía ese arreglo por UDP a otra aplicación.

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)
![Licencia](https://img.shields.io/badge/licencia-MIT-green?style=flat)
![Último commit](https://img.shields.io/github/last-commit/ViceAguilera/Python-Gestos?style=flat)

## Descripción

Script pequeño de visión por computador. Usa el módulo de seguimiento de manos de `cvzone` (basado en MediaPipe) para obtener el estado de los cinco dedos y transmitirlo a `127.0.0.1:5052`, de modo que otro programa (por ejemplo un juego o un visualizador) pueda reaccionar a los gestos.

## Características

- Captura de video a 1280x720 con vista espejo.
- Detección de una sola mano (confianza mínima 0.8).
- Envío del arreglo de dedos (por ejemplo `[0, 1, 1, 0, 0]`) por socket UDP.
- Se cierra con la tecla `q`.

## Tecnologías

- Python 3
- OpenCV
- cvzone y MediaPipe

## Requisitos

- Python 3 y una cámara web.

## Instalación

```bash
pip install opencv-contrib-python cvzone mediapipe
```

## Uso

```bash
python main.py
```

Los datos se envían a `127.0.0.1:5052`; un receptor UDP debe estar escuchando en ese puerto para consumirlos.

## Estructura del proyecto

```
main.py   # Captura, detección de mano y envío UDP
```

## Licencia

Distribuido bajo la licencia MIT. Ver [LICENSE](LICENSE).

## Autor

**Vicente Aguilera Arias** — [Portafolio](https://portfolio.iamsirius.cl) · [GitHub](https://github.com/ViceAguilera) · [LinkedIn](https://www.linkedin.com/in/vicenteaguilera/)
