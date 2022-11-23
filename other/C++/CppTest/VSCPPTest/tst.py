import rx7 as rx

r = rx.record()
rx.terminal.run("g++ -std=c++11 tst.cpp")
#rx.terminal.run("g++ -std=c++11 RX7.hpp")

print(r.lap())