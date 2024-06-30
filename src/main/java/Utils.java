import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Request;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Response;
import software.amazon.awssdk.services.s3.model.S3Object;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Paths;
import java.text.SimpleDateFormat;
import java.util.*;

public class Utils {
    protected static String PRIMARY = "primary";
    protected static String ENVIROMENT = "enviroment";
    protected static String BUCKETNAME = "bucketName";
    protected static String DESTINATIONFOLDER = "destinationFolder";
    protected static String AWSPROFILE = "awsProfile";
    protected static String DOWNLOAD = "download";

    public static Map<String, String> getJsonValues(String pathToConfig) {
        // Crear una instancia de ObjectMapper
        ObjectMapper objectMapper = new ObjectMapper();
        // Crear un mapa para almacenar las configuraciones
        Map<String, String> configMap = new HashMap<>();

        try {
            // Leer el archivo JSON y convertirlo en una instancia de Config
            JsonNode rootNode = objectMapper.readTree(new File(pathToConfig));

            // Obtener la configuración primaria
            JsonNode primaryNode = rootNode.path(PRIMARY);
            String environmentKey = primaryNode.path(ENVIROMENT).asText();

            // Almacenar las variables de la sección primaria en el mapa
            Iterator<Map.Entry<String, JsonNode>> fields = primaryNode.fields();
            while (fields.hasNext()) {
                Map.Entry<String, JsonNode> field = fields.next();
                configMap.put(field.getKey(), field.getValue().asText());
            }

            // Obtener la configuración dinámica basada en el valor de environment
            JsonNode environmentConfig = rootNode.path(environmentKey);

            // Almacenar las variables de la sección dinámica en el mapa
            fields = environmentConfig.fields();
            while (fields.hasNext()) {
                Map.Entry<String, JsonNode> field = fields.next();
                configMap.put(field.getKey(), field.getValue().asText());
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            return configMap;
        }
    }

    public static void S3DownloadPorcess(String bucketName, String destinationFolder, String awsProfile, Boolean donwload) {
        List<List> files_bucket = new ArrayList<>();

        Region region = Region.US_EAST_1;
        S3Client s3 = S3Client.builder()
                .region(region)
                .credentialsProvider(ProfileCredentialsProvider.create(awsProfile))
                .build();

        // Listar objetos en el bucket
        ListObjectsV2Request listObjectsV2Request = ListObjectsV2Request.builder()
                .bucket(bucketName)
                .build();

        ListObjectsV2Response listObjResponse;
        do {
            listObjResponse = s3.listObjectsV2(listObjectsV2Request);

            for (S3Object content : listObjResponse.contents()) {
                String key = content.key();

                files_bucket.add(save_content(content));
                if (donwload) {
                    downloasFiles(bucketName, key, destinationFolder, s3);
                }
            }
            showInfoFiles(files_bucket);

        } while (listObjResponse.isTruncated());

    }

    private static List save_content(S3Object content) {
        List<String> content_info = new ArrayList<>();
        String key = content.key();

        String type = key.substring(key.lastIndexOf('.') + 1);
        Date lastModifiedDate = Date.from(content.lastModified());

        // Time format GMT-05
        SimpleDateFormat sdfgmt = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        sdfgmt.setTimeZone(TimeZone.getTimeZone("GMT-05:00"));
        String lastModified = sdfgmt.format(lastModifiedDate);

        content_info.add(key);
        content_info.add(type);
        content_info.add(lastModified);

        return content_info;
    }

    private static void showInfoFiles(List<List> files) {
        Integer len = 0;
        for (List file : files) {
            if (file.get(0).toString().length() > len) {
                len = file.get(0).toString().length();
            }
        }

        String format = "%-" + (len + 10) + "s%-15s%-15s\n";
        System.out.printf(format, "Nombre", "Tipo", "Ult. modificacion");
        for (List file : files) {
            System.out.printf(format, file.get(0), file.get(1), file.get(2));
        }
    }

    private static void downloasFiles(String bucketName, String key, String destinationFolder, S3Client s3) {
        System.out.printf("\nDescargando archivo: %-5s\n", key);
        // Descargar el objeto
        GetObjectRequest getObjectRequest = GetObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();

        InputStream s3ObjectResponse = s3.getObject(getObjectRequest);

        File localFile = Paths.get(destinationFolder, key).toFile();
        localFile.getParentFile().mkdirs(); // Crea directorios si no existen

        try (FileOutputStream fos = new FileOutputStream(localFile)) {
            byte[] read_buf = new byte[1024];
            int read_len;
            while ((read_len = s3ObjectResponse.read(read_buf)) > 0) {
                fos.write(read_buf, 0, read_len);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("Descarga completada.\n");
    }
}
