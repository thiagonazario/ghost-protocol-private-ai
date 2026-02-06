# Use a lightweight CUDA base for performance and security
FROM ollama/ollama:latest

# Methodology: Hardened by Design - Metadata for auditability
LABEL maintainer="Thiago Nazario"
LABEL standard="DevSecOps"
LABEL project="Ghost-Protocol"

# Expose only the necessary local port for inference
EXPOSE 11434

# Healthcheck to ensure Fiscal Efficiency (don't run if broken)
HEALTHCHECK --interval=30s --timeout=5s \
  CMD ollama list || exit 1

# Entrypoint to start the Sovereign AI engine
ENTRYPOINT ["ollama", "serve"]