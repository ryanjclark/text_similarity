# Text Similarity

## Run with Docker
`docker pull docker.io/rclarkaptive/text-similarity:latest`  
  
`docker run -p 8000:8000 docker.io/rclarkaptive/text-similarity`  
  
View the docs at `http://localhost:8000/docs`  
  
```
curl -X \  
    POST \  
    "http://localhost:8000/api/v1/text-similarity" \  
    -H  "accept: application/json" \  
    -H  "Content-Type: application/json" \  
    -d "{\"doc_1\":\"firstString\",\"doc_2\":\"secondString\"}"
```

## Levenshtein
I am using Levenshtein's Distance algorithm to calculate text similarity. The algorithm returns an integer that represents how many modifications (inserts, deletions, substitutions) is necessary to change one string into another string. The higher the integer from Levenshtein, the more different the strings are.  

In my application, Levenshtein's Distance has `O(nm)` time and `O(nm)` space, where n and m are the length of the strings. It can be further optimized to only store part of the matrix, which can lower the space complexity to `O(min(n, m))`.
