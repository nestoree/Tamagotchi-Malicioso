# 🐣 Tamagotchi Malicioso (Proyecto Educativo de Ciberseguridad)

## ⚠️ ADVERTENCIA:
Este proyecto contiene código con comportamiento malicioso simulado (ransomware y reverse shell).
Está creado **únicamente con fines educativos y de laboratorio** para entender cómo funcionan este tipo de amenazas.

**NO** ejecutes este código en tu sistema real. Usa únicamente máquinas virtuales aisladas.

## 📚 Descripción

Este repositorio contiene una simulación de:

- 🎮 Un Tamagotchi en consola (tamagochi.py)
- 🐴 Un "troyano" (troyano.py)
- 🔐 Un "ransomware" (ransomware.py)

El flujo del programa simula un juego donde el usuario debe mantener vivo un Tamagotchi durante 7 días.
Si el usuario:

- Cierra el programa
- Deja morir al Tamagotchi
- No interactúa lo suficiente
Entonces se ejecuta el módulo de ransomware.
Si el usuario completa los 7 días, se ejecuta el módulo tipo troyano.

## 🧠 Funcionamiento del Código

**tamagochi.py**

Simula un Tamagotchi básico en consola:

Variables principales:

- Hambre
- Energía
- Tiempo restante (7 días)

Acciones disponibles:

- Comer
- Jugar
- Dormir
- Salir

Cada segundo:

- Reduce estadísticas
- Verifica si el Tamagotchi sigue vivo
- Controla el tiempo restante

Si muere o el usuario cierra el programa:

```
exec(open('ransomware.py').read())
```

Si sobrevive 7 días:
```
exec(open('troyano.py').read())
```

**ransomware.py**

Simulación básica de ransomware usando la librería:

**cryptography.fernet**

Funciones principales:

- generar_llave() → Genera una clave simétrica
- cifrar_archivos() → Recorre el directorio objetivo y cifra archivos
- soltar_nota() → Genera una nota de rescate

⚠️ Actualmente el directorio objetivo está definido como:

```
DIRECTORIO_OBJETIVO = "C:/"
```

Esto sería extremadamente destructivo en un sistema real.

## 3️⃣ troyano.py

Simula comportamiento de troyano:

- Intenta detener Windows Defender:

```
sc stop WinDefend
```

- Descarga Netcat
- Intenta abrir una reverse shell hacia una IP específica

## 🎯 Objetivo Educativo

Este proyecto sirve para:

Entender cómo funcionan:

- Ransomware
- Reverse shells
- Persistencia básica

Analizar código malicioso en un entorno controlado

Practicar:

- Análisis estático
- Análisis dinámico
- Detección de comportamiento sospechoso
- Mejora de defensas

## 🧪 Recomendaciones de Uso Seguro

✅ Usar solo en:

- Máquina virtual (por ejemplo: VirtualBox)
- Entorno aislado sin red
- Sistema de laboratorio

❌ No ejecutar en:

- Tu sistema principal
- Equipos con información importante
- Entornos de producción

## 📦 Requisitos

Python 3.9+
Librerías:

```
cryptography
tkinter
```

Instalación:

```
pip install cryptography
```

## ⚖️ Disclaimer Legal

Este proyecto es únicamente para fines educativos y de investigación en ciberseguridad.
El autor no se hace responsable del uso indebido del código.
El uso de técnicas de:

- Ransomware
- Reverse shells
- Desactivación de antivirus

sin autorización **explícita** es ilegal en la mayoría de países.

## 🛡️ Ética en Ciberseguridad

La ciberseguridad tiene como propósito:
- Proteger sistemas
- Detectar amenazas
- Fortalecer defensas
- Este código debe utilizarse para aprender cómo proteger, no cómo atacar.
