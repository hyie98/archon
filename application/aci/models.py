# -*- coding: utf-8 -*-
################################################################################
#        _____ _                  _____           _                            #
#       / ____(_)                / ____|         | |                           #
#      | |     _ ___  ___ ___   | (___  _   _ ___| |_ ___ _ __ ___  ___        #
#      | |    | / __|/ __/ _ \   \___ \| | | / __| __/ _ \ '_ ` _ \/ __|       #
#      | |____| \__ \ (_| (_) |  ____) | |_| \__ \ ||  __/ | | | | \__ \       #
#       \_____|_|___/\___\___/  |_____/ \__, |___/\__\___|_| |_| |_|___/       #
#                                        __/ |                                 #
#                                       |___/                                  #
#           _  __                       _____       _  _____ ______            #
#          | |/ /                      / ____|     | |/ ____|  ____|           #
#          | ' / ___  _ __ ___  __ _  | (___   ___ | | (___ | |__              #
#          |  < / _ \| '__/ _ \/ _` |  \___ \ / _ \| |\___ \|  __|             #
#          | . \ (_) | | |  __/ (_| |  ____) | (_) | |____) | |____            #
#          |_|\_\___/|_|  \___|\__,_| |_____/ \___/|_|_____/|______|           #
#                                                                              #
################################################################################
#                                                                              #
# Copyright (c) 2016 Cisco Systems                                             #
# All Rights Reserved.                                                         #
#                                                                              #
# Licensed under the Apache License, Version 2.0 (the "License"); you may      #
# not use this file except in compliance with the License. You may obtain      #
# a copy of the License at                                                     #
#                                                                              #
# http://www.apache.org/licenses/LICENSE-2.0                                   #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT #
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  #
#    License for the specific language governing permissions and limitations   #
#    under the License.                                                        #
#                                                                              #
################################################################################

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from archon import modelview

#===============================================================================
# Create your models here.
#===============================================================================

class Domain(models.Model):
    name = models.CharField(max_length=64)
    controllers = models.CharField(max_length=64)
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    created_date = models.DateTimeField(default=timezone.now)

modelview(Domain)

class EPTracker(models.Model):
    mac = models.CharField(max_length=18)
    ip = models.CharField(max_length=16)
    domain = models.CharField(max_length=64)
    tenant = models.CharField(max_length=100)
    app = models.CharField(max_length=100)
    epg = models.CharField(max_length=100)
    dn = models.CharField(max_length=2048)
    intf = models.CharField(max_length=2048)
    start = models.CharField(max_length=24)
    stop = models.CharField(max_length=24)

modelview(EPTracker)

class FaultMessage(models.Model):
    code = models.CharField(max_length=8)
    title = models.CharField(max_length=512)
    syslog = models.TextField()
    explan = models.TextField()
    actions = models.TextField()

modelview(FaultMessage)
