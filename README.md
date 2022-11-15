# louis-GitGuardian-test

Environment: 
MacOS: v12.5 (Apple M1)
Minikube v1.28.0
Kubernetes client v1.25.4
Kubernetes server v1.25.3


2) I have added a startup Shell Script and a Python Script to a ConfigMap created via the following command:
 k create cm sample-app-configmap --from-file scripts/ --dry-run=client -o yaml | k apply -f -
 I have the defined alias k='kubectl' in my ~/.zshrc
 I have generated the yaml for the ConfigMap with the following command:
 k get configmap sample-app-configmap -o yaml > sample-app-configMap.yaml
 
 
4) In order to expose the service from the minikube node to my browser, I used the following command:
minikube service sample-app --url


Questions:
1) On a managed cluster, I would use an ingress to configure inbound access to the application since a relevant controller would be readily available and would work correctly out of the box. That option also seems more appropriate to me because it is an abstraction provided by kubernetes itself as opposed to a minikube specific command like the one I had to run at point 4 above.

2) In order to monitor the application, I would rely on centralize solutions like Kibana, Prometheus or influxDB coupled with Grafana so that I can analize the state over long periods of time and I can easily run ad-hoc queries when needed.

3) to add a PostgreSQL container, I would make sure to use a StatefulSet instead of relying on ReplicaSets because they work better when it comes to persistency, and data consistency. It is necessary for pods to maintain a stable identify in order to retain those properties.

4) Feedback:

a) Taking this test took much longer than I expected. It did not seem so at first but it touches quite a vast number of topics. One really needs to have optimal knowledge of the topics involved in order to complete it within the alloted time in my opinion.

b) I would rate this test a 7. I don't find it particularly hard. However, unless one is already comfortable with all the topics, it seems quite long (as mentioned above).

c) I definitely found the test interesting. I really enjoyed going through it. It was sometimes challenging for me because I was not familiar with all the concepts but it was equally rewarding when I was making progress. I am actually planning to complete the last question as soon as I have more time to dedicate to it. It was really fun to go through it.
