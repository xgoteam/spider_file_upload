### 介绍

本项目主要用于上传文件至阿里OSS

### 安装

```
pipenv install -e git+https://github.com/xgoteam/spider_file_upload.git#egg=spider_file_upload
```

### 使用

```python
    from spider_uplod.upload_file import UploadFile
    upload = UploadFile(file_path="<your-filename>", bucket_name=os.getenv('OSS_BUCKET_NAME'))
    upload.start_upload()
    
```
### 注意

file_path="<your-filename>  参数代表文件名路径，文件名称不能重复，否则会覆盖源文件