#!/bin/bash

sudo sysctl -w net.ipv4.conf.all.secure_redirects=1
sudo sysctl -w net.ipv4.conf.br-fc87214a94fb.secure_redirects=1
sudo sysctl -w net.ipv4.conf.default.secure_redirects=1
sudo sysctl -w net.ipv4.conf.docker0.secure_redirects=1
sudo sysctl -w net.ipv4.conf.enp58s0.secure_redirects=1
sudo sysctl -w net.ipv4.conf.lo.secure_redirects=1
sudo sysctl -w net.ipv4.conf.wlp0s20f3.secure_redirects=1
sudo sysctl -w net.ipv4.conf.all.accept_redirects=0
echo 'check'
sudo sysctl -a | grep redir

