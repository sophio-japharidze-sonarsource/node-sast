FROM alpine:3.14
ENTRYPOINT ["/app", "-c", "config.json"] -D