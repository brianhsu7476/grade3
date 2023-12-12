# 加分項目

我的 server 有用 multithread ，支援多個 client 。

# 網址與 Port Number

server 在 0.0.0.0:8585
httpServer 在 0.0.0.0:8080

# 編譯
```
g++ -o server server.cpp
g++ -o client client.cpp
g++ -o httpServer httpServer.cpp
```

# 執行

server-client:
```
./server
./client
# input something to client
```

http server: 會跑出 profile.html 的頁面
```
./httpServer
```
