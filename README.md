Kafka Velib
=================

**API utilisé** : https://api.jcdecaux.com/vls/v1/stations
**IDE utilisé** : VS Code
**OS** : MAC

### Installation :

Package kafka-python :
https://kafka-python.readthedocs.io/en/master/

Zookeeper broker :
https://zookeeper.apache.org/

Kafka apache :
https://kafka.apache.org/

### Lancer le projet :

1. Lancer zookeeper :
`./bin/zookeeper-server-start.sh ./config/zookeeper.properties`

2. Lancer un cluster kafka :
`./bin/kafka-server-start.sh ./config/server.properties`

3. Créer un topic velib-stations :
`./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic velib-stations`

4. Lancer le producer velib-get-stations :
`python ./velib-get-stations.py`

5. Lancer le consumer velib-monitor-stations :
`python ./velib-monitor-stations.py`



Basé sur :
https://openclassrooms.com/fr/courses/4451251-gerez-des-flux-de-donnees-temps-reel/4451521-metamorphosez-vos-applications-temps-reel-avec-kafka
