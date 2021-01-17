# Análisis sentimental de tweets sobre las elecciones de EEUU en 2020 por territorios

El objetivo de este proyecto, encuadrado dentro de la asignatura Cloud y Big Data de la Universidad Complutense de Madrid, es obtener un análisis sentimental sobre un dataset de tweets generados entre el 15 de octubre de 2020 y el 8 de noviembre de 2020, los cuales incluyen los hashtags #donaldtrump y #joebiden. De esta forma, utilizando un analizador de lenguaje natural, podemos conocer cuál de los dos candidatos es el preferido en cada territorio.

## Requisitos
* Python >=3.5
* Pandas `pip install pandas`
* TextBlob `pip install textblob && python -m textblob.download_corpora`
* Pandarallel `pip install pandarallel`

## Contenido del repositorio

Dentro del repositorio existen dos ficheros .csv: *trump.csv*, que incluye todos los tweets con el hashtag #donaldtrump, y *biden.csv*, que incluye todos los tweets con el hashtag #joebiden. Ambos suman aproximadamente dos millones de tweets.

Por otro lado, se incluyen tres scripts para el análisis por territorios:

* analisisPorContinentes.py: Analiza los tweets por continente del candidato especificado e imprime por pantalla cuál es su polaridad. Si se incluye la opción de ambos, también imprime cuál de los dos es el preferido en cada continente. Uso:


      python analisisPorContinentes.py <trump|biden|both> <n_workers> <progressBar>  

* analisisPorPaises.py: Analiza los tweets del país especificado, imprime por pantalla la polaridad de ambos candidatos y cuál de los dos es el preferido. Uso:


      python analisisPorPaises.py <country> <n_workers> <progressBar>
  
* analisisPorEstados.py: Analiza los tweets de cada estado de EEUU, imprime por pantalla la polaridad de ambos candidatos y si el candidato con mayor positividad se corresponde con el ganador de las elecciones en ese estado. Finalmente imprime cuántas coincidencias ha habido y el porcentaje de acierto. Uso:

      python analisisPorEstados.py <n_workers> <progressBar>
  

## Más información

Toda la información referente a este proyecto se puede consultar en la web del proyecto: https://wantonfrito.github.io/bigdata2020-2021ELECTIONS/

Este proyecto ha sido desarrollado por:
* Gonzalo Martínez Berzal
* Álvaro Penalva Alberca
* Mario Román Dono
* Javier Ignacio Sotelino Barriga
