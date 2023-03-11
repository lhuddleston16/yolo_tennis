# Databricks notebook source
from scripts.argparse import create_parser
print("hello world")
param_value = dbutils.widgets.get("key1")
print(param_value)