import os
import json
from lxml import etree
from redis import Redis
redis = Redis(db=10)

def add_bucket(path):
    '''Adds a new bucket.
    
    
    :rtype : list
    :param path: Bucket name
    :return:
    '''
    data = {'name': path}
    redis.hset('buckets', path, json.dumps(data))
    result = [('Location', '/' + path), ('Content-Length', '0'),
              ('Connection', 'close'), ('Server', 'AmazonS3')]
    return result

