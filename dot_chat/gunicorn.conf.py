# Gunicorn configuration for Django

bind = "0.0.0.0:8000"

# Number of worker processes
workers = 2

# Number of threads per worker
threads = 4

# Request timeout in seconds
timeout = 120

# Keep connections alive
keepalive = 5

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"