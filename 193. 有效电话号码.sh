#!/bin/bash

fileName=$1

awk '/(^[0-9]{3}-|^\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/{print $0}' "${fileName}"
