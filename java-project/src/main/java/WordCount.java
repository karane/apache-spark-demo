public class WordCount {
    public static void main(String[] args) {
        // No need for args, we're using a fixed path
        String inputFilePath = "/tmp/data/input.txt";

        // Create a Java Spark Context
        SparkConf conf = new SparkConf().setAppName("WordCount").setMaster("spark://spark-master:7077");
        JavaSparkContext sc = new JavaSparkContext(conf);

        // Load the input data
        JavaRDD<String> lines = sc.textFile(inputFilePath);

        // Split lines into words
        JavaRDD<String> words = lines.flatMap(line -> Arrays.asList(line.split(" ")).iterator());

        // Count each word
        JavaRDD<Tuple2<String, Integer>> wordCounts = words
            .mapToPair(word -> new Tuple2<>(word, 1))
            .reduceByKey((count1, count2) -> count1 + count2);

        // Print the result
        wordCounts.collect().forEach(tuple -> System.out.println(tuple._1() + ": " + tuple._2()));

        // Stop the Spark context
        sc.stop();
    }
}
