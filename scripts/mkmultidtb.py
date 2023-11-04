#!/usr/bin/env python3
# SPDX-License-Identifier: (GPL-2.0+ OR MIT)
# Copyright (c) 2018 Fuzhou Rockchip Electronics Co., Ltd
# Copyright (C) 2023 Fewtarius


"""
Multiple dtb package tool

Usage: scripts/mkmultidtb.py board
The board is what you defined in DTBS dictionary like DTBS['board'],
Such as: PX30-EVB, RK3308-EVB

"""
import os
import sys
import shutil
from collections import OrderedDict

DTBS = {}

DTBS['PX30-EVB'] = OrderedDict([('px30-evb-ddr3-v10', '#_saradc_ch0=1024'),
				('px30-evb-ddr3-lvds-v10', '#_saradc_ch0=512')])

DTBS['RK3308-EVB'] = OrderedDict([('rk3308-evb-dmic-i2s-v10', '#_saradc_ch3=288'),
				  ('rk3308-evb-dmic-pdm-v10', '#_saradc_ch3=1024'),
				  ('rk3308-evb-amic-v10', '#_saradc_ch3=407')])

DTBS['rk356x'] = OrderedDict([('rk3566-rg353p-linux', '#_saradc_ch1=852'),
			      ('rk3566-rg353m-linux', '#_saradc_ch1=512'),
			      ('rk3566-rg353v-linux', '#_saradc_ch1=681'),
			      ('rk3566-rk2023-linux', '#_saradc_ch1=650'),
			      ('rk3566-rgb30-linux', '#_saradc_ch1=383'),
			      ('rk3566-rg503-linux', '#_saradc_ch1=1023')])

DTBS['rk3588'] = OrderedDict([('rk3588s-orangepi-5', '#_saradc_ch1=001'),
                              ('rk3588-rock-5b', '#_saradc_ch1=002'),
			      ('rk3588s-indiedroid-nova', '#_saradc_ch1=4095')])

def main():

    BOARD = sys.argv[1]
    TARGET_DTBS = DTBS[BOARD]
    target_dtb_list = ''
    default_dtb = False

    for dtb, value in TARGET_DTBS.items():
        if default_dtb:
            ori_file = 'arch/arm64/boot/dts/rockchip/' + dtb + '.dtb'
            shutil.copyfile(ori_file, "rk-kernel.dtb")
            target_dtb_list += 'rk-kernel.dtb '
            default_dtb = False
        new_file = dtb + value + '.dtb'
        ori_file = 'arch/arm64/boot/dts/rockchip/' + dtb + '.dtb'
        shutil.copyfile(ori_file, new_file)
        target_dtb_list += ' ' + new_file

    print (target_dtb_list)
    os.system('scripts/resource_tool ' + target_dtb_list)
    os.system('rm ' + target_dtb_list)

if __name__ == '__main__':
    main()
