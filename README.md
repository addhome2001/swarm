use Minikube

ingress controller

step 1
Start by creating the “mandatory” resources for Nginx Ingress in your cluster.
========

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml

step 2
minikube addons enable ingress
========

nginx
kubectl create configmap nginx-config --from-file=./app-ui/nginx.conf


...continues