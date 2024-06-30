import java.util.Map;

public class S3Download extends Utils {


    public static void main(String[] args) {
        System.out.println("-- INICIA --");
        String bucketName;
        String destinationFolder;
        String awsProfile;
        Boolean donwload;

        // Ruta del archivo de configuración
        String pathToConfig = args[0];

        Map<String, String> configMap = getJsonValues(pathToConfig);

        bucketName = configMap.get(BUCKETNAME);
        destinationFolder = configMap.get(DESTINATIONFOLDER);
        awsProfile = configMap.get(AWSPROFILE);
        donwload = Boolean.parseBoolean(configMap.get(DOWNLOAD));

        S3DownloadPorcess(bucketName, destinationFolder, awsProfile, donwload);
    }

}