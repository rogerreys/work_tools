# S3Download App

## Descripción

La aplicación `S3Download` es una herramienta que facilita la descarga de archivos desde un bucket de Amazon S3 a una carpeta local especificada. Esta herramienta utiliza un archivo de configuración en formato JSON para especificar los parámetros necesarios para la descarga.

## Requisitos

- Java JDK 8 o superior.
- Archivo de configuración en formato JSON.

## Estructura del Proyecto

- `S3Download.java`: Archivo principal que contiene la lógica de la aplicación.
- `Utils.java`: Archivo de utilidades que contiene métodos auxiliares.
- `config.json`: Archivo de configuración en formato JSON.

## Configuración

El archivo de configuración (`config.json`) debe contener las siguientes secciones:

```json
{
  "primary": {
    "destinationFolder": "./jars",
    "download": "false",
    "enviroment": "qa02"
  },
  "dev2": {
    "bucketName": "dev2-loans-t1-batch-executablefiledirectory-507781971948",
    "awsProfile": "507781971948_BI-XMEN-COBIS-DEV-D1-R2"
  },
  "qa02": {
    "bucketName": "qa02-loans-t1-batch-executablefiledirectory-462297762050",
    "awsProfile": "462297762050_BI-TRANSV-COBIS-STEP_FUNCT-QA-D1"
  }
}
```
# Descripción de los parámetros
### primary

- destinationFolder: Carpeta donde se guardarán los archivos descargados.
- download: Indicador de si se debe realizar la descarga (true o false).
- enviroment: Entorno de trabajo (ej. qa02, dev2).
#### dev2

- bucketName: Nombre del bucket S3 para el entorno dev2.
- awsProfile: Perfil de AWS para el entorno dev2.
#### qa02

- bucketName: Nombre del bucket S3 para el entorno qa02.
- awsProfile: Perfil de AWS para el entorno qa02.

# Ejecución
Para ejecutar la aplicación, se necesita un archivo .bat con la siguiente configuración:

```shell
java -jar App.jar ./config.json
```

# Ejemplo de Uso
1. Coloque el archivo de configuración config.json en el mismo directorio que App.jar.
2. Ejecute el siguiente comando desde la terminal o un archivo .bat:

```shell
java -jar App.jar ./config.json
```