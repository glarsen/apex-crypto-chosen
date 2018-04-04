FROM python:3-alpine

LABEL maintainer="garrett.larsen@protonmail.com" \
      language="python" \
      category="crypto"

# Install dependencies
RUN apk add --no-cache \
  socat

# Expose default port
EXPOSE 8000

# Create unprivileged, socat user
RUN adduser -SDH sdoe

# Build & Install
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Execute as socat user
USER sdoe
CMD ["/usr/src/app/exec.sh"]

