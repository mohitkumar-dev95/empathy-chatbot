#!/bin/sh
# Copy the mounted kubeconfig so we don't accidentally modify your real Windows file!
cp /root/.kube/config /tmp/kubeconfig

# Replace 127.0.0.1 with host.docker.internal so the container can reach out to Windows
sed -i 's/127.0.0.1/host.docker.internal/g' /tmp/kubeconfig

# Disable TLS verification because the cert is only valid for localhost, not host.docker.internal
sed -i 's/certificate-authority-data:.*/insecure-skip-tls-verify: true/g' /tmp/kubeconfig
export KUBECONFIG=/tmp/kubeconfig

# Execute the ansible command passed from Docker
exec ansible-playbook "$@"
