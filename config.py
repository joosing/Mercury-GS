###################################################################################
# @file config.py
###################################################################################
#   _  _____ ____  ____  _____
#  | |/ /_ _/ ___||  _ \| ____|
#  | ' / | |\___ \| |_) |  _|
#  | . \ | |___ ) |  __/| |___
#  |_|\_\___|____/|_|   |_____|
###################################################################################
# Copyright (c) 2020 KISPE Space Systems Ltd.
#
# Please follow the following link for the license agreement for this code:
# www.kispe.co.uk/projectlicenses/RA2001001003
###################################################################################
#  Created on: 06-May-2021
#  Mercury GS Global Variables
#  @author: Jamie Bayley (jbayley@kispe.co.uk)
###################################################################################

# Initialise Global Variables
BAUD_RATE = 9600
TC_TLM_RATE = 1

# Function Pointers
global ptr_unpacketise
global ptr_telemetry_update
global ptr_telecommand_response_update
