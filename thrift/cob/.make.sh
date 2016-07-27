gcc -g -I/usr/include/thrift -L/usr/lib/ -lthrift -lthriftnb -levent -lm -pthread -lz -lrt -lssl   asyncServer.cpp test_constants.cpp Test.cpp test_types.cpp -o asyncServer
gcc -g -I/usr/include/thrift -L/usr/lib/ -lthrift -lthriftnb -levent -lm -pthread -lz -lrt -lssl   test_constants.cpp Test.cpp test_types.cpp  asyncClient.cpp -o asyncClient

