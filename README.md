# WebPicrawler

Docker image for getting screenshot of website homepage.


## Use

```
docker build -t webpicrawler:0.0.1 .
docker run -it -u root -v /Users/moonswing/Desktop/:/data webpicrawler:0.0.1 --website-url http://blog.computbiol.com --output-dir /data
```



## Ref

https://chromedriver.chromium.org/downloads
