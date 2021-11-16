#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
token = os.environ.get("token", "default")

if token == "default":
    raise Exception("Missing token!")
