# twitter-kafka-streaming
Streaming data from twitter with apache kafka

## installing dependencies:
```
python3 -m pip install -r requirements.txt
```

## Setting up kafka
1. download the latest kafka binary tar from https://kafka.apache.org/downloads
2. Extract the tar 
```
$ tar -xzf kafka_2.x-2.x.x.tgz
$ cd kafka_2.x-2.x.x
```
3. Start the Kafka Environment (use different terminals for both)
> a. Start ZooKeeper Service
> ```
> $ bin/zookeeper-server-start.sh config/zookeeper.properties
> ```
> b.  Start the Kafka broker service
> ```
> $ bin/kafka-server-start.sh config/server.properties
> ```
4. Test the kafka setup 
> a. Create a test-events topic to store the events
> ```
> $ bin/kafka-topics.sh --create --topic test-events --bootstrap-server localhost:9092
> ```
> b. Create a producer to write events into the topic 
> ```
> $ bin/kafka-console-producer.sh --topic test-events --bootstrap-server localhost:9092
> ```
> c. Create a consumer to read events from the topic 
> ```
> $ bin/kafka-console-consumer.sh --topic test-events --from-beginning --bootstrap-server localhost:9092
> ```
> add some data to the producer terminal, the consumer will show the same data.

5. To check the details of the topic 
```
$ bin/kafka-topics.sh --describe --topic test-events --bootstrap-server localhost:9092
```
6. To list all available topics
```
$ bin/kafka-topics.sh --list --zookeeper localhost:2181
```
To terminate the kafka environment, use `Ctrl+C`, first close producers and consumers, then kafka-broker and lastly Zookeeper 
