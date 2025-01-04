## Estudiante: `Santiago Gamboa Martínez`

### Ejercicio 1:

<details><summary>Descripción</summary>

Create a package with all code of class `Shape`, this exersice should be conducted in two ways:

- A unique module inside of package Shape

- Individual modules that import Shape in inheritates from it.

</details>

---

### **A unique module inside of package `Shape`: reto_5.1**

(Un único módulo dentro del paquete `Shape`)

El proyecto está organizado en un paquete `Shape` que contiene un único módulo llamado `shape.py`. Este módulo centraliza todas las definiciones de las clases relacionadas con la geometría, incluyendo aquellas que representan puntos, líneas y formas geométricas. La estructura del proyecto es la siguiente:

```bash
reto_5.1/
├── Shape/
│   ├── __init__.py
│   └── shape.py
└── main.py
```

### **Descripción**

1. **Paquete `Shape`**:

   - Representa la lógica central del proyecto.
   - Contiene un único módulo `shape.py`, lo cual simplifica la estructura al consolidar toda la funcionalidad en un solo archivo.

2. **Módulo `shape.py`**:

   - Incluye las definiciones de las clases base y derivadas:
     - **`Point`**: Representa un punto en el plano bidimensional.
     - **`Line`**: Modela una línea compuesta por dos puntos (`Point`).
     - **`Shape`**: Define una forma geométrica utilizando composición (instancias de `Point` y `Line`).
     - **Clases derivadas de `Shape`**:
       - **`Rectangle`** y **`Triangle`**: Heredan de `Shape` y representan formas específicas.
       - **`Square`**: Especialización de `Rectangle`.
       - **Clases derivadas de `Triangle`**:
         - **`Isosceles`**, **`Equilateral`**, **`Scalene`**, **`Trirectangle`**: Subclases que modelan diferentes tipos de triángulos.
   - Utiliza composición y herencia para estructurar jerárquicamente los conceptos geométricos.

3. **Archivo principal `main.py`**:
   - Este archivo actúa como el punto de entrada para pruebas y ejecución.
   - Importa el paquete `Shape` y utiliza las clases definidas en `shape.py` para instanciar y manipular objetos geométricos.
   - Permite probar la interacción entre clases, como crear formas geométricas complejas, calcular propiedades y realizar operaciones.

### **Individual modules that import `Shape` inherit from it: reto_5.2**

(Los módulos individuales importan `Shape` y heredan de él)

En este enfoque, se busca que diferentes módulos independientes dentro del proyecto puedan importar la clase `Shape` (o las clases relacionadas dentro del paquete `Shape`) y extender su funcionalidad a través de la herencia. Aquí está la estructura del proyecto y su explicación:

```bash
reto_5.2/
├── Shape/
│   ├── __init__.py
│   ├── equilateral.py
│   ├── isosceles.py
│   ├── line.py
│   ├── point.py
│   ├── ractangle.py
│   ├── scalene.py
│   ├── shape.py
│   ├── square.py
│   ├── triangle.py
│   └── trirectangle.py
└── main.py
```

---

### **Descripción**

1. **Paquete `Shape`**:

   - Contiene la clase base `Shape`, definida en el módulo `shape.py`.
   - La clase `Shape` actúa como un modelo abstracto que otras clases heredan y especializan.

2. **Módulo `shape.py`**:

   - Contiene únicamente la definición de la clase `Shape` y, opcionalmente, clases o métodos utilitarios relacionados con las formas geométricas generales.
   - **`Shape`**: Define atributos y métodos básicos que las clases derivadas pueden sobrescribir o extender.

3. **Módulos individuales (`rectangle.py`, `triangle.py`, etc.)**:

   - Cada módulo importa la clase `Shape` desde el paquete `Shape` y define una clase derivada específica:
     - **`rectangle.py`**: Define la clase `Rectangle`, que extiende `Shape` para representar rectángulos.
     - **`triangle.py`**: Define la clase `Triangle`, que extiende `Shape` para representar triángulos.
     - **Otros módulos** (como `equilateral.py`, `isosceles.py`, `scalene.py`, etc.) se encargan de formas geométricas más específicas, como triángulos con características particulares (equiláteros, isósceles, escaleno).
   - La lógica de cada forma específica se encapsula en su módulo respectivo, lo que facilita su mantenimiento y extensión.

4. **Archivo principal `main.py`**:
   - Importa las clases derivadas desde sus respectivos módulos (`Rectangle`, `Triangle`, etc.).
   - Se utiliza para crear instancias de las formas, realizar pruebas y ejecutar operaciones geométricas.
