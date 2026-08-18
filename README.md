# Kubernetes Production Deployment

Flask API deployed to Kubernetes with Deployment, Service, ConfigMap, Secret, health probes, resource limits, rolling updates, HPA, and Ingress.

## Build
```bash
docker build -t day303-api:1.0 .
```
For Minikube:
```bash
minikube image load day303-api:1.0
```

## Deploy
```bash
kubectl apply -k k8s/
```

## Check
```bash
kubectl get pods -n day303
kubectl get services -n day303
kubectl get deployments -n day303
```

## Test
```bash
kubectl port-forward service/day303-api 5000:80 -n day303
```
Open `http://localhost:5000/health`.

## Scale
```bash
kubectl scale deployment day303-api --replicas=5 -n day303
```

## Rolling update
Build/load `day303-api:1.1`, then:
```bash
kubectl set image deployment/day303-api api=day303-api:1.1 -n day303
kubectl rollout status deployment/day303-api -n day303
```
Rollback:
```bash
kubectl rollout undo deployment/day303-api -n day303
```

Day 303 / 365
