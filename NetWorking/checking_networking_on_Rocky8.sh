#!/bin/bash

nmcli general status
nmcli connection show

nmcli connection up enp0s3
