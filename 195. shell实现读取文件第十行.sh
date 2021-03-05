#!/bin/bash

fileName=$1
rowNum=$(cat "${fileName}" | wc -l)

if [[ $rowNum -lt 10 ]];then
  echo "The number of row is less than 10"
else
  # 方法一
  awk 'NR==10{print $0}' "${fileName}"
  # 方法二
  grep -n "" "${fileName}" | grep -w '10' | cut -d: -f 2
  # 方法三
  sed -n '10p' "${fileName}"
fi