from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()

class BlogPostIndex(Document):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()

    class Index:
        name = 'blogpost-index'

    def bulk_indexing():
        BlogPostIndex.init()
        es = Elasticsearch()
        bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))