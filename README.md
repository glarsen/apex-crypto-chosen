# APEX - "chosen"

A crypto challenge to demonstrate the power of
[chosen plaintext attacks](https://en.wikipedia.org/wiki/Chosen-plaintext_attack)
against monoalphabetic ciphers. Inspired by
[Over the Wire - Krypton](http://overthewire.org/wargames/krypton/krypton2.html).

### Building & Testing

```
docker build -t apex-crypto-chosen .
docker run -d --rm --name apex-crypto-chosen -p 8000:8000 -e KEY='...' apex-crypto-chosen
nc localhost 8000
```

### Production

Deploy with [Docker Swarm](https://docs.docker.com/engine/swarm/).

### Flags

For testing, pass the key into the container via an environment
variable named `KEY`. For production, pass the key as a
[Docker secret](https://git.io/vxZJF).

