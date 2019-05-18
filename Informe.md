# Informe Lógica Difusa

##### Nombre: Joel David Hernández Cruz

##### Grupo: C-411

##### Correo: j.cruz@estudiantes.matcom.uh.cu

### 1. Propuesta de Problema a Solucionar

David quiere cambiar su laptop por una mejor, ya que la actual no esta funcionando bien. Pero David no quiere cualquier laptop, según su criterio, lo mas importa a la hora de comprar una nueva laptop es:

- Micro:
  Se puede caracterizar como:
  
  - Regular
  - Bueno
  - Muy Bueno
  
- Tarjeta de Video:

  Se puede caracterizar como:

  - Regular
  - Buena
  - Muy Buena

- Precio:

  Se puede caracterizar como:

  - Medio
  - Caro
  - Muy Caro

Nuestro sistema dado una configuración de estas tres variables, dirá un ***rating*** si David:

- Se compra la laptop
- No se la compra
- Si quizás se la compre

### 2. Principales ideas seguidas al implementar el Sistema

Para dar solución a este problema, primeramente implementamos funciones de pertenencia para cada una de las categorías posibles de las variables (**Micro**, **Tarjeta de Video**, **Precio**  y **Rating**), estas son de tipo triangular y trapezoidal. Definimos varias reglas de inferencia para obtener distintos valores y con estos hacer una aproximación del resultado final. Escogimos como métodos de agregación **Mamdani** y **Larsen**. Y para desdifuziﬁcar se implementaron (Centroide, Bisección, Métodos de Máximos).



### 3. Características del sistema de inferencia propuesto

- Reglas de Inferencia:

  - Si **micro regular** $\and$ **tarjeta de video regular** $\and$ **precio medio**$\implies$ **Maybe**
  - Si **micro regular** $\and$ **tarjeta de video regular** $\and$ **precio muy caro** $\implies$ **No**
  - Si **micro regular** $\and$ **tarjeta de video buena** $\and$ **precio medio** $\implies$ **Yes**
  - Si **micro regular** $\and$ **tarjeta de video muy buena** $\and$ **precio caro** $\implies$ **Yes**
  - Si **micro regular** $\and$ **tarjeta de video muy buena** $\and$ **precio muy caro** $\implies$ **Maybe**
  - Si **micro bueno** $\and$ **tarjeta de video regular** $\and$ **precio medio** $\implies$ **Maybe**
  - Si **micro bueno** $\and$ **tarjeta de video regular** $\and$ **precio caro** $\implies$ **No**
  - Si **micro bueno** $\and$ **tarjeta de video buena** $\and$ **precio medio** $\implies$ **Yes**
  - Si **micro bueno** $\and$ **tarjeta de video buena** $\and$ **precio muy caro** $\implies$ **No**
  - Si **micro bueno** $\and$ **tarjeta de video muy buena** $\and$ **precio medio** $\implies$ **Yes**
  - Si **micro muy bueno** $\and$ **tarjeta de video regular** $\and$ **precio medio** $\implies$ **Maybe**
  - Si **micro muy bueno** $\and$ **tarjeta de video buena** $\and$ **precio medio** $\implies$ **Yes**
  - Si **micro muy bueno** $\and$ **tarjeta de video muy buena** $\and$ **precio medio** $\implies$ **Yes**

  
  
### 4. Estructura del proyecto:
  El proyecto esta dividido en varios archivos:

- ***aggregation.py*** se encuentran implementados los métodos de Larsen y Mamdani. 
- **database.py*** se encuentran las funciones de pertenencia para las categorías de las variables.
- **defuzzification.py** métodos de defuzzificacion(Centroide, Bisección, Máximos).
- **membership.py** funciones de membrecía implementadas(triangular y trapezoidal).