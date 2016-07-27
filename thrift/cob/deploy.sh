thrift --gen cpp:cob_style test.thrift
mv .asyncClient.cpp gen-cpp/asyncClient.cpp
mv .asyncServer.cpp gen-cpp/asyncServer.cpp
mv .make.sh gen-cpp/make.sh
cd gen-cpp && sh make.sh
