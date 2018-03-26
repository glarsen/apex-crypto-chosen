FROM python:3-alpine

LABEL maintainer="garrett.larsen@protonmail.com" \
      language="python" \
      category="crypto"

# Install dependencies
RUN apk add --no-cache \
  socat

# Expose default port
EXPOSE 8000

# Build & Install
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["/usr/src/app/exec.sh"]

