thrift --gen cpp HelloThrift.thrift 
thrift --gen py HelloThrift.thrift
mv .make.sh gen-cpp/make.sh
mv .client.py gen-py/client.py
cd gen-cpp/ && sh make.sh

