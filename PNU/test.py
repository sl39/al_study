import sys
import google.protobuf.text_format as tf
from bareunpy import Tagger
API_KEY = "koba-WEIDHEI-FBPETCA-QKMXX7I-YF6LL7Y"
tagger = Tagger(API_KEY, 'localhost')
# 결과를 가져옵니다.
res = tagger.tags(["안녕하세요.", "바른을 사용해서 새로운 경험을 해보세요."])