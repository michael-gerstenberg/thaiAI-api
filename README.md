# thaiAI-api

## General information



## Deployed on uberspace

1. clone repo
2. setup and activate python environment, install required packages
   ```sh
   $ virtualenv -p python3 ENV
   $ source ENV/bin/activate
   $ pip install requirements.txt
   ```
3. set port in nginx
   ```sh
   $ uberspace web backend set / --http --port 1024
   ```
4. setup daemon (refresh supvervisord config)
   ```sh
   $ supervisorctl restart flask
   $ supervisorctl update
   ```

## Example POST

```
POST https://thaiai.uber.space/syl_segment HTTP/1.1
content-type: application/json

{
    "text": "เวลาหลังเที่ยงคืนถึงเที่ยงวัน"
}
```

## Contact

Michael - michael@thaiai.de

Robin - robin@thaiai.de


## Acknowledgements

* [thai language toolkit](https://pypi.org/project/tltk/)
* [flask installation on uberspace](https://lab.uberspace.de/guide_flask.html)
