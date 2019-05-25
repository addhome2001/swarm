Step 1
Install and run [Minikube](https://github.com/kubernetes/minikube#installation)
```
minikube start
```
---
Step 2
Create the “mandatory” resources for Nginx Ingress in your cluster.
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml
```
---
Step 3 Setup Nginx ingress as an add-on
```
minikube addons enable ingress
```
---
Step 4 Create config-map for `app-ui`
```
kubectl create configmap app-ui-nginx-config --from-file=./app-ui/nginx.conf
```
---
Step 5 Apply all of the yaml files for k8s
```
kubectl apply -f .
kubectl apply -f app-api/k8s
kubectl apply -f app-db/k8s
kubectl apply -f app-ui/k8s
```
---
Step 6 Add your IP(`minukube ip`) to your etc/hosts
```
<ip> my-app.com
```


