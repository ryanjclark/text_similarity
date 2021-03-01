IMG_TAG="$(git rev-parse --short HEAD)"
IMG=rclarkaptive/text-similarity

docker build -t "$IMG":"$IMG_TAG" -t "$IMG":latest . && \
    docker push "$IMG":"$IMG_TAG" && \
    docker push "$IMG":latest
