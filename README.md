### 介绍

本项目主要功能为阿里OSS上传文件用

### 安装

```
pipenv install -e git+https://github.com/xgoteam/spider_file_upload.git@master#egg=spider_file_upload
```

### 使用

```python
from spider_file_upload.upload_file import UploadFile

upload = UploadFile(file_path="<your-filename>", bucket_name=os.getenv('OSS_BUCKET_NAME'))

upload.start_upload()
```

### 注意

`file_path="<your-filename>"` 代表文件路径，最后的文件名不能重复，否则会被覆盖。

`bucket_name=os.getenv('OSS_BUCKET_NAME')` 代表仓库名称



### 需要添加环境变量 
```
OSS_ACCESS_KEYID =
OSS_ACCESS_KEY_SECRET =
OSS_BUCKET_NAME = 
OSS_ENDPOINT = 
MONGODB_URL = 

```
