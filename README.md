# Lifecycle system suite

This includes:

- Continuous Integration
- Continuous Deployment
- Infrastructure as Code
- Testing

# Bootstrap the integrator

```bash
docker build -t integration:latest -f docker/integration.Dockerfile .
```

# Run the integrator

```bash
export $PROJECT_DIR=/mnt/c/Users/ccanellas/Proyectos/pruebas/cicd-docker-python
docker run \
    --rm -it \
    -e BUILD_PATH=/build \
    -v /mnt/c/Users/ccanellas/Proyectos/pruebas/cicd-docker-python:/build \
    -v /var/run/docker.sock:/var/run/docker.sock \
    integration:latest [--debug] build integration:latest ./docker/integration.Dockerfile
```