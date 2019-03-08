import os
import zipfile
import oss2
from pymongo import MongoClient
import datetime

DBClient = MongoClient(os.getenv('MONGODB_URL'))
# DBClient = MongoClient()
download_file = DBClient['download']['download_file']


class UploadFile(object):
    def __init__(self, file_name, file_path, bucket_name):
        """
        :param file_name: 保存至OSS文件名称,自己起名，也可为文件名
        :param file_path:  文件所在路径
        :param bucket_name: 仓库名称
        :return 保存至 oss/mongo 的文件名，仓库名
        注意： 上传文件夹不要重名，否则会被覆盖
        """
        self.path = file_path
        self.auth = oss2.Auth(os.getenv('AccessKeyId'), os.getenv('AccessKeySecret'))
        self.bucket_name = bucket_name
        self.endpoint = os.getenv('Endpoint')
        self.filename = file_name

    def upload(self, path, file_name):
        """上传文件"""
        print('开始上传文件')
        bucket = oss2.Bucket(self.auth, self.endpoint, self.bucket_name)
        bucket.put_object_from_file(file_name, path)
        print('保存至Oss成功')
        # with open(path, 'rb') as fileobj:
        #     # fileobj.seek(1000, os.SEEK_SET)
        #     # current = fileobj.tell()
        #     bucket.put_object(file_name, fileobj)

    def save_mongodb(self):
        try:
            download_file.insert_one({"name": 'oss-spider-{}'.format(self.filename), "bucketname": self.bucket_name,
                                      'data': datetime.datetime.now().strftime('%Y-%m-%d')})
        except Exception as e:
            print('保存mongo数据库失败: %s' % e)
        print('保存至数据库成功')
        return 'oss-spider-{}'.format(self.filename), self.bucket_name

    def zip_dir(self):
        """
        判断是否为文件
        压缩文件 - > 指定文件夹
        """
        if os.path.isdir(self.path):
            print('开始压缩文件')
            zip = zipfile.ZipFile(self.path + '.zip', "w", zipfile.ZIP_DEFLATED)
            for path, dirnames, filenames in os.walk(self.path):
                fpath = path.replace(self.path, '')
                for filename in filenames:
                    zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
            zip.close()
            return 'oss-spider-{}'.format(self.filename), self.path + '.zip'
        return 'oss-spider-{}'.format(self.filename), self.path

    def start_upload(self):
        name, path = self.zip_dir()
        self.upload(path=path, file_name=name)
        file_name, bucket_name = self.save_mongodb()
        print('上传结束')
        return file_name, bucket_name


if __name__ == '__main__':
    a = UploadFile(file_name='<your-file-name>', file_path=r'<your-file-path>', bucket_name=os.getenv('BucketName'))
    a.start_upload()
